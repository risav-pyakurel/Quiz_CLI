ADMIN_INFO = "Admin_Credentials.txt"


def Set_Credentials():
    static_username = 'Risav_pyakurel'
    static_password = "Risav@123"
    return static_username, static_password


def Create_admin():
    static_username, static_password = Set_Credentials()
    with open(ADMIN_INFO, 'w') as file:
        file.write(f" admin_username:{static_username} \n")
        file.write(f"admin_password:{static_password}\n")





def check_admin():
    try:
        with open(ADMIN_INFO, 'r') as file:
            for line in file:
                if line.startswith("admin: "):
                    return True
    except FileNotFoundError:
        return False
    return False

def check_admin_credentials(username, password):

    with open(ADMIN_INFO, 'r') as file:

        lines = file.readlines()
        stored_username = lines[0].strip().split(":")[1]
        stored_password = lines[1].strip().split(":")[1]
        if (stored_username == username) and (stored_password == password):
            print("Welcome to the admin panel")
        else:
            print("Please enter the correct credentials")



def login_option():
    print("Choose login mode as: \n")
    print("1. Admin login\n")
    print("2. continue as user \n")
    choice = int(input("Enter login choice: \n"))

    if choice == 1:
        username = input("Enter the username: \n")
        password = input("Enter the password : \n")
        check_admin_credentials(username,password)

    elif choice == 2:
        pass



def main():
    if not check_admin():
        Create_admin()
    else:
        print("Admin already exists")
    login_option()

main()

