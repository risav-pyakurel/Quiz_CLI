ADMIN_INFO = "Admin_Credentials.txt"
QUIZ_QUESTIONS =  "questions.txt"


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
        print(stored_username)
        stored_password = lines[1].strip().split(":")[1]
        if (stored_username == username) and (stored_password == password):
            print("Welcome to the admin panel. Continue to add Questions")
            return True
        else:
            print("Please enter the correct credentials")
            return False

def read_questions():
    questions = []
    with open(QUIZ_QUESTIONS, 'r') as file:
        current_question = {}
        for line in file:
            line =  line.strip()
            if line.startswith("**") and line.endswith("**"):
                if current_question:
                    questions.append(current_question)
                current_question = {"question": line.strip("**")}
                current_question["options"] = []
            elif line.startswith("-"):
                current_question["options"].append(line[1:].strip())
            elif line.startswith("**Answer:**"):
                current_question["answer"] = line.split(":") [-1].strip()

    if current_question:
        questions.append(current_question)
    return questions

def quiz_game():
    questions = read_questions()
    print("Let's start the game!!!!")
    score = 0
    total_questions = len(questions)

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for option in q['options']:
            print(option)










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
        print("Welcome to the Quiz app!!!!!!!!")



def main():
    if not check_admin():
        Create_admin()
    else:
        print("Admin already exists")
    login_option()
    read_questions()
    quiz_game()


main()

