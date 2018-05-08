# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: state.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='state.proto',
  package='',
  syntax='proto3',
  serialized_pb=_b('\n\x0bstate.proto\"\r\n\x0bStateFilter\"C\n\tStateInfo\x12\x1b\n\x03\x61pp\x18\x01 \x01(\x0b\x32\x0e.StateInfo.App\x1a\x19\n\x03\x41pp\x12\x12\n\nexecutable\x18\x01 \x01(\t2/\n\x05State\x12&\n\x08GetState\x12\x0c.StateFilter\x1a\n.StateInfo\"\x00\x62\x06proto3')
)




_STATEFILTER = _descriptor.Descriptor(
  name='StateFilter',
  full_name='StateFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=28,
)


_STATEINFO_APP = _descriptor.Descriptor(
  name='App',
  full_name='StateInfo.App',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='executable', full_name='StateInfo.App.executable', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=97,
)

_STATEINFO = _descriptor.Descriptor(
  name='StateInfo',
  full_name='StateInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app', full_name='StateInfo.app', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_STATEINFO_APP, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=30,
  serialized_end=97,
)

_STATEINFO_APP.containing_type = _STATEINFO
_STATEINFO.fields_by_name['app'].message_type = _STATEINFO_APP
DESCRIPTOR.message_types_by_name['StateFilter'] = _STATEFILTER
DESCRIPTOR.message_types_by_name['StateInfo'] = _STATEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StateFilter = _reflection.GeneratedProtocolMessageType('StateFilter', (_message.Message,), dict(
  DESCRIPTOR = _STATEFILTER,
  __module__ = 'state_pb2'
  # @@protoc_insertion_point(class_scope:StateFilter)
  ))
_sym_db.RegisterMessage(StateFilter)

StateInfo = _reflection.GeneratedProtocolMessageType('StateInfo', (_message.Message,), dict(

  App = _reflection.GeneratedProtocolMessageType('App', (_message.Message,), dict(
    DESCRIPTOR = _STATEINFO_APP,
    __module__ = 'state_pb2'
    # @@protoc_insertion_point(class_scope:StateInfo.App)
    ))
  ,
  DESCRIPTOR = _STATEINFO,
  __module__ = 'state_pb2'
  # @@protoc_insertion_point(class_scope:StateInfo)
  ))
_sym_db.RegisterMessage(StateInfo)
_sym_db.RegisterMessage(StateInfo.App)



_STATE = _descriptor.ServiceDescriptor(
  name='State',
  full_name='State',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=99,
  serialized_end=146,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetState',
    full_name='State.GetState',
    index=0,
    containing_service=None,
    input_type=_STATEFILTER,
    output_type=_STATEINFO,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_STATE)

DESCRIPTOR.services_by_name['State'] = _STATE

# @@protoc_insertion_point(module_scope)
