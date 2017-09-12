# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: karps/proto/api_internal.proto

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


from karps.proto import computation_pb2 as karps_dot_proto_dot_computation__pb2
from karps.proto import graph_pb2 as karps_dot_proto_dot_graph__pb2
from karps.proto import interface_pb2 as karps_dot_proto_dot_interface__pb2
from karps.proto import io_pb2 as karps_dot_proto_dot_io__pb2
from tensorflow.core.framework import graph_pb2 as tensorflow_dot_core_dot_framework_dot_graph__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='karps/proto/api_internal.proto',
  package='karps.core',
  syntax='proto3',
  serialized_pb=_b('\n\x1ekarps/proto/api_internal.proto\x12\nkarps.core\x1a\x1dkarps/proto/computation.proto\x1a\x17karps/proto/graph.proto\x1a\x1bkarps/proto/interface.proto\x1a\x14karps/proto/io.proto\x1a%tensorflow/core/framework/graph.proto\"\xae\x02\n\x15PerformGraphTransform\x12&\n\x07session\x18\x01 \x01(\x0b\x32\x15.karps.core.SessionId\x12.\n\x0b\x63omputation\x18\x02 \x01(\x0b\x32\x19.karps.core.ComputationId\x12+\n\x10\x66unctional_graph\x18\x03 \x01(\x0b\x32\x11.karps.core.Graph\x12\x30\n\x0f\x61vailable_nodes\x18\x04 \x03(\x0b\x32\x17.karps.core.NodeMapItem\x12)\n\x0frequested_paths\x18\x05 \x03(\x0b\x32\x10.karps.core.Path\x12\x33\n\x0fknown_resources\x18\x06 \x03(\x0b\x32\x1a.karps.core.ResourceStatus\"\xc4\x01\n\x16GraphTransformResponse\x12\'\n\x0cpinned_graph\x18\x01 \x01(\x0b\x32\x11.karps.core.Graph\x12)\n\x08node_map\x18\x02 \x03(\x0b\x32\x17.karps.core.NodeMapItem\x12-\n\x08messages\x18\x03 \x03(\x0b\x32\x1b.karps.core.AnalysisMessage\x12\'\n\x05steps\x18\x04 \x03(\x0b\x32\x18.karps.core.CompilerStep\"f\n\x0eResourceStatus\x12*\n\x08resource\x18\x01 \x01(\x0b\x32\x18.karps.core.ResourcePath\x12(\n\x05stamp\x18\x02 \x01(\x0b\x32\x19.karps.core.ResourceStamp\"n\n\x17\x41nalyzeResourcesRequest\x12+\n\tresources\x18\x01 \x03(\x0b\x32\x18.karps.core.ResourcePath\x12&\n\x07session\x18\x02 \x01(\x0b\x32\x15.karps.core.SessionId\"\xd7\x01\n\x17\x41nalyzeResourceResponse\x12-\n\tsuccesses\x18\x01 \x03(\x0b\x32\x1a.karps.core.ResourceStatus\x12\x42\n\x08\x66\x61ilures\x18\x02 \x03(\x0b\x32\x30.karps.core.AnalyzeResourceResponse.FailedStatus\x1aI\n\x0c\x46\x61iledStatus\x12*\n\x08resource\x18\x01 \x01(\x0b\x32\x18.karps.core.ResourcePath\x12\r\n\x05\x65rror\x18\x02 \x01(\t\"\xa7\x01\n\x0bNodeMapItem\x12 \n\x04node\x18\x01 \x01(\x0b\x32\x12.karps.core.NodeId\x12\x1e\n\x04path\x18\x02 \x01(\x0b\x32\x10.karps.core.Path\x12.\n\x0b\x63omputation\x18\x03 \x01(\x0b\x32\x19.karps.core.ComputationId\x12&\n\x07session\x18\x04 \x01(\x0b\x32\x15.karps.core.SessionId\"\x84\x01\n\x0c\x43ompilerStep\x12)\n\x05phase\x18\x01 \x01(\x0e\x32\x1a.karps.core.CompilingPhase\x12 \n\x05graph\x18\x02 \x01(\x0b\x32\x11.karps.core.Graph\x12\'\n\tgraph_def\x18\x03 \x01(\x0b\x32\x14.tensorflow.GraphDef\"\x17\n\x06NodeId\x12\r\n\x05value\x18\x01 \x01(\t\"\xef\x01\n\x0f\x41nalysisMessage\x12.\n\x0b\x63omputation\x18\x01 \x01(\x0b\x32\x19.karps.core.ComputationId\x12&\n\x07session\x18\x02 \x01(\x0b\x32\x15.karps.core.SessionId\x12\'\n\x0brelevant_id\x18\x03 \x01(\x0b\x32\x12.karps.core.NodeId\x12\x1e\n\x04path\x18\x04 \x01(\x0b\x32\x10.karps.core.Path\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12*\n\x05level\x18\x06 \x01(\x0e\x32\x1b.karps.core.MessageSeverity*\xfc\x01\n\x0e\x43ompilingPhase\x12\x0b\n\x07INITIAL\x10\x00\x12\x16\n\x12REMOVE_UNREACHABLE\x10\x01\x12\x19\n\x15\x44\x41TA_SOURCE_INSERTION\x10\x02\x12\x12\n\x0ePOINTER_SWAP_1\x10\x03\x12\x16\n\x12MERGE_AGGREGATIONS\x10\x07\x12\x14\n\x10MERGE_TRANSFORMS\x10\x08\x12\x18\n\x14MERGE_AGGREGATIONS_2\x10\t\x12\x19\n\x15\x46UNCTIONAL_FLATTENING\x10\x04\x12\x16\n\x12\x41UTOCACHE_FULLFILL\x10\x05\x12\x0f\n\x0b\x43\x41\x43HE_CHECK\x10\x06\x12\n\n\x05\x46INAL\x10\xe8\x07*3\n\x0fMessageSeverity\x12\x08\n\x04INFO\x10\x00\x12\x0b\n\x07WARNING\x10\x01\x12\t\n\x05\x46\x41TAL\x10\x02\x32\xa8\x02\n\tKarpsRest\x12`\n\x11\x43reateComputation\x12$.karps.core.CreateComputationRequest\x1a%.karps.core.CreateComputationResponse\x12]\n\x11\x43omputationStatus\x12$.karps.core.ComputationStatusRequest\x1a\".karps.core.BatchComputationResult\x12Z\n\x0eResourceStatus\x12#.karps.core.AnalyzeResourcesRequest\x1a#.karps.core.AnalyzeResourceResponseb\x06proto3')
  ,
  dependencies=[karps_dot_proto_dot_computation__pb2.DESCRIPTOR,karps_dot_proto_dot_graph__pb2.DESCRIPTOR,karps_dot_proto_dot_interface__pb2.DESCRIPTOR,karps_dot_proto_dot_io__pb2.DESCRIPTOR,tensorflow_dot_core_dot_framework_dot_graph__pb2.DESCRIPTOR,])

_COMPILINGPHASE = _descriptor.EnumDescriptor(
  name='CompilingPhase',
  full_name='karps.core.CompilingPhase',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INITIAL', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='REMOVE_UNREACHABLE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATA_SOURCE_INSERTION', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POINTER_SWAP_1', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MERGE_AGGREGATIONS', index=4, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MERGE_TRANSFORMS', index=5, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MERGE_AGGREGATIONS_2', index=6, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FUNCTIONAL_FLATTENING', index=7, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AUTOCACHE_FULLFILL', index=8, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CACHE_CHECK', index=9, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FINAL', index=10, number=1000,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1703,
  serialized_end=1955,
)
_sym_db.RegisterEnumDescriptor(_COMPILINGPHASE)

CompilingPhase = enum_type_wrapper.EnumTypeWrapper(_COMPILINGPHASE)
_MESSAGESEVERITY = _descriptor.EnumDescriptor(
  name='MessageSeverity',
  full_name='karps.core.MessageSeverity',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INFO', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='WARNING', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FATAL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1957,
  serialized_end=2008,
)
_sym_db.RegisterEnumDescriptor(_MESSAGESEVERITY)

MessageSeverity = enum_type_wrapper.EnumTypeWrapper(_MESSAGESEVERITY)
INITIAL = 0
REMOVE_UNREACHABLE = 1
DATA_SOURCE_INSERTION = 2
POINTER_SWAP_1 = 3
MERGE_AGGREGATIONS = 7
MERGE_TRANSFORMS = 8
MERGE_AGGREGATIONS_2 = 9
FUNCTIONAL_FLATTENING = 4
AUTOCACHE_FULLFILL = 5
CACHE_CHECK = 6
FINAL = 1000
INFO = 0
WARNING = 1
FATAL = 2



_PERFORMGRAPHTRANSFORM = _descriptor.Descriptor(
  name='PerformGraphTransform',
  full_name='karps.core.PerformGraphTransform',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='session', full_name='karps.core.PerformGraphTransform.session', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='computation', full_name='karps.core.PerformGraphTransform.computation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='functional_graph', full_name='karps.core.PerformGraphTransform.functional_graph', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='available_nodes', full_name='karps.core.PerformGraphTransform.available_nodes', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requested_paths', full_name='karps.core.PerformGraphTransform.requested_paths', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='known_resources', full_name='karps.core.PerformGraphTransform.known_resources', index=5,
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
  serialized_start=193,
  serialized_end=495,
)


_GRAPHTRANSFORMRESPONSE = _descriptor.Descriptor(
  name='GraphTransformResponse',
  full_name='karps.core.GraphTransformResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pinned_graph', full_name='karps.core.GraphTransformResponse.pinned_graph', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='node_map', full_name='karps.core.GraphTransformResponse.node_map', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='messages', full_name='karps.core.GraphTransformResponse.messages', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='steps', full_name='karps.core.GraphTransformResponse.steps', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=498,
  serialized_end=694,
)


_RESOURCESTATUS = _descriptor.Descriptor(
  name='ResourceStatus',
  full_name='karps.core.ResourceStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource', full_name='karps.core.ResourceStatus.resource', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamp', full_name='karps.core.ResourceStatus.stamp', index=1,
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
  serialized_start=696,
  serialized_end=798,
)


_ANALYZERESOURCESREQUEST = _descriptor.Descriptor(
  name='AnalyzeResourcesRequest',
  full_name='karps.core.AnalyzeResourcesRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resources', full_name='karps.core.AnalyzeResourcesRequest.resources', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='karps.core.AnalyzeResourcesRequest.session', index=1,
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
  serialized_start=800,
  serialized_end=910,
)


_ANALYZERESOURCERESPONSE_FAILEDSTATUS = _descriptor.Descriptor(
  name='FailedStatus',
  full_name='karps.core.AnalyzeResourceResponse.FailedStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='resource', full_name='karps.core.AnalyzeResourceResponse.FailedStatus.resource', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='karps.core.AnalyzeResourceResponse.FailedStatus.error', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=1055,
  serialized_end=1128,
)

_ANALYZERESOURCERESPONSE = _descriptor.Descriptor(
  name='AnalyzeResourceResponse',
  full_name='karps.core.AnalyzeResourceResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='successes', full_name='karps.core.AnalyzeResourceResponse.successes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='failures', full_name='karps.core.AnalyzeResourceResponse.failures', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_ANALYZERESOURCERESPONSE_FAILEDSTATUS, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=913,
  serialized_end=1128,
)


_NODEMAPITEM = _descriptor.Descriptor(
  name='NodeMapItem',
  full_name='karps.core.NodeMapItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='node', full_name='karps.core.NodeMapItem.node', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='karps.core.NodeMapItem.path', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='computation', full_name='karps.core.NodeMapItem.computation', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='karps.core.NodeMapItem.session', index=3,
      number=4, type=11, cpp_type=10, label=1,
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
  serialized_start=1131,
  serialized_end=1298,
)


_COMPILERSTEP = _descriptor.Descriptor(
  name='CompilerStep',
  full_name='karps.core.CompilerStep',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phase', full_name='karps.core.CompilerStep.phase', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph', full_name='karps.core.CompilerStep.graph', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph_def', full_name='karps.core.CompilerStep.graph_def', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=1301,
  serialized_end=1433,
)


_NODEID = _descriptor.Descriptor(
  name='NodeId',
  full_name='karps.core.NodeId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='karps.core.NodeId.value', index=0,
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
  serialized_start=1435,
  serialized_end=1458,
)


_ANALYSISMESSAGE = _descriptor.Descriptor(
  name='AnalysisMessage',
  full_name='karps.core.AnalysisMessage',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='computation', full_name='karps.core.AnalysisMessage.computation', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='session', full_name='karps.core.AnalysisMessage.session', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='relevant_id', full_name='karps.core.AnalysisMessage.relevant_id', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='karps.core.AnalysisMessage.path', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='content', full_name='karps.core.AnalysisMessage.content', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='level', full_name='karps.core.AnalysisMessage.level', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=1461,
  serialized_end=1700,
)

_PERFORMGRAPHTRANSFORM.fields_by_name['session'].message_type = karps_dot_proto_dot_computation__pb2._SESSIONID
_PERFORMGRAPHTRANSFORM.fields_by_name['computation'].message_type = karps_dot_proto_dot_computation__pb2._COMPUTATIONID
_PERFORMGRAPHTRANSFORM.fields_by_name['functional_graph'].message_type = karps_dot_proto_dot_graph__pb2._GRAPH
_PERFORMGRAPHTRANSFORM.fields_by_name['available_nodes'].message_type = _NODEMAPITEM
_PERFORMGRAPHTRANSFORM.fields_by_name['requested_paths'].message_type = karps_dot_proto_dot_graph__pb2._PATH
_PERFORMGRAPHTRANSFORM.fields_by_name['known_resources'].message_type = _RESOURCESTATUS
_GRAPHTRANSFORMRESPONSE.fields_by_name['pinned_graph'].message_type = karps_dot_proto_dot_graph__pb2._GRAPH
_GRAPHTRANSFORMRESPONSE.fields_by_name['node_map'].message_type = _NODEMAPITEM
_GRAPHTRANSFORMRESPONSE.fields_by_name['messages'].message_type = _ANALYSISMESSAGE
_GRAPHTRANSFORMRESPONSE.fields_by_name['steps'].message_type = _COMPILERSTEP
_RESOURCESTATUS.fields_by_name['resource'].message_type = karps_dot_proto_dot_io__pb2._RESOURCEPATH
_RESOURCESTATUS.fields_by_name['stamp'].message_type = karps_dot_proto_dot_io__pb2._RESOURCESTAMP
_ANALYZERESOURCESREQUEST.fields_by_name['resources'].message_type = karps_dot_proto_dot_io__pb2._RESOURCEPATH
_ANALYZERESOURCESREQUEST.fields_by_name['session'].message_type = karps_dot_proto_dot_computation__pb2._SESSIONID
_ANALYZERESOURCERESPONSE_FAILEDSTATUS.fields_by_name['resource'].message_type = karps_dot_proto_dot_io__pb2._RESOURCEPATH
_ANALYZERESOURCERESPONSE_FAILEDSTATUS.containing_type = _ANALYZERESOURCERESPONSE
_ANALYZERESOURCERESPONSE.fields_by_name['successes'].message_type = _RESOURCESTATUS
_ANALYZERESOURCERESPONSE.fields_by_name['failures'].message_type = _ANALYZERESOURCERESPONSE_FAILEDSTATUS
_NODEMAPITEM.fields_by_name['node'].message_type = _NODEID
_NODEMAPITEM.fields_by_name['path'].message_type = karps_dot_proto_dot_graph__pb2._PATH
_NODEMAPITEM.fields_by_name['computation'].message_type = karps_dot_proto_dot_computation__pb2._COMPUTATIONID
_NODEMAPITEM.fields_by_name['session'].message_type = karps_dot_proto_dot_computation__pb2._SESSIONID
_COMPILERSTEP.fields_by_name['phase'].enum_type = _COMPILINGPHASE
_COMPILERSTEP.fields_by_name['graph'].message_type = karps_dot_proto_dot_graph__pb2._GRAPH
_COMPILERSTEP.fields_by_name['graph_def'].message_type = tensorflow_dot_core_dot_framework_dot_graph__pb2._GRAPHDEF
_ANALYSISMESSAGE.fields_by_name['computation'].message_type = karps_dot_proto_dot_computation__pb2._COMPUTATIONID
_ANALYSISMESSAGE.fields_by_name['session'].message_type = karps_dot_proto_dot_computation__pb2._SESSIONID
_ANALYSISMESSAGE.fields_by_name['relevant_id'].message_type = _NODEID
_ANALYSISMESSAGE.fields_by_name['path'].message_type = karps_dot_proto_dot_graph__pb2._PATH
_ANALYSISMESSAGE.fields_by_name['level'].enum_type = _MESSAGESEVERITY
DESCRIPTOR.message_types_by_name['PerformGraphTransform'] = _PERFORMGRAPHTRANSFORM
DESCRIPTOR.message_types_by_name['GraphTransformResponse'] = _GRAPHTRANSFORMRESPONSE
DESCRIPTOR.message_types_by_name['ResourceStatus'] = _RESOURCESTATUS
DESCRIPTOR.message_types_by_name['AnalyzeResourcesRequest'] = _ANALYZERESOURCESREQUEST
DESCRIPTOR.message_types_by_name['AnalyzeResourceResponse'] = _ANALYZERESOURCERESPONSE
DESCRIPTOR.message_types_by_name['NodeMapItem'] = _NODEMAPITEM
DESCRIPTOR.message_types_by_name['CompilerStep'] = _COMPILERSTEP
DESCRIPTOR.message_types_by_name['NodeId'] = _NODEID
DESCRIPTOR.message_types_by_name['AnalysisMessage'] = _ANALYSISMESSAGE
DESCRIPTOR.enum_types_by_name['CompilingPhase'] = _COMPILINGPHASE
DESCRIPTOR.enum_types_by_name['MessageSeverity'] = _MESSAGESEVERITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PerformGraphTransform = _reflection.GeneratedProtocolMessageType('PerformGraphTransform', (_message.Message,), dict(
  DESCRIPTOR = _PERFORMGRAPHTRANSFORM,
  __module__ = 'karps.proto.api_internal_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.PerformGraphTransform)
  ))
_sym_db.RegisterMessage(PerformGraphTransform)

GraphTransformResponse = _reflection.GeneratedProtocolMessageType('GraphTransformResponse', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHTRANSFORMRESPONSE,
  __module__ = 'karps.proto.api_internal_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.GraphTransformResponse)
  ))
_sym_db.RegisterMessage(GraphTransformResponse)

ResourceStatus = _reflection.GeneratedProtocolMessageType('ResourceStatus', (_message.Message,), dict(
  DESCRIPTOR = _RESOURCESTATUS,
  __module__ = 'karps.proto.api_internal_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.ResourceStatus)
  ))
_sym_db.RegisterMessage(ResourceStatus)

AnalyzeResourcesRequest = _reflection.GeneratedProtocolMessageType('AnalyzeResourcesRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZERESOURCESREQUEST,
  __module__ = 'karps.proto.api_internal_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.AnalyzeResourcesRequest)
  ))
_sym_db.RegisterMessage(AnalyzeResourcesRequest)

AnalyzeResourceResponse = _reflection.GeneratedProtocolMessageType('AnalyzeResourceResponse', (_message.Message,), dict(

  FailedStatus = _reflection.GeneratedProtocolMessageType('FailedStatus', (_message.Message,), dict(
    DESCRIPTOR = _ANALYZERESOURCERESPONSE_FAILEDSTATUS,
    __module__ = 'karps.proto.api_internal_pb2'
    # @@protoc_insertion_point(class_scope:karps.core.AnalyzeResourceResponse.FailedStatus)
    ))
  ,
  DESCRIPTOR = _ANALYZERESOURCERESPONSE,
  __module__ = 'karps.proto.api_internal_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.AnalyzeResourceResponse)
  ))
_sym_db.RegisterMessage(AnalyzeResourceResponse)
_sym_db.RegisterMessage(AnalyzeResourceResponse.FailedStatus)

NodeMapItem = _reflection.GeneratedProtocolMessageType('NodeMapItem', (_message.Message,), dict(
  DESCRIPTOR = _NODEMAPITEM,
  __module__ = 'karps.proto.api_internal_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.NodeMapItem)
  ))
_sym_db.RegisterMessage(NodeMapItem)

CompilerStep = _reflection.GeneratedProtocolMessageType('CompilerStep', (_message.Message,), dict(
  DESCRIPTOR = _COMPILERSTEP,
  __module__ = 'karps.proto.api_internal_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.CompilerStep)
  ))
_sym_db.RegisterMessage(CompilerStep)

NodeId = _reflection.GeneratedProtocolMessageType('NodeId', (_message.Message,), dict(
  DESCRIPTOR = _NODEID,
  __module__ = 'karps.proto.api_internal_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.NodeId)
  ))
_sym_db.RegisterMessage(NodeId)

AnalysisMessage = _reflection.GeneratedProtocolMessageType('AnalysisMessage', (_message.Message,), dict(
  DESCRIPTOR = _ANALYSISMESSAGE,
  __module__ = 'karps.proto.api_internal_pb2'
  # @@protoc_insertion_point(class_scope:karps.core.AnalysisMessage)
  ))
_sym_db.RegisterMessage(AnalysisMessage)


try:
  # THESE ELEMENTS WILL BE DEPRECATED.
  # Please use the generated *_pb2_grpc.py files instead.
  import grpc
  from grpc.beta import implementations as beta_implementations
  from grpc.beta import interfaces as beta_interfaces
  from grpc.framework.common import cardinality
  from grpc.framework.interfaces.face import utilities as face_utilities


  class KarpsRestStub(object):
    """This service is not implemented in GRPC.
    It is implemented as a collection of RPC calls that accepts proto byte strings.
    This is useful for languages that do not have GRPC support.
    """

    def __init__(self, channel):
      """Constructor.

      Args:
        channel: A grpc.Channel.
      """
      self.CreateComputation = channel.unary_unary(
          '/karps.core.KarpsRest/CreateComputation',
          request_serializer=karps_dot_proto_dot_interface__pb2.CreateComputationRequest.SerializeToString,
          response_deserializer=karps_dot_proto_dot_interface__pb2.CreateComputationResponse.FromString,
          )
      self.ComputationStatus = channel.unary_unary(
          '/karps.core.KarpsRest/ComputationStatus',
          request_serializer=karps_dot_proto_dot_interface__pb2.ComputationStatusRequest.SerializeToString,
          response_deserializer=karps_dot_proto_dot_computation__pb2.BatchComputationResult.FromString,
          )
      self.ResourceStatus = channel.unary_unary(
          '/karps.core.KarpsRest/ResourceStatus',
          request_serializer=AnalyzeResourcesRequest.SerializeToString,
          response_deserializer=AnalyzeResourceResponse.FromString,
          )


  class KarpsRestServicer(object):
    """This service is not implemented in GRPC.
    It is implemented as a collection of RPC calls that accepts proto byte strings.
    This is useful for languages that do not have GRPC support.
    """

    def CreateComputation(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ComputationStatus(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')

    def ResourceStatus(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.set_code(grpc.StatusCode.UNIMPLEMENTED)
      context.set_details('Method not implemented!')
      raise NotImplementedError('Method not implemented!')


  def add_KarpsRestServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'CreateComputation': grpc.unary_unary_rpc_method_handler(
            servicer.CreateComputation,
            request_deserializer=karps_dot_proto_dot_interface__pb2.CreateComputationRequest.FromString,
            response_serializer=karps_dot_proto_dot_interface__pb2.CreateComputationResponse.SerializeToString,
        ),
        'ComputationStatus': grpc.unary_unary_rpc_method_handler(
            servicer.ComputationStatus,
            request_deserializer=karps_dot_proto_dot_interface__pb2.ComputationStatusRequest.FromString,
            response_serializer=karps_dot_proto_dot_computation__pb2.BatchComputationResult.SerializeToString,
        ),
        'ResourceStatus': grpc.unary_unary_rpc_method_handler(
            servicer.ResourceStatus,
            request_deserializer=AnalyzeResourcesRequest.FromString,
            response_serializer=AnalyzeResourceResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'karps.core.KarpsRest', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


  class BetaKarpsRestServicer(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """This service is not implemented in GRPC.
    It is implemented as a collection of RPC calls that accepts proto byte strings.
    This is useful for languages that do not have GRPC support.
    """
    def CreateComputation(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ComputationStatus(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)
    def ResourceStatus(self, request, context):
      # missing associated documentation comment in .proto file
      pass
      context.code(beta_interfaces.StatusCode.UNIMPLEMENTED)


  class BetaKarpsRestStub(object):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This class was generated
    only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0."""
    """This service is not implemented in GRPC.
    It is implemented as a collection of RPC calls that accepts proto byte strings.
    This is useful for languages that do not have GRPC support.
    """
    def CreateComputation(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    CreateComputation.future = None
    def ComputationStatus(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    ComputationStatus.future = None
    def ResourceStatus(self, request, timeout, metadata=None, with_call=False, protocol_options=None):
      # missing associated documentation comment in .proto file
      pass
      raise NotImplementedError()
    ResourceStatus.future = None


  def beta_create_KarpsRest_server(servicer, pool=None, pool_size=None, default_timeout=None, maximum_timeout=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_deserializers = {
      ('karps.core.KarpsRest', 'ComputationStatus'): karps_dot_proto_dot_interface__pb2.ComputationStatusRequest.FromString,
      ('karps.core.KarpsRest', 'CreateComputation'): karps_dot_proto_dot_interface__pb2.CreateComputationRequest.FromString,
      ('karps.core.KarpsRest', 'ResourceStatus'): AnalyzeResourcesRequest.FromString,
    }
    response_serializers = {
      ('karps.core.KarpsRest', 'ComputationStatus'): karps_dot_proto_dot_computation__pb2.BatchComputationResult.SerializeToString,
      ('karps.core.KarpsRest', 'CreateComputation'): karps_dot_proto_dot_interface__pb2.CreateComputationResponse.SerializeToString,
      ('karps.core.KarpsRest', 'ResourceStatus'): AnalyzeResourceResponse.SerializeToString,
    }
    method_implementations = {
      ('karps.core.KarpsRest', 'ComputationStatus'): face_utilities.unary_unary_inline(servicer.ComputationStatus),
      ('karps.core.KarpsRest', 'CreateComputation'): face_utilities.unary_unary_inline(servicer.CreateComputation),
      ('karps.core.KarpsRest', 'ResourceStatus'): face_utilities.unary_unary_inline(servicer.ResourceStatus),
    }
    server_options = beta_implementations.server_options(request_deserializers=request_deserializers, response_serializers=response_serializers, thread_pool=pool, thread_pool_size=pool_size, default_timeout=default_timeout, maximum_timeout=maximum_timeout)
    return beta_implementations.server(method_implementations, options=server_options)


  def beta_create_KarpsRest_stub(channel, host=None, metadata_transformer=None, pool=None, pool_size=None):
    """The Beta API is deprecated for 0.15.0 and later.

    It is recommended to use the GA API (classes and functions in this
    file not marked beta) for all further purposes. This function was
    generated only to ease transition from grpcio<0.15.0 to grpcio>=0.15.0"""
    request_serializers = {
      ('karps.core.KarpsRest', 'ComputationStatus'): karps_dot_proto_dot_interface__pb2.ComputationStatusRequest.SerializeToString,
      ('karps.core.KarpsRest', 'CreateComputation'): karps_dot_proto_dot_interface__pb2.CreateComputationRequest.SerializeToString,
      ('karps.core.KarpsRest', 'ResourceStatus'): AnalyzeResourcesRequest.SerializeToString,
    }
    response_deserializers = {
      ('karps.core.KarpsRest', 'ComputationStatus'): karps_dot_proto_dot_computation__pb2.BatchComputationResult.FromString,
      ('karps.core.KarpsRest', 'CreateComputation'): karps_dot_proto_dot_interface__pb2.CreateComputationResponse.FromString,
      ('karps.core.KarpsRest', 'ResourceStatus'): AnalyzeResourceResponse.FromString,
    }
    cardinalities = {
      'ComputationStatus': cardinality.Cardinality.UNARY_UNARY,
      'CreateComputation': cardinality.Cardinality.UNARY_UNARY,
      'ResourceStatus': cardinality.Cardinality.UNARY_UNARY,
    }
    stub_options = beta_implementations.stub_options(host=host, metadata_transformer=metadata_transformer, request_serializers=request_serializers, response_deserializers=response_deserializers, thread_pool=pool, thread_pool_size=pool_size)
    return beta_implementations.dynamic_stub(channel, 'karps.core.KarpsRest', cardinalities, options=stub_options)
except ImportError:
  pass
# @@protoc_insertion_point(module_scope)
