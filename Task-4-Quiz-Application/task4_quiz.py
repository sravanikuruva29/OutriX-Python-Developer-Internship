"""
OutriX Python Developer Internship - Task 4
Quiz Application with Score Tracker
Tools: Python, random, json

Run:
    python task4_quiz.py

The program stores questions in a JSON file automatically on first run,
randomizes the questions, accepts answers, and tracks the final score.
"""

import json
import os
import random


QUESTION_FILE = "quiz_questions.json"

DEFAULT_QUESTIONS = [
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. float"],
        "answer": "C"
    },
    {
        "question": "Which symbol is used for a comment in Python?",
        "options": ["A. //", "B. <!-- -->", "C. #", "D. **"],
        "answer": "C"
    },
    {
        "question": "Which loop is commonly used to iterate over a sequence?",
        "options": ["A. for", "B. switch", "C. repeat", "D. select"],
        "answer": "A"
    },
    {
        "question": "Which method adds an item to the end of a list?",
        "options": ["A. add()", "B. append()", "C. insertEnd()", "D. push()"],
        "answer": "B"
    },
    {
        "question": "What does len() return?",
        "options": [
            "A. The data type",
            "B. The largest value",
            "C. The number of items",
            "D. The memory address"
        ],
        "answer": "C"
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ^", "B. //", "C. **", "D. ^^"],
        "answer": "C"
    },
    {
        "question": "Which collection stores key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "What is the output of 10 // 3?",
        "options": ["A. 3", "B. 3.33", "C. 1", "D. 4"],
        "answer": "A"
    },
    {
        "question": "Which function is used to get input from the user?",
        "options": ["A. scan()", "B. read()", "C. input()", "D. get()"],
        "answer": "C"
    }
]


def create_question_file():
    if not os.path.exists(QUESTION_FILE):
        with open(QUESTION_FILE, "w", encoding="utf-8") as file:
            json.dump(DEFAULT_QUESTIONS, file, indent=4)


def load_questions():
    try:
        with open(QUESTION_FILE, "r", encoding="utf-8") as file:
            questions = json.load(file)

        if not questions:
            raise ValueError("Question file is empty.")

        return questions

    except (FileNotFoundError, json.JSONDecodeError, ValueError):
        with open(QUESTION_FILE, "w", encoding="utf-8") as file:
            json.dump(DEFAULT_QUESTIONS, file, indent=4)

        return DEFAULT_QUESTIONS


def get_answer():
    while True:
        answer = input("Your answer (A/B/C/D): ").strip().upper()

        if answer in {"A", "B", "C", "D"}:
            return answer

        print("Invalid choice. Please enter A, B, C, or D.")


def run_quiz():
    questions = load_questions()
    random.shuffle(questions)

    try:
        total_questions = int(input(
            f"How many questions do you want? (1-{len(questions)}): "
        ))

        if not 1 <= total_questions <= len(questions):
            raise ValueError

    except ValueError:
        print("Invalid number. Using 5 questions.")
        total_questions = min(5, len(questions))

    selected_questions = questions[:total_questions]
    score = 0

    print("\n" + "=" * 55)
    print("              OUTRIX PYTHON QUIZ")
    print("=" * 55)

    for number, item in enumerate(selected_questions, start=1):
        print(f"\nQuestion {number}: {item['question']}")

        for option in item["options"]:
            print(option)

        user_answer = get_answer()

        if user_answer == item["answer"]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! Correct answer: {item['answer']}")

    percentage = (score / total_questions) * 100

    print("\n" + "=" * 55)
    print("                 QUIZ RESULT")
    print("=" * 55)
    print(f"Score      : {score}/{total_questions}")
    print(f"Percentage : {percentage:.2f}%")

    if percentage >= 80:
        print("Performance: Excellent!")
    elif percentage >= 60:
        print("Performance: Good!")
    elif percentage >= 40:
        print("Performance: Needs Improvement")
    else:
        print("Performance: Keep Practicing!")

    print("=" * 55)


if __name__ == "__main__":
    create_question_file()
    run_quiz()
