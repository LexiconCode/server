import time
from services.state import State
from server import server


def serve():
    print('Starting server. Listening on port 50051.')
    State.serve()
    server.add_insecure_port('[::]:50051')
    server.start()

    _ONE_DAY_IN_SECONDS = 60 * 60 * 24
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)
