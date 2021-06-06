# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: messenger.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='messenger.proto',
  package='messenger',
  syntax='proto3',
  serialized_options=b'\n\030com.azaat.grpcchatclientB\016MessengerProto',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0fmessenger.proto\x12\tmessenger\"#\n\x10MessengerMessage\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x07\n\x05\x45mpty\"$\n\x14MessengerNameRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\"8\n\x15MessengerNameResponse\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x11\n\tconnected\x18\x02 \x01(\x08\x32\x92\x02\n\tMessenger\x12;\n\ngetMessage\x12\x1b.messenger.MessengerMessage\x1a\x10.messenger.Empty\x12>\n\x0bsendMessage\x12\x10.messenger.Empty\x1a\x1b.messenger.MessengerMessage0\x01\x12S\n\x0estartMessaging\x12\x1f.messenger.MessengerNameRequest\x1a .messenger.MessengerNameResponse\x12\x33\n\rstopMessaging\x12\x10.messenger.Empty\x1a\x10.messenger.EmptyB*\n\x18\x63om.azaat.grpcchatclientB\x0eMessengerProtob\x06proto3'
)




_MESSENGERMESSAGE = _descriptor.Descriptor(
  name='MessengerMessage',
  full_name='messenger.MessengerMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='messenger.MessengerMessage.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=65,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='messenger.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=74,
)


_MESSENGERNAMEREQUEST = _descriptor.Descriptor(
  name='MessengerNameRequest',
  full_name='messenger.MessengerNameRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='messenger.MessengerNameRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=76,
  serialized_end=112,
)


_MESSENGERNAMERESPONSE = _descriptor.Descriptor(
  name='MessengerNameResponse',
  full_name='messenger.MessengerNameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='messenger.MessengerNameResponse.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='connected', full_name='messenger.MessengerNameResponse.connected', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['MessengerMessage'] = _MESSENGERMESSAGE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['MessengerNameRequest'] = _MESSENGERNAMEREQUEST
DESCRIPTOR.message_types_by_name['MessengerNameResponse'] = _MESSENGERNAMERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MessengerMessage = _reflection.GeneratedProtocolMessageType('MessengerMessage', (_message.Message,), {
  'DESCRIPTOR' : _MESSENGERMESSAGE,
  '__module__' : 'messenger_pb2'
  # @@protoc_insertion_point(class_scope:messenger.MessengerMessage)
  })
_sym_db.RegisterMessage(MessengerMessage)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'messenger_pb2'
  # @@protoc_insertion_point(class_scope:messenger.Empty)
  })
_sym_db.RegisterMessage(Empty)

MessengerNameRequest = _reflection.GeneratedProtocolMessageType('MessengerNameRequest', (_message.Message,), {
  'DESCRIPTOR' : _MESSENGERNAMEREQUEST,
  '__module__' : 'messenger_pb2'
  # @@protoc_insertion_point(class_scope:messenger.MessengerNameRequest)
  })
_sym_db.RegisterMessage(MessengerNameRequest)

MessengerNameResponse = _reflection.GeneratedProtocolMessageType('MessengerNameResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSENGERNAMERESPONSE,
  '__module__' : 'messenger_pb2'
  # @@protoc_insertion_point(class_scope:messenger.MessengerNameResponse)
  })
_sym_db.RegisterMessage(MessengerNameResponse)


DESCRIPTOR._options = None

_MESSENGER = _descriptor.ServiceDescriptor(
  name='Messenger',
  full_name='messenger.Messenger',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=173,
  serialized_end=447,
  methods=[
  _descriptor.MethodDescriptor(
    name='getMessage',
    full_name='messenger.Messenger.getMessage',
    index=0,
    containing_service=None,
    input_type=_MESSENGERMESSAGE,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='sendMessage',
    full_name='messenger.Messenger.sendMessage',
    index=1,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_MESSENGERMESSAGE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='startMessaging',
    full_name='messenger.Messenger.startMessaging',
    index=2,
    containing_service=None,
    input_type=_MESSENGERNAMEREQUEST,
    output_type=_MESSENGERNAMERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='stopMessaging',
    full_name='messenger.Messenger.stopMessaging',
    index=3,
    containing_service=None,
    input_type=_EMPTY,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_MESSENGER)

DESCRIPTOR.services_by_name['Messenger'] = _MESSENGER

# @@protoc_insertion_point(module_scope)
