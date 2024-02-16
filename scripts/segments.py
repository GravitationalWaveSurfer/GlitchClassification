import pandas as pd
import os
#import subprocess
import get_git_repo_root

def get_list(verbose=False, tmin=1387468818, tmax=1387612818):
    """
    Reads a CSV file containing segment data, extracts 'start' and 'end' times, and returns a combined list of [start, end]
    pairs. This function locates a specific CSV file within a Git repository's root directory, reads the file to extract 'start'
    and 'end' columns, and combines these into a list of [start, end] pairs. Optionally, it can print the first five [start,end]
    pairs for verification.

    Parameters:
    - verbose (bool): If True, prints the first five [start, end] pairs for verification. Default is False.
    - tmin (int): The minimum timestamp for filtering segments. This parameter is currently not used in the function.
    - tmax (int): The maximum timestamp for filtering segments. This parameter is currently not used in the function.

    Returns:
    - combined (list of lists): A list of [start, end] pairs extracted from the CSV file.
    """
    git_parent_directory = get_git_repo_root.repo_root()
  #  print(git_parent_directory)
    # File path for the CSV file
    file_path = os.path.join(git_parent_directory,'Dec23_ER-DQstudies_seg.csv')

    # Reading the CSV file
    df = pd.read_csv(file_path)

    # Extracting 'start' and 'end' columns into lists
    start = df['start'].tolist()
    end = df['end'].tolist()
    
    combined = [[start[i], end[i]] for i in range(len(start)) if start[i] > tmin and end[i] < tmax]
    # Displaying the first few elements of each list as a check
    if verbose==True:
        print('First and last five segments from the .csv file:')
        print(start[:5]) 
        print(end[:5])
    
    return combined
