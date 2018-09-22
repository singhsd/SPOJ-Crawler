# SPOJ-Crawler
A python based crawler that downloads all sublissions made on [SPOJ](https://www.spoj.com).

## Key Features
- Simple interface
- Does not store passwords :innocent:
- Downloads **all** submissions, accepted or not. This helps in contemplation and review.
- Also creates a csv file that contains a list of:
  - Problem Name
  - Submission ID
  - Date of Submission
  - Status of Submission
  - Time Taken
  - Memory Consumed
  - Language Used
  - Complete Problem Link
- Does not store text files (.txt). Rather, this crawler stores files **according to language used**, i.e. C codes will be stored with ".c" extension, C++ codes with ".cpp", Java codes with ".java" and Python codes with ".py". Other codes will be stored as ".txt" but support for new languages can be added easily.

## Dependencies
The following packages need to be installed before running the crawler:
- BeautifulSoup
- getpass
- requests
- mechanize
- csv

## How to run
Follow these steps to successfully download your submissions from [SPOJ](https://www.spoj.com):
- Download this script
- In the directory where the script is present, make a cew directory with name "SPOJ_Codes" (without quotes)
- Install the required dependencies
- Use the command - "python -W ignore crawler.py" in the terminal (without quotes)
- Wait for a couple of minutes while SPOJ_Codes directory is getting filled with your submissions. A csv file named "information.csv" will also be created in the current folder that contains details about your submissions

**Note 1:** Only the most recent submissions are downloaded, since they are assumed to be the most recent and most optimized codes.

**Note 2:** My submissions on [SPOJ](https://www.spoj.com) can be found [here](https://github.com/singhsd/SPOJ-Codes). They were also downloaded using this crawler.
