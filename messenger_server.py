from concurrent import futures
import logging
import grpc
import threading
import datetime
import messenger_pb2
import messenger_pb2_grpc
import sys
import PySimpleGUI as sg


from ChatMenu import ChatWindow
from message import Message


class Server(messenger_pb2_grpc.MessengerServicer):
    def __init__(self, name):
        self.name = name
        self.connected = False
        self.client_name = None
        self.messages = []
        self.main_window = None
        self.serve()



    def startMessaging(self, request, context):
        logging.info(f'got name "{request.name}"')
        if not self.connected:
            self.client_name = request.name
            self.connected = True

            self.main_window = ChatWindow(self, 'Server')
            return messenger_pb2.MessengerNameResponse(name=self.name, connected=True)

        else:
            return messenger_pb2.MessengerNameResponse(connected=False)

    def stopMessaging(self, request, context):
        logging.info('disconnected')
        self.connected = False
        self.client_name = None
        self.messages = []
        self.main_window.window.close()
        yield messenger_pb2.Empty()
        sys.exit()



        
        
        
    def sendMessage(self, request_iterator, context):
        self.main_window = ChatWindow(self, 'Server')
        while self.connected:
            mes = self.main_window.processing()
            self.main_window.print(Message(mes, self.name, datetime.datetime.now(), 'server'))
            self.messages.append(Message(mes, self.name, datetime.datetime.now(), 'server'))
            yield messenger_pb2.MessengerMessage(message=mes)


    def getMessage(self, request, context):
        logging.info(f'got message "{request.message}" from {self.client_name}')
        self.main_window.print(Message(request.message, self.client_name, datetime.datetime.now(), 'client'))
        self.messages.append(Message(request.message, self.client_name, datetime.datetime.now(), 'client'))
        return messenger_pb2.Empty()

    def serve(self):
        
        server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        messenger_pb2_grpc.add_MessengerServicer_to_server(self, server)
        port = "50051"
        server.add_insecure_port(f"[::]:{port}")
        print(f"localhost:{port}")
        server.start()
        server.wait_for_termination()
