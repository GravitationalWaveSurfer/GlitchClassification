import subprocess
import os

def get_git_repo_root():
    try:
        # This command returns the root directory of the current git repository
        return subprocess.check_output(["git", "rev-parse", "--show-toplevel"]).decode('utf-8').strip()
    except subprocess.CalledProcessError:
        # Handle the case where the current directory is not a git repository
        return None