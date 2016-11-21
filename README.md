# Github repo for MAS.500 

## HW1: Getting started with Media Cloud

In this project, play around with the MediaCloud API and run different queries on media treatment of election.

### To Install:

* Download the Github repo
* From the HW1 project directory, run `pip install -r requirements.txt`
* Copy `hw1-11-17-16/settings.template` to `hw1-11-17-16/settings.ini` and add your Media Cloud API key in appropriate location

### To Run:

`python hw1.py`

## HW2: Adding logging, unit tests

In this project, build upon HW1 to add proper logging, unit tests, and command line inputs to the Media Cloud query.

### To Install:

* Download the Github repo
* From the HW2 project directory, run `pip install -r requirements.txt`
* Copy `hw2-11-22-16/settings.template` to `hw2-11-22-16/settings.ini` and add your Media Cloud API key, and desired query date range in the appropriate locations

### To Run:

* Media Query script: `python hw2-run-with-args.py <topic1> <topic2>`
* Unit tests: `python hw2-test.py`
* Logs can be found in `hw2.log`