# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/cloud/spanner_v1/proto/result_set.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.cloud.spanner_v1.proto import query_plan_pb2 as google_dot_cloud_dot_spanner__v1_dot_proto_dot_query__plan__pb2
from google.cloud.spanner_v1.proto import transaction_pb2 as google_dot_cloud_dot_spanner__v1_dot_proto_dot_transaction__pb2
from google.cloud.spanner_v1.proto import type_pb2 as google_dot_cloud_dot_spanner__v1_dot_proto_dot_type__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='google/cloud/spanner_v1/proto/result_set.proto',
  package='google.spanner.v1',
  syntax='proto3',
  serialized_pb=_b('\n.google/cloud/spanner_v1/proto/result_set.proto\x12\x11google.spanner.v1\x1a\x1cgoogle/api/annotations.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a.google/cloud/spanner_v1/proto/query_plan.proto\x1a/google/cloud/spanner_v1/proto/transaction.proto\x1a(google/cloud/spanner_v1/proto/type.proto\"\x9f\x01\n\tResultSet\x12\x36\n\x08metadata\x18\x01 \x01(\x0b\x32$.google.spanner.v1.ResultSetMetadata\x12(\n\x04rows\x18\x02 \x03(\x0b\x32\x1a.google.protobuf.ListValue\x12\x30\n\x05stats\x18\x03 \x01(\x0b\x32!.google.spanner.v1.ResultSetStats\"\xd1\x01\n\x10PartialResultSet\x12\x36\n\x08metadata\x18\x01 \x01(\x0b\x32$.google.spanner.v1.ResultSetMetadata\x12&\n\x06values\x18\x02 \x03(\x0b\x32\x16.google.protobuf.Value\x12\x15\n\rchunked_value\x18\x03 \x01(\x08\x12\x14\n\x0cresume_token\x18\x04 \x01(\x0c\x12\x30\n\x05stats\x18\x05 \x01(\x0b\x32!.google.spanner.v1.ResultSetStats\"y\n\x11ResultSetMetadata\x12/\n\x08row_type\x18\x01 \x01(\x0b\x32\x1d.google.spanner.v1.StructType\x12\x33\n\x0btransaction\x18\x02 \x01(\x0b\x32\x1e.google.spanner.v1.Transaction\"p\n\x0eResultSetStats\x12\x30\n\nquery_plan\x18\x01 \x01(\x0b\x32\x1c.google.spanner.v1.QueryPlan\x12,\n\x0bquery_stats\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB}\n\x15\x63om.google.spanner.v1B\x0eResultSetProtoP\x01Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\xaa\x02\x17Google.Cloud.Spanner.V1b\x06proto3')
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,google_dot_protobuf_dot_struct__pb2.DESCRIPTOR,google_dot_cloud_dot_spanner__v1_dot_proto_dot_query__plan__pb2.DESCRIPTOR,google_dot_cloud_dot_spanner__v1_dot_proto_dot_transaction__pb2.DESCRIPTOR,google_dot_cloud_dot_spanner__v1_dot_proto_dot_type__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_RESULTSET = _descriptor.Descriptor(
  name='ResultSet',
  full_name='google.spanner.v1.ResultSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='google.spanner.v1.ResultSet.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rows', full_name='google.spanner.v1.ResultSet.rows', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats', full_name='google.spanner.v1.ResultSet.stats', index=2,
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
  serialized_start=269,
  serialized_end=428,
)


_PARTIALRESULTSET = _descriptor.Descriptor(
  name='PartialResultSet',
  full_name='google.spanner.v1.PartialResultSet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='metadata', full_name='google.spanner.v1.PartialResultSet.metadata', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='values', full_name='google.spanner.v1.PartialResultSet.values', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='chunked_value', full_name='google.spanner.v1.PartialResultSet.chunked_value', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='resume_token', full_name='google.spanner.v1.PartialResultSet.resume_token', index=3,
      number=4, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stats', full_name='google.spanner.v1.PartialResultSet.stats', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=431,
  serialized_end=640,
)


_RESULTSETMETADATA = _descriptor.Descriptor(
  name='ResultSetMetadata',
  full_name='google.spanner.v1.ResultSetMetadata',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='row_type', full_name='google.spanner.v1.ResultSetMetadata.row_type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='transaction', full_name='google.spanner.v1.ResultSetMetadata.transaction', index=1,
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
  serialized_start=642,
  serialized_end=763,
)


_RESULTSETSTATS = _descriptor.Descriptor(
  name='ResultSetStats',
  full_name='google.spanner.v1.ResultSetStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='query_plan', full_name='google.spanner.v1.ResultSetStats.query_plan', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='query_stats', full_name='google.spanner.v1.ResultSetStats.query_stats', index=1,
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
  serialized_start=765,
  serialized_end=877,
)

_RESULTSET.fields_by_name['metadata'].message_type = _RESULTSETMETADATA
_RESULTSET.fields_by_name['rows'].message_type = google_dot_protobuf_dot_struct__pb2._LISTVALUE
_RESULTSET.fields_by_name['stats'].message_type = _RESULTSETSTATS
_PARTIALRESULTSET.fields_by_name['metadata'].message_type = _RESULTSETMETADATA
_PARTIALRESULTSET.fields_by_name['values'].message_type = google_dot_protobuf_dot_struct__pb2._VALUE
_PARTIALRESULTSET.fields_by_name['stats'].message_type = _RESULTSETSTATS
_RESULTSETMETADATA.fields_by_name['row_type'].message_type = google_dot_cloud_dot_spanner__v1_dot_proto_dot_type__pb2._STRUCTTYPE
_RESULTSETMETADATA.fields_by_name['transaction'].message_type = google_dot_cloud_dot_spanner__v1_dot_proto_dot_transaction__pb2._TRANSACTION
_RESULTSETSTATS.fields_by_name['query_plan'].message_type = google_dot_cloud_dot_spanner__v1_dot_proto_dot_query__plan__pb2._QUERYPLAN
_RESULTSETSTATS.fields_by_name['query_stats'].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name['ResultSet'] = _RESULTSET
DESCRIPTOR.message_types_by_name['PartialResultSet'] = _PARTIALRESULTSET
DESCRIPTOR.message_types_by_name['ResultSetMetadata'] = _RESULTSETMETADATA
DESCRIPTOR.message_types_by_name['ResultSetStats'] = _RESULTSETSTATS

ResultSet = _reflection.GeneratedProtocolMessageType('ResultSet', (_message.Message,), dict(
  DESCRIPTOR = _RESULTSET,
  __module__ = 'google.cloud.spanner_v1.proto.result_set_pb2'
  ,
  __doc__ = """Results from [Read][google.spanner.v1.Spanner.Read] or
  [ExecuteSql][google.spanner.v1.Spanner.ExecuteSql].
  
  
  Attributes:
      metadata:
          Metadata about the result set, such as row type information.
      rows:
          Each element in ``rows`` is a row whose format is defined by [
          metadata.row\_type][google.spanner.v1.ResultSetMetadata.row\_t
          ype]. The ith element in each row matches the ith field in [me
          tadata.row\_type][google.spanner.v1.ResultSetMetadata.row\_typ
          e]. Elements are encoded based on type as described
          [here][google.spanner.v1.TypeCode].
      stats:
          Query plan and execution statistics for the query that
          produced this result set. These can be requested by setting [E
          xecuteSqlRequest.query\_mode][google.spanner.v1.ExecuteSqlRequ
          est.query\_mode].
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.ResultSet)
  ))
_sym_db.RegisterMessage(ResultSet)

PartialResultSet = _reflection.GeneratedProtocolMessageType('PartialResultSet', (_message.Message,), dict(
  DESCRIPTOR = _PARTIALRESULTSET,
  __module__ = 'google.cloud.spanner_v1.proto.result_set_pb2'
  ,
  __doc__ = """Partial results from a streaming read or SQL query. Streaming reads and
  SQL queries better tolerate large result sets, large rows, and large
  values, but are a little trickier to consume.
  
  
  Attributes:
      metadata:
          Metadata about the result set, such as row type information.
          Only present in the first response.
      values:
          A streamed result set consists of a stream of values, which
          might be split into many ``PartialResultSet`` messages to
          accommodate large rows and/or large values. Every N complete
          values defines a row, where N is equal to the number of
          entries in [metadata.row\_type.fields][google.spanner.v1.Struc
          tType.fields].  Most values are encoded based on type as
          described [here][google.spanner.v1.TypeCode].  It is possible
          that the last value in values is "chunked", meaning that the
          rest of the value is sent in subsequent ``PartialResultSet``\
          (s). This is denoted by the [chunked\_value][google.spanner.v1
          .PartialResultSet.chunked\_value] field. Two or more chunked
          values can be merged to form a complete value as follows:  -
          ``bool/number/null``: cannot be chunked -  ``string``:
          concatenate the strings -  ``list``: concatenate the lists. If
          the last element in a list is a    ``string``, ``list``, or
          ``object``, merge it with the first element    in the next
          list by applying these rules recursively. -  ``object``:
          concatenate the (field name, field value) pairs. If a    field
          name is duplicated, then apply these rules recursively to
          merge    the field values.  Some examples of merging:  ::
          # Strings are concatenated.     "foo", "bar" => "foobar"
          # Lists of non-strings are concatenated.     [2, 3], [4] =>
          [2, 3, 4]      # Lists are concatenated, but the last and
          first elements are merged     # because they are strings.
          ["a", "b"], ["c", "d"] => ["a", "bc", "d"]      # Lists are
          concatenated, but the last and first elements are merged     #
          because they are lists. Recursively, the last and first
          elements     # of the inner lists are merged because they are
          strings.     ["a", ["b", "c"]], [["d"], "e"] => ["a", ["b",
          "cd"], "e"]      # Non-overlapping object fields are combined.
          {"a": "1"}, {"b": "2"} => {"a": "1", "b": 2"}      #
          Overlapping object fields are merged.     {"a": "1"}, {"a":
          "2"} => {"a": "12"}      # Examples of merging objects
          containing lists of strings.     {"a": ["1"]}, {"a": ["2"]} =>
          {"a": ["12"]}  For a more complete example, suppose a
          streaming SQL query is yielding a result set whose rows
          contain a single string field. The following
          ``PartialResultSet``\ s might be yielded:  ::      {
          "metadata": { ... }       "values": ["Hello", "W"]
          "chunked_value": true       "resume_token": "Af65..."     }
          {       "values": ["orl"]       "chunked_value": true
          "resume_token": "Bqp2..."     }     {       "values": ["d"]
          "resume_token": "Zx1B..."     }  This sequence of
          ``PartialResultSet``\ s encodes two rows, one containing the
          field value ``"Hello"``, and a second containing the field
          value ``"World" = "W" + "orl" + "d"``.
      chunked_value:
          If true, then the final value in
          [values][google.spanner.v1.PartialResultSet.values] is
          chunked, and must be combined with more values from subsequent
          ``PartialResultSet``\ s to obtain a complete field value.
      resume_token:
          Streaming calls might be interrupted for a variety of reasons,
          such as TCP connection loss. If this occurs, the stream of
          results can be resumed by re-sending the original request and
          including ``resume_token``. Note that executing any other
          transaction in the same session invalidates the token.
      stats:
          Query plan and execution statistics for the query that
          produced this streaming result set. These can be requested by
          setting [ExecuteSqlRequest.query\_mode][google.spanner.v1.Exec
          uteSqlRequest.query\_mode] and are sent only once with the
          last response in the stream.
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.PartialResultSet)
  ))
_sym_db.RegisterMessage(PartialResultSet)

ResultSetMetadata = _reflection.GeneratedProtocolMessageType('ResultSetMetadata', (_message.Message,), dict(
  DESCRIPTOR = _RESULTSETMETADATA,
  __module__ = 'google.cloud.spanner_v1.proto.result_set_pb2'
  ,
  __doc__ = """Metadata about a [ResultSet][google.spanner.v1.ResultSet] or
  [PartialResultSet][google.spanner.v1.PartialResultSet].
  
  
  Attributes:
      row_type:
          Indicates the field names and types for the rows in the result
          set. For example, a SQL query like ``"SELECT UserId, UserName
          FROM Users"`` could return a ``row_type`` value like:  ::
          "fields": [       { "name": "UserId", "type": { "code":
          "INT64" } },       { "name": "UserName", "type": { "code":
          "STRING" } },     ]
      transaction:
          If the read or SQL query began a transaction as a side-effect,
          the information about the new transaction is yielded here.
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.ResultSetMetadata)
  ))
_sym_db.RegisterMessage(ResultSetMetadata)

ResultSetStats = _reflection.GeneratedProtocolMessageType('ResultSetStats', (_message.Message,), dict(
  DESCRIPTOR = _RESULTSETSTATS,
  __module__ = 'google.cloud.spanner_v1.proto.result_set_pb2'
  ,
  __doc__ = """Additional statistics about a [ResultSet][google.spanner.v1.ResultSet]
  or [PartialResultSet][google.spanner.v1.PartialResultSet].
  
  
  Attributes:
      query_plan:
          [QueryPlan][google.spanner.v1.QueryPlan] for the query
          associated with this result.
      query_stats:
          Aggregated statistics from the execution of the query. Only
          present when the query is profiled. For example, a query could
          return the statistics as follows:  ::      {
          "rows_returned": "3",       "elapsed_time": "1.22 secs",
          "cpu_time": "1.19 secs"     }
  """,
  # @@protoc_insertion_point(class_scope:google.spanner.v1.ResultSetStats)
  ))
_sym_db.RegisterMessage(ResultSetStats)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\025com.google.spanner.v1B\016ResultSetProtoP\001Z8google.golang.org/genproto/googleapis/spanner/v1;spanner\252\002\027Google.Cloud.Spanner.V1'))
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
