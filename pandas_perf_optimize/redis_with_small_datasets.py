import redis
import pandas as pd
import pickle
import time

# Connect to Redis server
# r = redis.Redis(host='localhost', port=6379, db=0, ssl=True)
# r = redis.StrictRedis(host='localhost', port=6379, health_check_interval = 30, ssl = True)
r = redis.StrictRedis(host='localhost', port=6379, db=0)

# Read pickle file
start_time = time.time()
df = pd.read_pickle('/home/ec2-user/ird_mqr_saved_data_5046/get_model_explanation_data.pkl')
total_time = time.time() - start_time
print('pickle file read time before cache')
print(total_time)

# Convert DataFrame to bytes
data = pickle.dumps(df)

# Store in Redis cache
r.set('data_key', data)

# Retrieve data from Redis cache
start_time = time.time()
data = r.get('data_key')
total_time = time.time() - start_time
print('pickle file read time after cache')
print(total_time)
# Convert bytes to DataFrame
df = pickle.loads(data)
print(df.head())
