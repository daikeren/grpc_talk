import grpc

import hello_pb2
import hello_pb2_grpc


def run(name):
    channel = grpc.insecure_channel('localhost:50051')
    stub = hello_pb2_grpc.HelloStub(channel)    
    try:
        response = stub.Echo(hello_pb2.Request(name=name))
        print(response.val)
    except grpc.RpcError as e:
        status_code = e.code()        
        print(e.details())
        print(status_code.name)
    

if __name__ == '__main__':
    print("Normal GRPC Call")
    run(name='World')
    print("GRPC with Error")
    run(name='')
