# Quiz Bowl

## Overview of the Project:

The **Quiz Bowl** is a lightweight, interactive general knowledge quiz application developed in Python. It allows users to test their knowledge across a collection of multiple-choice questions covering different areas such as geography, science, history, mathematics, technology, sports, literature, and general knowledge.

The application maintains a predefined question pool containing multiple-choice questions with four possible options—A, B, C, and D. For every quiz session, the program randomly selects **10 questions** from the available question pool, ensuring that the questions can vary between different executions.

The application provides a simple command-line interface where users answer each question interactively. At the end of the quiz, the application calculates and displays the user's final score and percentage.

## Features:

**Randomized Question Selection:**
The application maintains a large question pool and randomly selects 10 questions for every quiz session using Python's `random.sample()` function. This prevents the quiz from following the same question order every time.

**Multiple-Choice Questions:**
Each question contains four possible answers represented by:

```text
A. Option 1
B. Option 2
C. Option 3
D. Option 4
```

The user must enter one of the four valid choices.

**Wide Range of Topics:**
The question pool contains questions from multiple general knowledge categories, including:

* Geography
* Science
* Mathematics
* History
* Technology
* Sports
* Literature
* Human body and biology
* Astronomy
* Chemistry
* General knowledge

**Automatic Scoring:**
Every correct answer increases the user's score by one point. Incorrect answers do not increase the score.

**Answer Validation:**
The program accepts only `A`, `B`, `C`, or `D` as valid answer choices. The input is stripped of extra whitespace and converted to uppercase before validation.

**Immediate Feedback:**
After every answer, the program displays whether the response was correct or incorrect. If the answer is incorrect, the correct option is also displayed.

**Final Score and Percentage:**
After all questions have been answered, the application displays the final score in the following format:

```text
Your Final Score: X / 10
Percentage: XX.XX%
```

**Error Handling:**
The program uses exception handling around the answer input process so that unexpected input-related errors do not immediately terminate the quiz. The program instead displays an error message and proceeds to the next question.

## Technical Specifications:

**Language:** Python 3

**Primary Function:** `run_quiz()`

**Module Used:**

* `random` — used for randomly selecting questions from the question pool.

**Data Structures and Concepts:**

* List
* Dictionary
* Functions
* `random.sample()`
* `min()`
* `len()`
* `enumerate()`
* `for` loop
* `if-elif-else` conditional statements
* `try-except` exception handling
* `input()` and `print()`
* String `.strip()`
* String `.upper()`
* Dictionary key access
* Arithmetic operations
* Formatted strings and decimal formatting
* `if __name__ == "__main__":`

## How It Works:

**Question Pool:**
The program begins with a predefined `QUESTION_POOL` list. Every question is stored as a dictionary containing three main elements:

```python
{
    "q": "Question text",
    "options": ["A. ...", "B. ...", "C. ...", "D. ..."],
    "answer": "C"
}
```

The `q` field stores the question, `options` contains the four possible choices, and `answer` stores the correct option.

**Random Question Selection:**
When `run_quiz()` is executed, the program determines how many questions should be asked:

```python
num_questions_to_ask = min(10, len(QUESTION_POOL))
```

It then randomly selects the required number of questions using:

```python
selected_questions = random.sample(
    QUESTION_POOL,
    num_questions_to_ask
)
```

This ensures that each quiz session can contain a different combination of questions.

**Question Display:**
The selected questions are processed one at a time using a `for` loop and `enumerate()`. The question number, question text, and all four answer options are displayed to the user.

**User Answer Processing:**
The user enters an answer through the command line. The input is processed using:

```python
user_answer = input(
    "Your answer (A/B/C/D): "
).strip().upper()
```

This removes unnecessary spaces and converts lowercase responses such as `a` or `b` into uppercase form.

**Answer Validation:**
The program checks whether the entered answer belongs to the valid set:

```text
A, B, C, D
```

If the user enters another value, the answer is marked as incorrect and the program continues to the next question.

**Score Calculation:**
If the user's answer matches the stored correct answer, the score is increased by one:

```python
score += 1
```

For an incorrect answer, the program displays the correct answer without increasing the score.

**Percentage Calculation:**
After all selected questions have been processed, the final percentage is calculated using:

```text
Percentage = (Score / Number of Questions) × 100
```

The result is formatted to two decimal places before being displayed.

## Execution Guide:

### Run the Program

Save the Python source code as:

```text
Nivash(1).py
```

Run it using:

```bash
python "Nivash(1).py"
```

or:

```bash
python3 "Nivash(1).py"
```

### Interactive Quiz Mode

When the program starts, it displays:

```text
========================================
         WELCOME TO THE QUIZ BOWL
========================================
```

The program then randomly selects 10 questions and displays them one by one.

### Example:

```text
Question 1: What is the capital of France?

A. London
B. Berlin
C. Paris
D. Madrid

Your answer (A/B/C/D): C
✅ Correct!
```

For an incorrect response:

```text
Question 2: Which planet is known as the Red Planet?

A. Venus
B. Saturn
C. Mars
D. Jupiter

Your answer (A/B/C/D): A
❌ Incorrect. The correct answer was C.
```

After all questions are completed, the program displays:

```text
========================================
              QUIZ FINISHED
========================================
Your Final Score: 8 / 10
Percentage: 80.00%
```

## Known Edge Cases & Quick Handling:

**Invalid Answer Choice:**
If the user enters a character other than `A`, `B`, `C`, or `D`, the program displays an invalid-choice message and marks that question as incorrect.

**Lowercase Answers:**
Lowercase responses such as `a`, `b`, `c`, or `d` are accepted because the input is converted to uppercase before validation.

**Extra Spaces:**
Leading or trailing spaces are removed using `.strip()`, allowing inputs such as `C` to be processed correctly.

**Unexpected Input Error:**
The answer-processing section is protected using `try-except`. If an unexpected exception occurs, the program displays an error message and moves to the next question.

**Question Pool Size:**
The program is designed to ask a maximum of 10 questions. If the question pool contains fewer than 10 questions, the program automatically uses the number of available questions instead.

## Conclusion:

The **Quiz Bowl** serves as an interactive Python command-line application designed to test general knowledge while demonstrating important programming concepts. Through a combination of a structured question pool, dictionaries, lists, random question selection, loops, conditional statements, input validation, exception handling, and score calculation, the project provides a practical implementation of fundamental Python programming techniques.

Randomly selecting questions makes each quiz session more varied, while the multiple-choice format provides a simple and intuitive interaction model. The final score and percentage allow the user to immediately understand their performance.

Moving forward, potential enhancements include **difficulty levels, category selection, larger question databases, timed questions, negative marking, high-score storage, user profiles, a leaderboard, database-based question storage, and a graphical user interface (GUI)**.
