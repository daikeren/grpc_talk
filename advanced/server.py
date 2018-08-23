import time
import grpc
from concurrent import futures

import advanced_pb2
import advanced_pb2_grpc


class HelloService(advanced_pb2_grpc.HelloServicer):

    def Echo(self, request_iterator, context):
        count = 0
        print("Enter Echo")

        for request in request_iterator:
            count += 1
            name = request.name
            response = f'{count}: Hello {name}'
            yield advanced_pb2.Response(val=response)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    advanced_pb2_grpc.add_HelloServicer_to_server(HelloService(), server)
    server.add_insecure_port('127.0.0.1:50051')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()