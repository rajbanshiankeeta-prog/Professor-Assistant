Professor Assistant

The Professor Assistant is a Python-based tool designed to help professors automatically create exams or quizzes from a question bank. The program loads a file containing question–answer pairs, randomly selects a specified number of questions, and saves them into an exam file chosen by the professor.

📌 Features

Greets the professor and collects their name

Loads a question bank file (Q&A format: question → next line answer)

Randomly selects any number of question–answer pairs

Saves the generated exam to a text file

Allows creation of multiple exams in one run

Simple, user-friendly command-line interface

📁 Project Structure
├── question_bank.txt      # Question bank (Q&A format)
├── professor_assistant.py # Main program
└── README.md              # Documentation

🧠 How It Works

Program starts and greets the professor

Professor enters their name

System asks if they want to create an exam

If yes:

Provide path to question bank

Enter number of questions

Enter output file name

Program randomly selects questions using random.randint()

Exam file is created and saved

Professor may create another exam or quit

📌 Question Bank Format

Your question_bank.txt must follow this structure:

Question 1?
Answer 1
Question 2?
Answer 2
...


Each question is followed immediately by its answer on the next line.

▶️ Running the Program

Make sure you have Python 3 installed.

Run the script using:

python professor_assistant.py


Follow the on-screen instructions.

🔧 Requirements

Python 3.x

Standard Library only (no external packages)

📝 Example Interaction
Welcome to professor assistant version 1.0.
Please Enter Your Name: Ibrahim Musa
Hello Professor Ibrahim Musa, I am here to help you create exams.
Do you want me to help you create an exam (Yes | No)? Yes
Please enter the path to the question bank: question_bank.txt
How many questions do you want? 20
Where do you want to save your exam? midterm.txt
Your exam has been created and saved in midterm.txt.
Create another exam (Yes | No)? No
Thank you Professor Ibrahim Musa. Have a good day!

💡 Future Improvements (Optional)

Add GUI interface

Allow topic-based filtering

Save exam with numbering and formatting

