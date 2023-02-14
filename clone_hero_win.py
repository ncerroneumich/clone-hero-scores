import subprocess
import os
import time

# Set the program path
program = "D:\\Program Files\\Clone Hero 2\\Clone Hero.exe"

# Set the file path
file_path = "C:\\Users\\Nicko\\AppData\\LocalLow\\srylain Inc_\\Clone Hero\\scoredata.bin"

# Set the repository URL
repo_url = "https://github.com/ncerroneumich/clone-hero-scores.git"

# Set the local folder
local_folder = "D:\\Program Files\\Clone Hero 2\\clone-hero-scores"

# Pull the latest version of the repository
os.chdir(local_folder)
pull_command = "git pull " + repo_url
subprocess.run(pull_command, shell=True)

# Launch the program
p = subprocess.Popen(program)

# Wait for the program to close
while p.poll() is None:
    time.sleep(1)

# Copy the file from the source folder to the local folder
copy_command = "copy " + file_path + " " + local_folder
subprocess.run(copy_command, shell=True)

# Push the file to the repository
os.chdir(local_folder)
push_command = "git add ."
subprocess.run(push_command, shell=True)

# Get the current time and format it
current_time = time.strftime("%Y-%m-%d %H:%M:%S")
commit_message = "Update scores from windows at " + current_time

# Commit and push the changes
commit_command = "git commit -m \"" + commit_message + "\""
subprocess.run(commit_command, shell=True)
push_command = "git push -f " + repo_url
subprocess.run(push_command, shell=True)