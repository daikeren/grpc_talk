import time

import grpc

import advanced_pb2
import advanced_pb2_grpc


def gen_request():
    count = 1

    while 1:
        name = f"Name {count}"
        yield advanced_pb2.Request(name=name)
        time.sleep(1)
        count += 1


def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = advanced_pb2_grpc.HelloStub(channel)

    try:
        responses = stub.Echo(gen_request())

        for response in responses:
            print(response.val)

    except grpc.RpcError as e:
        status_code = e.code()
        print(e.details())
        print(status_code.name)


if __name__ == '__main__':
    run()
