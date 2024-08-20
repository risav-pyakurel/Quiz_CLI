ADMIN_INFO = "Admin_Credentials.txt"
QUIZ_QUESTIONS = "questions.txt"

class Admin():
    def __init__(self):
      self.username, self.password = self.set_credentials()

    def set_credentials(self):
        return 'Risav_pyakurel', 'Risav@123'


    def create_admin(self):
        with open(ADMIN_INFO,'w') as file:
            file.write(f"admin_username: {self.username} \n")
            file.write(f"admin_password: {self.password} \n")


    def check_admin(self):
        try:
            with open(ADMIN_INFO, 'r') as file:
                for line in file:
                    if line.startswith("admin : "):
                        return True

        except FileNotFoundError:
            return False

        return False

    def check_admin_credentials(self):
        while True:
            username = input ("Enter the username: ")
            password = input("Enter the password: ")

            with open(ADMIN_INFO, 'r') as file:
                lines =  file.readlines()

                stored_username = lines[0].strip().split(':')[1]
                stored_password = lines[1].strip().split(':')[1]
                if (stored_username == username)  and (stored_password == password):
                    print("Welcome to the admin panel. Continue to add Questions")
                    return True
                else:
                    print("Please enter the correct credentials!!!")










