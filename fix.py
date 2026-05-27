import os
import subprocess
from datetime import datetime, timedelta

START_DATE = datetime(2026, 2, 27)
END_DATE = datetime(2026, 3, 10)
COMMITS_PER_DAY = 18
LOG_FILE = "recent_log.txt"

# Windows पर Git का डिफ़ॉल्ट एब्सोल्यूट पाथ
GIT_PATH = r"C:\Program Files\Git\cmd\git.exe"

def run_backfill():
    total_days = (END_DATE - START_DATE).days
    env = os.environ.copy()

    # अगर डिफ़ॉल्ट पाथ पर गिट न मिले, तो लोकल एनवायरनमेंट से ढूंढने की कोशिश करें
    git_cmd = GIT_PATH if os.path.exists(GIT_PATH) else "git"

    for i in range(total_days + 1):
        current_date = START_DATE + timedelta(days=i)
        commit_date = f"{current_date.strftime('%Y-%m-%d')} 12:00:00"

        env["GIT_AUTHOR_DATE"] = commit_date
        env["GIT_COMMITTER_DATE"] = commit_date

        for j in range(COMMITS_PER_DAY):
            with open(LOG_FILE, "a") as f:
                f.write(f"work {commit_date} {j}\n")

            # डायरेक्ट गिट पाथ का उपयोग करके ऐड करें
            subprocess.run([git_cmd, "add", LOG_FILE], env=env, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            commit_message = f"chore: update log {current_date.strftime('%Y-%m-%d')} {j}"
            # डायरेक्ट गिट पाथ का उपयोग करके कमिट करें
            subprocess.run(
                [git_cmd, "commit", "-m", commit_message],
                env=env,
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

    print("done")

if __name__ == "__main__":
    run_backfill()
