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
            stored_password = lines[1].strip().split(":")[1]
            if (stored_username == username) and (stored_password == password):
                print("Welcome to the admin panel. Continue to add Questions")
                return True
            else:
                print("Please enter the correct credentials")

def add_questions():
    with open(QUIZ_QUESTIONS,'a') as file:
        question = input("Enter the question: ")
        file.write(f"{question}")
        Option_A = input("Enter a Option A: ")
        file.write(f"A) {Option_A} ")
        Option_B = input("Enter a Option B: ")
        file.write(f" B) {Option_B}")
        Option_C = input("Enter a Option C: ")
        file.write(f" C) {Option_C}")
        Option_D = input("Enter a Option D: ")
        file.write(f" D) {Option_D}")

        answer = input("Enter the correct answer: ").upper()
        print("Question is added!!")



# def quiz_game():
#     print("Let's start the game!")
#     with open(QUIZ_QUESTIONS, 'r') as file:
#         lines = file.readline()
#         score = 0
#         question_num = 0



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


    else:
        print("Invalid choice of option! You don't  deserve to play this game!!!!!")


def prepare_question():
    final_question_array=[]
    question =''
    answer = []
    correct_answer= ''
    with open(QUIZ_QUESTIONS, 'r') as file:
        for num,line in enumerate(file):
            if (num+1)%6==1:
                question=line
            elif (num+1)%6>=2 and (num+1)%6<=5:
                answer.append(line)
            elif(num+1)%6 ==0:
                correct_answer = line
                one_set={'question':question,"choices":answer,"correct_answer":correct_answer}
                final_question_array.append(one_set)
                question=''
                answer=[]
                correct_answer=''

def main():
    if not check_admin():
        Create_admin()
    else:
        print("Admin already exists")
    login_option()
    prepare_question()




main()


