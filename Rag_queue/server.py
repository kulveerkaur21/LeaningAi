from fastapi import FastAPI, Query
from client.rq_client import queue
from queues.worker import process_job
app = FastAPI()

@app.get("/")
def root():
   return {"status":"server is up an running"}

@app.post("/chat_queue")
def chat(query : str = Query(...,description="User query")):
    job = queue.enqueue(process_job, query)
    return {"status":"queued", "job_id": job.id}

@app.get("/result")
def get_result(job_id: str = Query(...,description="Job ID")):
    job = queue.fetch_job(job_id)
    if job.is_finished:
        return {"status":"finished", "result": job.result}
    elif job.is_failed:
        return {"status":"failed", "error": job.exc_info}
    else:
        return {"status":"pending"}
