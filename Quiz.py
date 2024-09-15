import requests
import random
import html


def fetch_questions(amount=5, difficulty="easy"):
    # Fetch questions from the Open Trivia Database API
    url = f"https://opentdb.com/api.php?amount={amount}&difficulty={difficulty}&type=multiple"
    response = requests.get(url)
    data = response.json()

    # Return the list of questions
    return data['results']


def ask_question(question_data):
    # Decode HTML entities in the question and choices
    question = html.unescape(question_data['question'])
    correct_answer = html.unescape(question_data['correct_answer'])
    incorrect_answers = [html.unescape(ans) for ans in question_data['incorrect_answers']]

    # Prepare multiple choice options (shuffle the correct answer among incorrect ones)
    choices = incorrect_answers + [correct_answer]
    random.shuffle(choices)

    # Ask the question
    print(f"\nQuestion: {question}")

    # Display choices
    for idx, choice in enumerate(choices, 1):
        print(f"{idx}. {choice}")

    # Get user's answer
    while True:
        try:
            user_answer = int(input("Choose the correct answer (1-4): "))
            if 1 <= user_answer <= 4:
                break
            else:
                print("Please enter a valid option between 1 and 4.")
        except ValueError:
            print("Please enter a number.")

    # Check if the answer is correct
    if choices[user_answer - 1] == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Wrong! The correct answer was: {correct_answer}\n")
        return False


def start_quiz():
    print("Welcome to the Python Quiz!")
    score = 0
    questions = fetch_questions(amount=5, difficulty="medium")  # Fetch 5 questions

    # Ask each question
    for question_data in questions:
        if ask_question(question_data):
            score += 1

    # Display final score
    print(f"Quiz Completed! Your final score: {score}/{len(questions)}")


# Run the quiz
if __name__ == "__main__":
    start_quiz()
