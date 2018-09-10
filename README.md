# Feeling Analyzer
This project is a system that scans the content shared by Iranian users in different social networks and analyzes the overall rate of satisfaction of life and happiness of people in Iran, finds out the reasons of those feelings, and shows them in well-detailed charts. Feeling analyzer gets updated in every hour.

## How does it work?
This program is consisted of 3 main parts:
1) Data collector
2) Data analyzer
3) Status updater

### Data Collector
Data collector is a crone job that:
1) Scans users list every day.
2) Recieves the lastest tweets each hour of the day.

#### Prepare the crone job:
After cloning the project, make sure to make a file named "credentials.txt" in "Data" folder and fill in **consumer key**, **consumer secret**, **access key**, and **access secret** in the mentioned order.
#### Run main.py
After the credentials file was configured, just open up the terminal in project's directory and either run the crone job with the following command:
```
# this is a test code
```
