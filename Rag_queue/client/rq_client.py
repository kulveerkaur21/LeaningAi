from redis import Redis
from rq import Queue,SimpleWorker

redis_conn = Redis(host="localhost", port=6379)
queue = Queue("default", connection=redis_conn)

print("Worker started...")

worker = SimpleWorker([queue], connection=redis_conn)
worker.work()