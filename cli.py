ADMIN_INFO = "Admin_Credentials.txt"
QUIZ_QUESTIONS = "questions.txt"


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


def check_admin_credentials():
    while True:
        username = input("Enter the Username: ")
        password = input("Enter the password: ")
        with open(ADMIN_INFO, 'r') as file:
            lines = file.readlines()
            stored_username = lines[0].strip().split(":")[1]
            print(stored_username)
            stored_password = lines[1].strip().split(":")[1]
            if (stored_username == username) and (stored_password == password):
                print("Welcome to the admin panel. Continue to add Questions")
                return True
            else:
                print("Please enter the correct credentials")

def add_questions():
    with open(QUIZ_QUESTIONS,'a') as file:
        question = input("Enter the question: ")
        file.write(f"{question}\ n")
        Option_A = input("Enter a Option A: ")
        file.write(f"A) {Option_A} \n ")
        Option_B = input("Enter a Option B: ")
        file.write(f" B) {Option_B} \n")
        Option_C = input("Enter a Option C: ")
        file.write(f" C) {Option_C} \n")
        Option_D = input("Enter a Option D: ")
        file.write(f" D) {Option_D} \n")

        answer = input("Enter the correct answer: ").upper()
        print("Question is added!!")



def quiz_game():
    print("Let's start the game!")
    with open(QUIZ_QUESTIONS, 'r') as file:
        lines = file.readline()
        score = 0
        question_num = 0
    for i in range(0 , len(lines), 6):
        question_num +=1
        print(f"\n Question {question_num}: {lines[i].strip()} ")
        print(lines[i+1].strip())
        print(lines[i+2].strip())
        print(lines[i+3].strip())
        print(lines[i+4].strip())

        user_answer = input("Choose the correct Option: ").upper()
        correct_answer= lines[i+5].strip().split(": ")[1]

        if user_answer == correct_answer:
            print("Your answer is correct! ")
            score +=1

        else:
            print(f"Your given answer is incorrect. The correct answer {correct_answer}!!")

    print(f" Quiz game is completed!!, You Scored: {score}/{question_num}")


def login_option():
    print("Choose login mode as: \n")
    print("1. Admin login\n")
    print("2. continue as user \n")
    choice = int(input("Enter login choice: \n"))

    if choice == 1:
        if check_admin_credentials():
            add_questions()
    elif choice == 2:
        print("Welcome to the Quiz app!!!!!!!!")
        quiz_game()

    else:
        print("Invalid choice of option! You don't  deserve to play this!!!!!")


def main():
    if not check_admin():
        Create_admin()
    else:
        print("Admin already exists")
    login_option()



main()
