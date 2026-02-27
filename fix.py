import os
import random
from datetime import datetime, timedelta

# 1 जनवरी 2025 से आज तक
start_date = datetime(2025, 1, 1)
end_date = datetime.now()
days_count = (end_date - start_date).days

for i in range(days_count + 1):
    current_date = (start_date + timedelta(days=i)).strftime('%Y-%m-%d 12:00:00')
    
    # रैंडम तरीके से तय करना कि उस दिन कितने कमिट करने हैं
    # 0 = कोई काम नहीं, 1-3 = हल्का हरा, 10-15 = गहरा हरा
    commit_count = random.choice([0, 1, 2, 3, 8, 12, 15]) 
    
    for j in range(commit_count):
        with open('natural_log.txt', 'a') as f:
            f.write(f'Work on {current_date} commit {j}\n')
        
        # Windows CMD के लिए तारीख सेट करके कमिट करना
        os.system(f'git add natural_log.txt')
        os.system(f'set GIT_AUTHOR_DATE={current_date} && set GIT_COMMITTER_DATE={current_date} && git commit -m "Fixed issue #{random.randint(100, 999)}"')

print("Ab aapka 2025 ka graph ekdam REAL aur NATURAL dikhega!")
