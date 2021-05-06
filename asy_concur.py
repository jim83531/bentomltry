import requests
import pandas as pd
import os
import time
import concurrent
from concurrent.futures import ThreadPoolExecutor

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "request.csv")
data = pd.read_csv(file_path, index_col=0)
data_j = data.values.tolist()
with ThreadPoolExecutor(max_workers=5) as executor:
    start_time=time.time()
    futures = []
    for i in range(len(data_j)):
#         t = time.time()
#         print("Send a request at",t-start_time,"seconds.")
        futures.append(executor.submit(requests.post, url="http://localhost:5000/predict", json = [data_j[i]]))
#         t = time.time()
#         print("Receive a request at",t-start_time,"seconds.")
    for future in concurrent.futures.as_completed(futures):
        print(future.exception())
