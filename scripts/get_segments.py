import pandas as pd
import os
#import subprocess
from .get_git_repo_root import get_git_repo_root

git_parent_directory = get_git_repo_root()

# File path for the CSV file
file_path = os.path.join(git_parent_directory,'Dec23_ER-DQstudies_seg.csv')

# Reading the CSV file
df = pd.read_csv(file_path)

# Extracting 'start' and 'end' columns into lists
start = df['start'].tolist()
end = df['end'].tolist()

# Displaying the first few elements of each list as a check
print(start[:5]) 
print(end[:5])
