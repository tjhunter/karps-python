# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: karps/proto/computation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from karps.proto import graph_pb2 as karps_dot_proto_dot_graph__pb2
from karps.proto import row_pb2 as karps_dot_proto_dot_row__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='karps/proto/computation.proto',
  package='karps.core',
  syntax='proto3',
  serialized_pb=_b('\n\x1dkarps/proto/computation.proto\x12\nkarps.core\x1a\x17karps/proto/graph.proto\x1a\x15karps/proto/row.proto\"\xfd\x01\n\x11\x43omputationResult\x12$\n\nlocal_path\x18\x01 \x01(\x0b\x32\x10.karps.core.Path\x12(\n\x06status\x18\x02 \x01(\x0e\x32\x18.karps.core.ResultStatus\x12\x13\n\x0b\x66inal_error\x18\x03 \x01(\t\x12.\n\x0c\x66inal_result\x18\x04 \x01(\x0b\x32\x18.karps.core.CellWithType\x12+\n\x0bspark_stats\x18\x05 \x01(\x0b\x32\x16.karps.core.SparkStats\x12&\n\x0c\x64\x65pendencies\x18\x06 \x03(\x0b\x32\x10.karps.core.Path\"o\n\x16\x42\x61tchComputationResult\x12%\n\x0btarget_path\x18\x01 \x01(\x0b\x32\x10.karps.core.Path\x12.\n\x07results\x18\x02 \x03(\x0b\x32\x1d.karps.core.ComputationResult\"c\n\x0bPointerPath\x12.\n\x0b\x63omputation\x18\x01 \x01(\x0b\x32\x19.karps.core.ComputationId\x12$\n\nlocal_path\x18\x02 \x01(\x0b\x32\x10.karps.core.Path\"3\n\nSparkStats\x12%\n\x08rdd_info\x18\x01 \x03(\x0b\x32\x13.karps.core.RDDInfo\"L\n\x07RDDInfo\x12\x0e\n\x06rdd_id\x18\x01 \x01(\x03\x12\x12\n\nclass_name\x18\x02 \x01(\t\x12\x0c\n\x04repr\x18\x03 \x01(\t\x12\x0f\n\x07parents\x18\x04 \x03(\x03\"\x1b\n\rComputationId\x12\n\n\x02id\x18\x01 \x01(\t\"\x17\n\tSessionId\x12\n\n\x02id\x18\x01 \x01(\t*b\n\x0cResultStatus\x12\n\n\x06UNUSED\x10\x00\x12\x0b\n\x07RUNNING\x10\x01\x12\x14\n\x10\x46INISHED_SUCCESS\x10\x02\x12\x14\n\x10\x46INISHED_FAILURE\x10\x03\x12\r\n\tSCHEDULED\x10\x04\x62\x06proto3')
  ,
  dependencies=[karps_dot_proto_dot_graph__pb2.DESCRIPTOR,karps_dot_proto_dot_row__pb2.DESCRIPTOR,])

_RESULTSTATUS = _descriptor.EnumDescriptor(
  name='ResultStatus',
  full_name='karps.core.ResultStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNUSED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RUNNING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISHED_SUCCESS', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINISHED_FAILURE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SCHEDULED', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=748,
  serialized_end=846,
)
_sym_db.RegisterEnumDescriptor(_RESULTSTATUS)

ResultStatus = enum_type_wrapper.EnumTypeWrapper(_RESULTSTATUS)
UNUSED = 0
RUNNING = 1
FINISHED_SUCCESS = 2
FINISHED_FAILURE = 3
SCHEDULED = 4



_COMPUTATIONRESULT = _descriptor.Descriptor(
  name='ComputationResult',
  full_name='karps.core.ComputationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='local_path', full_name='karps.core.ComputationResult.local_path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='status', full_name='karps.core.ComputationResult.status', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='final_error', full_name='karps.core.ComputationResult.final_error', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='final_result', full_name='karps.core.ComputationResult.final_result', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spark_stats', full_name='karps.core.ComputationResult.spark_stats', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dependencies', full_name='karps.core.ComputationResult.dependencies', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=94,
  serialized_end=347,
)


_BATCHCOMPUTATIONRESULT = _descriptor.Descriptor(
  name='BatchComputationResult',
  full_name='karps.core.BatchComputationResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target_path', full_name='karps.core.BatchComputationResult.target_path', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='results', full_name='karps.core.BatchComputationResult.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=349,
  serialized_end=460,
)


_POINTERPATH = _descriptor.Descriptor(
  name='PointerPath',
  full_name='karps.core.PointerPath',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='computation', full_name='karps.core.PointerPath.computation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='local_path', full_name='karps.core.PointerPath.local_path', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=462,
  serialized_end=561,
)


_SPARKSTATS = _descriptor.Descriptor(
  name='SparkStats',
  full_name='karps.core.SparkStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rdd_info', full_name='karps.core.SparkStats.rdd_info', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=563,
  serialized_end=614,
)


_RDDINFO = _descriptor.Descriptor(
  name='RDDInfo',
  full_name='karps.core.RDDInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rdd_id', full_name='karps.core.RDDInfo.rdd_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='class_name', full_name='karps.core.RDDInfo.class_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='repr', full_name='karps.core.RDDInfo.repr', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parents', full_name='karps.core.RDDInfo.parents', index=3,
      number=4, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=616,
  serialized_end=692,
)


_COMPUTATIONID = _descriptor.Descriptor(
  name='ComputationId',
  full_name='karps.core.ComputationId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='karps.core.ComputationId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=694,
  serialized_end=721,
)


_SESSIONID = _descriptor.Descriptor(
  name='SessionId',
  full_name='karps.core.SessionId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='karps.core.SessionId.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=723,
  serialized_end=746,
)

_COMPUTATIONRESULT.fields_by_name['local_path'].message_type = karps_dot_proto_dot_graph__pb2._PATH
_COMPUTATIONRESULT.fields_by_name['status'].enum_type = _RESULTSTATUS
_COMPUTATIONRESULT.fields_by_name['final_result'].message_type = karps_dot_proto_dot_row__pb2._CELLWITHTYPE
_COMPUTATIONRESULT.fields_by_name['spark_stats'].message_type = _SPARKSTATS
_COMPUTATIONRESULT.fields_by_name['dependencies'].message_type = karps_dot_proto_dot_graph__pb2._PATH
_BATCHCOMPUTATIONRESULT.fields_by_name['target_path'].message_type = karps_dot_proto_dot_graph__pb2._PATH
_BATCHCOMPUTATIONRESULT.fields_by_name['results'].message_type = _COMPUTATIONRESULT
_POINTERPATH.fields_by_name['computation'].message_type = _COMPUTATIONID
_POINTERPATH.fields_by_name['local_path'].message_type = karps_dot_proto_dot_graph__pb2._PATH
_SPARKSTATS.fields_by_name['rdd_info'].message_type = _RDDINFO
DESCRIPTOR.message_types_by_name['ComputationResult'] = _COMPUTATIONRESULT
DESCRIPTOR.message_types_by_name['BatchComputationResult'] = _BATCHCOMPUTATIONRESULT
DESCRIPTOR.message_types_by_name['PointerPath'] = _POINTERPATH
DESCRIPTOR.message_types_by_name['SparkStats'] = _SPARKSTATS
DESCRIPTOR.message_types_by_name['RDDInfo'] = _RDDINFO
DESCRIPTOR.message_types_by_name['ComputationId'] = _COMPUTATIONID
DESCRIPTOR.message_types_by_name['SessionId'] = _SESSIONID
DESCRIPTOR.enum_types_by_name['ResultStatus'] = _RESULTSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComputationResult = _reflection.GeneratedProtocolMessageType('ComputationResult', (_message.Message,), dict(
  DESCRIPTOR = _COMPUTATIONRESULT,
  __module__ = 'karps.proto.computation_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.ComputationResult)
  ))
_sym_db.RegisterMessage(ComputationResult)

BatchComputationResult = _reflection.GeneratedProtocolMessageType('BatchComputationResult', (_message.Message,), dict(
  DESCRIPTOR = _BATCHCOMPUTATIONRESULT,
  __module__ = 'karps.proto.computation_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.BatchComputationResult)
  ))
_sym_db.RegisterMessage(BatchComputationResult)

PointerPath = _reflection.GeneratedProtocolMessageType('PointerPath', (_message.Message,), dict(
  DESCRIPTOR = _POINTERPATH,
  __module__ = 'karps.proto.computation_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.PointerPath)
  ))
_sym_db.RegisterMessage(PointerPath)

SparkStats = _reflection.GeneratedProtocolMessageType('SparkStats', (_message.Message,), dict(
  DESCRIPTOR = _SPARKSTATS,
  __module__ = 'karps.proto.computation_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.SparkStats)
  ))
_sym_db.RegisterMessage(SparkStats)

RDDInfo = _reflection.GeneratedProtocolMessageType('RDDInfo', (_message.Message,), dict(
  DESCRIPTOR = _RDDINFO,
  __module__ = 'karps.proto.computation_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.RDDInfo)
  ))
_sym_db.RegisterMessage(RDDInfo)

ComputationId = _reflection.GeneratedProtocolMessageType('ComputationId', (_message.Message,), dict(
  DESCRIPTOR = _COMPUTATIONID,
  __module__ = 'karps.proto.computation_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.ComputationId)
  ))
_sym_db.RegisterMessage(ComputationId)

SessionId = _reflection.GeneratedProtocolMessageType('SessionId', (_message.Message,), dict(
  DESCRIPTOR = _SESSIONID,
  __module__ = 'karps.proto.computation_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.SessionId)
  ))
_sym_db.RegisterMessage(SessionId)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
