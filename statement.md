# PROBLEM STATEMENT:

Students and general users often need a simple and engaging way to test and improve their general knowledge across different subjects. Traditional quizzes may use fixed question sequences, require manual checking of answers, or provide results only after the entire quiz has been evaluated. These extra steps can make the process less interactive and reduce the usefulness of a quick self-assessment activity. This project solves this problem by providing an easy-to-use command line Quiz Bowl application that randomly selects multiple-choice questions, accepts user answers, provides immediate feedback, and automatically calculates the final score and percentage with minimal setup.

# OBJECTIVES:

Design the program around a single Python function that manages the complete quiz process, from selecting questions to displaying the final result.

Create a structured question pool using Python dictionaries containing questions, four multiple-choice options, and the corresponding correct answer.

Randomly select a limited number of questions from the available question pool so that each quiz session can provide a different combination of questions.

Provide simple and clear multiple-choice interaction where users can select answers using the options A, B, C, or D.

Validate and normalize user input by removing unnecessary spaces and converting answers to uppercase before checking them.

Give immediate feedback after every question by displaying whether the selected answer is correct and showing the correct answer when the response is incorrect.

Automatically calculate the user's total score and percentage at the end of the quiz and display the final result clearly.

Use exception handling to safely manage unexpected input or runtime errors and allow the quiz to continue without abruptly terminating.

# SCOPE OF THE PROJECT:

## Functional Scope

**Randomized quiz sessions:** The program randomly selects up to 10 questions from the available question pool for each quiz session, ensuring that the questions are not simply presented in a fixed order.

**Multiple-choice questions:** Each question contains four answer choices represented by A, B, C, and D, allowing the user to select one answer through the command line.

**Wide range of general knowledge:** The question pool contains questions from different areas such as science, history, geography, mathematics, technology, sports, literature, and general knowledge.

**Structured question management:** Questions are stored as dictionaries containing the question text, a list of four options, and the correct answer, making the question pool easy to organize and expand.

**Input validation and normalization:** User answers are processed using `strip()` and `upper()` so that inputs such as lowercase letters or answers with extra spaces can still be checked consistently.

**Immediate answer feedback:** After every question, the program informs the user whether the answer is correct. If the answer is wrong, the correct option is displayed.

**Automatic scoring:** The program increases the score for every correct answer and displays the final score in the format of the number of correct answers out of the total questions attempted.

**Percentage calculation:** At the end of the quiz, the program calculates the user's percentage using the final score and total number of questions and displays it up to two decimal places.

**Error handling:** Invalid answer choices are identified and unexpected exceptions are caught so that the program can move to the next question instead of stopping unexpectedly.

## Non-functional Scope:

**Fast execution:** The quiz runs locally through the command line and requires only normal Python execution, allowing questions, answers, and results to be processed immediately.

**No external dependencies:** The program uses Python's built-in `random` module for selecting questions and does not require external libraries or online services.

**Simple and intuitive:** The command-line interface uses clear prompts, numbered questions, and A–D options, making it easy for students and beginner Python users to understand.

**Maintainable question structure:** The dictionary-based question format allows additional questions to be added to the existing question pool using the same structure without changing the main quiz logic.

**Reliable result calculation:** Scores and percentages are calculated automatically by the program, reducing the possibility of manual calculation errors.

# Target Audience:

**School and college students** who want to practice general knowledge and test their understanding through a quick interactive quiz.

**Python beginners and programming students** who want to study a practical example of lists, dictionaries, loops, functions, conditional statements, input validation, exception handling, and the `random` module.

**Teachers and instructors** who can use the application as a simple command-line quiz activity or as a foundation for a larger educational quiz system.

**Casual quiz users** who want to test their general knowledge through a short, randomized multiple-choice quiz without requiring a web browser or additional
