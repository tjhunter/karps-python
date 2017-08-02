# karps-python
Python bindings for the Karps project

## Development note.

The proto interface is generated this way (from the root of the karps-python project):

PYTHONPATH="" python3 -m grpc_tools.protoc -I../karps/src/main/protobuf/ --python_out=. --grpc_python_out=. ../karps/src/main/protobuf/karps/proto/computation.proto ../karps/src/main/protobuf/karps/proto/graph.proto ../karps/src/main/protobuf/karps/proto/interface.proto ../karps/src/main/protobuf/karps/proto/io.proto ../karps/src/main/protobuf/karps/proto/row.proto ../karps/src/main/protobuf/karps/proto/structured_transform.proto ../karps/src/main/protobuf/karps/proto/types.proto
