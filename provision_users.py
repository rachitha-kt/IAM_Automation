import csv
csv_file = 'users.csv'

roles = {
    "IT":"Admin",
    "HR":"User",
    "Finance":"FinanceUser"
}

def provision_users():
    with open(csv_file,mode='r') as file:
        csv_reader= csv.DictReader(file)
        for row in csv_reader:
            username = row['username']
            email =row['email']
            department = row['department']
            role=roles.get(department,"User")
            print(f"Provisioning user: {username},Role:{role}")

provision_users()