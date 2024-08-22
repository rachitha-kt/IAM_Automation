import csv
csv_file = 'deprovision_users.csv'

def deprovision_users():
    with open(csv_file,mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            username = row['username']
            print(f"De-provisioning user:{username}")

deprovision_users()