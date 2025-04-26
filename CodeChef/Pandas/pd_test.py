from ast import literal_eval
import pandas as pd
import string
import random
from datetime import datetime, timedelta
import json

test_df = pd.DataFrame({
    'job_id': pd.Series(dtype='str'),
    'pipe_id': pd.Series(dtype='int'),
    'tmstp': pd.Series(dtype='datetime64[ns]'),
    'rtype': pd.Series(dtype='str')
})

print(test_df.dtypes)

filt_df = pd.read_json('test.json')

print(filt_df)

Job = filt_df['job_id']
pipe = filt_df['pipe_id']
time = filt_df['tmstp']
rtype = filt_df.loc[0].at['entry'][0]['type']

print(f"Values grabbed from json file:\n{Job}\n{pipe}\n{time}\n{rtype}")
if 1 < 0:
    print("yes")
elif 1 > 0:
    print("No")
else:
    pass

format = "%Y-%m-%dT%H:%M:%S.%f%z"
start_time = "2025-03-25T15:37:57.000Z"
end_time = "2025-03-25T15:38:18.000Z"
diff_time = datetime.strptime(end_time, format) - datetime.strptime(start_time, format)

print(diff_time)

print(diff_time/timedelta(seconds=1))