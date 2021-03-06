# GRPC-Chat

GRPC-chat is a basic cross-platform p2p messenger, which is implemented as a part of SPbU Software Architecture course.

## *Architecture*

![Class diagram](./grpc.png)

There are 4 rpc-methods:

### rpc *getMessage* (MessengerMessage) returns (Empty)

Client calls *getMessage* for sending only message to server. Server returns nothing.

### rpc *sendMessage* (Empty) returns (stream MessengerMessage)

Client calls *sendMessage* for getting stream of messages from server. When next message has created, it is sent throughout stream to client.

### rpc *startMessaging* (MessengerNameRequest) returns (MessengerNameResponse)

Client calls *startMessaging* when it want to connect to server, say its name and receive server's name.

### rpc *stopMessaging* (Empty) returns (Empty)

Client calls *stopMessaging* when client want to disconnect.

## *How to run in Linux?*

  * Server:
```
$ make simple_server name=$server_name port=$port
```
  * Client:
```
$ make simple_client name=$client_name host=$server_host port=$port
```

## *How to run in Linux via docker?*

  * Server:
```
$ make simple_server_docker name=$server_name port=$port
```
  * Client:
```
$ make simple_client_docker name=$client_name host=$server_host port=$port
```

## *How to run in Windows (or in Linux without make)?*

1)  Install requirements:
```
$ python -m pip install --upgrade pip
$ python -m pip install -r requirements.txt
```

2)  Generate additional files from proto-file:
```
$ python -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. shared_proto/messenger.proto
```

3)  Run server or client:
```
$ python main.py --mode={server,client} --name=$client_or_server_name --port=$port --host=$server_host_for_client
```

## *Android client*

### Screenshots
<img src="https://imgur.com/EV34VRa.png" width="300">

### Usage

1) Install [the client](./client.apk)
2) Launch server on pc and get *server hostname*
3) Send messages from text field

### Client architecture details

- ```ClientActivity``` duplicates logic from python client
- ```ApplicationInterface``` provides calls for various client events, which perform the required UI modifications (```onDisconnect```, ```onConnectionInitiated```)
  - The app has two layouts (connection and chat layout). When disconnected, it switches to connection layout and waits for user login
