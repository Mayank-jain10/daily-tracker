import pandas as pd
from datetime import datetime
import os

file_name = 'daily_records.csv'

# नया डेटा बनाना
today_data = {
    'Date': [datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
    'Status': ['Success']
}
new_df = pd.DataFrame(today_data)

# फ़ाइल अपडेट करना
if not os.path.isfile(file_name):
    new_df.to_csv(file_name, index=False)
else:
    new_df.to_csv(file_name, mode='a', header=False, index=False)

print("Daily Record Added Successfully!")
