# Professor Assistant Program
# Version 1.0

import random
import os

print("Welcome to professor assistant version 1.0.")

# Ask professor name
professor_name = input("Please Enter Your Name: ")
print(f"Hello Professor {professor_name}, I am here to help you create exams from a question bank.\n")

while True:
    # Ask if professor wants to create an exam
    choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ").strip().lower()

    if choice == "no":
        print(f"Thank you Professor {professor_name}. Have a good day!")
        break

    elif choice == "yes":
        # Ask for path to question bank
        question_bank_path = input("Please Enter the Path to the Question Bank: ").strip()

        # Check if file exists
        if not os.path.exists(question_bank_path):
            print("The path you provided does not exist. Please try again.\n")
            continue
        else:
            print("Yes, indeed the path you provided includes questions and answers.")

        # Read questions and answers
        with open(question_bank_path, "r", encoding="utf-8") as file:
            lines = [line.strip() for line in file.readlines()]

        # Convert list into pairs (question, answer)
        question_pairs = []
        for i in range(0, len(lines), 2):
            if i + 1 < len(lines):        # Ensure answer exists
                question_pairs.append((lines[i], lines[i + 1]))

        # Ask how many questions for the exam
        try:
            num_questions = int(input("How many question-answer pairs do you want to include in your exam? "))
        except ValueError:
            print("Invalid number. Please try again.\n")
            continue

        if num_questions > len(question_pairs):
            print("Not enough questions in the question bank. Please try again.\n")
            continue

        # Ask where to save the exam
        output_path = input("Where do you want to save your exam? ").strip()

        # Select random questions
        selected = random.sample(question_pairs, num_questions)

        # Write selected questions to output file
        with open(output_path, "w", encoding="utf-8") as output_file:
            for q, a in selected:
                output_file.write(q + "\n")
                output_file.write(a + "\n\n")

        print(f"Congratulations Professor {professor_name}. Your exam is created and saved in {output_path}.\n")

    else:
        print("Invalid input. Please type Yes or No.\n")
