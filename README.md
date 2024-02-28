# GlitchClassification

This project's goal is to classify glitches found in Virgo gravitational wave data. Utilizing advanced data processing and machine learning techniques, it aims to enhance the accuracy and efficiency of gravitational wave data analysis.

## Contents

The repository is organized in two folders for useful **scripts** and demos **notebooks**. The **notebook** folder contains:

- **run_wdf_worker**: This notebook contains a step-by-step guide to run the WDF worker with multiprocessing.

- **wdf_demo**: Here, you will find a demonstration of WDF's capabilities, with detailed instructions on carrying out downsampling, whitening and wavelet transform for event trigger production.

The **scripts** folder contains scripts to load a sample segment list for analysis. Other files in the repo are:

- **.gitignore**: This file lists directories and files that are intentionally untracked by Git to prevent them from being included in the repository.

- **Dec23_ER-DQstudies_seg.csv**: CSV file with a list of Advanced Virgo interferometer segment times. 

## Installation & Requirements

You can clone the repository to your local machine. However, you will have to install the WDF library in your environment. To do this visit the [WDF project page](https://gitlab.com/wdfpipe/wdf/-/tree/master?ref_type=heads) and follow the installation instructions provided there.

## Usage

Refer to the notebook directory and its content (`run_wdf_worker` and `wdf_demo`) for guided instructions on running WDF.
 
## Contributing

Contributions to the GlitchClassification project are welcome. If you have suggestions for improvements or new features, please review the contribution guidelines.
