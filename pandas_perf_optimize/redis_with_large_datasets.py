import numpy as np
import pandas as pd
import redis
import time
import pickle

# redis_client = redis.Redis(host='localhost', port=6379, socket_timeout=300)
# redis_client = redis.Redis(host='localhost', port=6379, db=0)
# redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

start_time = time.time()
df = pd.read_pickle(
    '/home/ec2-user/ird_mqr_saved_data_5046/get_smart_text_equity_bias_data.pkl')
print(df.head())
# get_category_id
# get_smart_text_equity_bias_data
total_time = time.time() - start_time
print('pickle file read time without cache')
print(total_time)

start_time = time.time()
# batch_size = 1000
# batches = [df[i:i+batch_size] for i in range(0, len(df), batch_size)]

# Store each batch as a separate key in Redis
# for i, batch in enumerate(batches):
#     key = f'get_smart_text_equity_bias_data_{i}'
#     value = pickle.dumps(batch)
#     redis_client.set(key, value)

# To retrieve a batch, use:
# key = 'batch_0'
# batch = pickle.loads(redis_client.get(key))

# retrieve all batch keys
keys = redis_client.keys('get_smart_text_equity_bias_data_*')
# retrieve and concatenate all batches into a single dataframe
dfs = []
for key in keys:
    data = pickle.loads(redis_client.get(key))
    dfs.append(data)
df = pd.concat(dfs)

# print the resulting dataframe
print(df.head())

total_time = time.time() - start_time
print('1' * 30)
print('pickle file read time after cache')
print(total_time)
