from redis import Redis
from rq import Queue, Retry, Connection
from rq.worker import Worker

import config

listen = [config.QUEUE_NAME]
redis_conn = Redis.from_url(config.REDIS_URL)

if __name__ == "__main__":
    with Connection(redis_conn):
        worker = Worker(map(Queue, listen), name=config.WORKER_NAME)
        worker.work(with_scheduler=True)
        