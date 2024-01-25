import pandas as pd
import os
#import subprocess
import get_git_repo_root

def get_list(verbose=False):
    git_parent_directory = get_git_repo_root.repo_root()
    print(git_parent_directory)
    # File path for the CSV file
    file_path = os.path.join(git_parent_directory,'Dec23_ER-DQstudies_seg.csv')

    # Reading the CSV file
    df = pd.read_csv(file_path)

    # Extracting 'start' and 'end' columns into lists
    start = df['start'].tolist()
    end = df['end'].tolist()
    
    combined = [[start[i], end[i]] for i in range(len(start))]
    # Displaying the first few elements of each list as a check
    if verbose==True:
        print('First and last five segments from the .csv file:')
        print(start[:5]) 
        print(end[:5])
    
    return combined
