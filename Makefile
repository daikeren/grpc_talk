TARGET=hello

build:
	cd $(TARGET) && python -m grpc_tools.protoc --proto_path=. --python_out=. --grpc_python_out=. *.proto
