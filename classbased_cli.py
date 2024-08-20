

ADMIN_INFO = "Admin_Credentials.txt"
QUIZ_QUESTIONS = "questions.txt"



class Admin:
    def __init__(self):
        self.username, self.password = self.set_credentials()

    def set_credentials(self):
        return 'Risav_pyakurel', 'Risav@123'

    def create_admin(self):
        with open(ADMIN_INFO, 'w') as file:
            file.write(f"admin_username: {self.username}\n")
            file.write(f"admin_password: {self.password}\n")

    def check_admin(self):
        try:
            with open(ADMIN_INFO, 'r') as file:
                lines = file.readlines()
                if len(lines) >= 2:
                    return True
        except FileNotFoundError:
            return False
        return False

    def check_admin_credentials(self):
        while True:
            username = input("Enter the username: ").strip()
            password = input("Enter the password: ").strip()

            with open(ADMIN_INFO, 'r') as file:
                lines = file.readlines()

                if len(lines) < 2:
                    print("Credentials file is not properly formatted.")
                    return False

                stored_username = lines[0].strip().split(':')[1].strip()
                stored_password = lines[1].strip().split(':')[1].strip()

                if (stored_username == username) and (stored_password == password):
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
            file.write(f"{Option_B}")
            Option_C = input("Enter a Option C: ")
            file.write(f"{Option_C}")
            Option_D = input("Enter a Option D: ")
            file.write(f"{Option_D}")

            answer = input("Enter a Correct answer: ").upper()
            print(" Question is added!!")

    def prepare_question(self):
        self.final_question_array = []

        question = ''
        answer = []
        correct_answer = ''

        with open(QUIZ_QUESTIONS, 'r') as file:
            for num, line in enumerate(file):
                line = line.strip()
                if (num + 1) % 6 == 1:
                    question = line
                elif 2 <= (num + 1) % 6 <= 5:
                    answer.append(line)
                elif (num + 1) % 6 == 0:
                    correct_answer = line
                    one_set = {'question': question, 'choices': answer, 'correct_answer': correct_answer}
                    self.final_question_array.append(one_set)
                    question = ''
                    answer = []
                    correct_answer = ''

    def show_questions(self):
        print(self.final_question_array[0].get('question'))
        print("Enter right answer:")
        print(self.final_question_array[0].get("choices")[0])
        print(self.final_question_array[0].get("choices")[1])
        print(self.final_question_array[0].get("choices")[2])
        print(self.final_question_array[0].get("choices")[3])
        answer = input("Enter right answer: ").upper()
        correct_answer_all = self.final_question_array[0].get("correct_answer")
        correct_answer = correct_answer_all.split()[1][0]
        if answer == correct_answer:
            print("Hurrah right answer")
        else:
            print("You are a loser")

class Quiz_App:

    def __init__(self):
        self.admin = Admin()
        self.questions = Questions()

    def login_option(self):
        print("Choose login mode as:\n")
        print("1. Admin Login\n")
        print("2. Continue as user\n")
        choice = int(input("Enter login choice: \n"))

        if choice == 1:
            if self.admin.check_admin_credentials():
                self.questions.add_questions()
        elif choice == 2:
            print("Welcome to quiz app!!!")
            self.questions.prepare_question()
            self.questions.show_questions()
        else:
            print("Invalid option!")

    def main(self):
        if not self.admin.check_admin():
            self.admin.create_admin()
        else:
            print("Admin already exists")

        self.login_option()

if __name__ == "__main__":
    app = Quiz_App()
    app.main()



