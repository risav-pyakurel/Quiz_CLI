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


class Questions:

    def add_questions(self):
        with open(QUIZ_QUESTIONS, 'a') as file:
            question = input("Enter the question: ")
            file.write(f" {question}")
            Option_A = input("Enter a Option A: ")
            file.write(f" A) {Option_A}")
            Option_B = input("Enter a Option B: ")
            file.write (f"{Option_B}")
            Option_C = input("Enter a Option C: ")
            file.write(f"{Option_C}")
            Option_D = input("Enter a Option D: ")
            file.write(f"{Option_D}")

            answer = input("Enter a Correct answer: ").upper()
            print(" Question is added!!")

    def login_option(self):
        print("Choose login mode as: \n")
        print("1. Admin Login \n")
        print("2. Continue as user \n")
        choice = int(input("Enter login choice: \n"))

        if choice == 1:
            if self.check_admin_credentials():
                self.add_questions()

        elif choice ==2:
            print("Welcome to quiz app!!!")

        else:
            print("Invalid option!")

















