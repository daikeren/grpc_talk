import time

from concurrent import futures

import grpc

import hello_pb2
import hello_pb2_grpc


class HelloService(hello_pb2_grpc.HelloServicer):

    def Echo(self, request, context):
        print('Call Echo')
        name = request.name
        if name == '':
            context.set_details('大爆炸 Name should not be empty')
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)

        response = f"Hello {name}"
        return hello_pb2.Response(val=response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    hello_pb2_grpc.add_HelloServicer_to_server(HelloService(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
