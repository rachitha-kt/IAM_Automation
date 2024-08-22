IAM Automation Project

##Overview
This project automates user provisioning and de-provisioning in an Active directory

##Scripts

-`provision_users.py`: Provision users based on a CSV input file. It also assigns roles based on department.
-`deprovision_users.py`: Deprovision users based on a CSV input file.

##Setup

1. Install Python
2. Install dependencies(optionsl - in case of AD)
3. Running the scripts:
	a. to provision users : python3 provision_users.py
	b. to deprovision users: python3 deprovision_users.py
4. Create the csv file: 
	a. to create users.csv: nano users.csv
	b. to create deprovision.csv: nano deprovision.csv

##Project structure
