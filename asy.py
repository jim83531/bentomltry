import asyncio
import requests
import pandas as pd
import os
import time
from concurrent.futures import ThreadPoolExecutor
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "request.csv")
data = pd.read_csv(file_path, index_col=0)
# b = data.head(1).values.tolist()
loop = asyncio.get_event_loop()
executor = ThreadPoolExecutor(max_workers=2)
def req_post(b):
    print(b)
    t = time.time()
    print("Send a request at",t-start_time,"seconds.")
    response = requests.post("http://localhost:5000/predict", json=data[data.index==b].values.tolist())
    return response

async def foo(b):
#     print(b)
    res = await loop.run_in_executor(executor, req_post, b)
    t = time.time()
    print("Receive a response at",t-start_time,"seconds.")
    return res.json()

def got_result(future):
    print(future.result())

# async def hello_world():
tasks=[]
for i in range(10):
    task = loop.create_task(foo(i))
    task.add_done_callback(got_result)
    tasks.append(task)
start_time = time.time()
loop.run_until_complete(asyncio.wait(tasks))
