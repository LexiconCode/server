import grpc
from concurrent import futures

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
