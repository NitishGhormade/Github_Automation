import os
import subprocess
from datetime import datetime, timedelta

num = 0

def git_commit_and_push(repo_path, start_date, days, commits_per_day, commit_message):
    global num
    
    os.chdir(repo_path)
    
    for day in range(days):
        commit_date = (start_date + timedelta(days=day)).strftime("%Y-%m-%dT12:00:00")
        
        for _ in range(commits_per_day):
            # Make changes to the file
            with open("my_number.txt", "w") as f:
                f.write(str(num))
                num += 1

            # Add all changes
            subprocess.run(["git", "add", "--all"], check=True)
            
            # Set the environment variables for backdating
            env = os.environ.copy()
            env["GIT_AUTHOR_DATE"] = commit_date
            env["GIT_COMMITTER_DATE"] = commit_date
            
            # Commit changes
            subprocess.run(["git", "commit", "-m", f"{commit_message}"], check=True, env=env)
        
            # Push changes after each day's commits
            subprocess.run(["git", "push"], check=True)

if __name__ == "__main__":
    repo_path = "C:\\Users\\nitis\\OneDrive\\Desktop\\Github_Automation"  # Change this to your repository path
    start_date = datetime(2024, 6, 25)  # Start date for commits in (YYYY, MM, DD)
    days = (datetime.today() - start_date).days + 1  # Number of days till today
    commits_per_day = 5  # Number of commits per day
    commit_message = "It's a commit, for being productive"  # Change this if needed
    
    git_commit_and_push(repo_path, start_date, days, commits_per_day, commit_message)
    print("Backdated commits pushed successfully!")