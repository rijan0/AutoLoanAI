def read_data_from_file(file_name):
    users = []
    with open(file_name, 'r') as file:
        current_user = {}
        for line in file:
            line = line.strip()
            if line.startswith("User"):
                if current_user:
                    users.append(current_user)
                current_user = {}
            elif line:
                key, value = line.split(": ")
                if key == "Land Number":
                    current_user[key] = int(value)
                elif key == "Annual Income" or key == "Rate per Dhur" or key == "Total Area in Dhur":
                    current_user[key] = float(value)
                else:
                    current_user[key] = value
        if current_user:
            users.append(current_user)
    return users

def decide_loan_approval(users, loan_amount, land_number, pan_number):
    for user in users:
        if user["Land Number"] == land_number and user["PAN Number"] == pan_number:
            main_value = user["Total Area in Dhur"] * user["Rate per Dhur"]
            max_loan_amount = 0.6 * main_value  # 60% of main value
            if user["Tax Payment Status"] == "paid" and user["Income Tax Payment Status"] == "paid":
                if loan_amount <= max_loan_amount:
                    return True
                else:
                    return False
            else:
                return False
    return False

def main():
    # Read data from file
    file_name = 'data.txt'  # Adjust this if your file is named differently
    users = read_data_from_file(file_name)
    
    # Accept user input
    loan_amount = float(input("Enter the loan amount you want to apply for: "))
    land_number = int(input("Enter your land number: "))
    pan_number = input("Enter your PAN number: ")
    
    # Make loan decision
    if decide_loan_approval(users, loan_amount, land_number, pan_number):
        print("Congratulations! Your loan is approved.")
    else:
        print("Sorry, your loan application is rejected.")

if __name__ == "__main__":
    main()
