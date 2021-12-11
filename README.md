# Internship-Opportunity-Web-Scraper
This is a webscraper I wrote for my CAS project which searches three websites to provide relavant internship and scholarhsip information for highschool students. The script used for scraping indeed.com is wrote by @[vdhar1992](https://github.com/vdhar1992/Web_Scraper), all credits goes to her for this part of the code. 

## How to Use It
If you're not into code and doesn't want to run it on your local environment or look at the raw code, simply clone this repo or download the main.exe and run it. You will likely receive four files inside the folder where the exe file is located. If the file doesn't run, try removing the suffix .exe and run again.

If you want to run these code on your local environment follow the following steps:
1. Clone this repository
2. cd into the directory
3. Run the following command in the terminal with anaconda installed
```bash
conda env create -f environment.yml
```
4. Activate the conda virtual environment using the following command
```bash
conda activate webscraper
```
6. Run the main.py script with this virtual environment, all the scripts are contained.

##Potential Issues
If you run this script several times, the webiste might start using human reCaptchas and I did NOT design any plan for that, so if that doesn't work  ¯\_(ツ)_/¯
