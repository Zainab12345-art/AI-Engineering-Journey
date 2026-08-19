# Day 01 - Python Basics

This is my first day learning Python as part of my journey toward becoming an AI Engineer.

## Concepts Learned

- print()
- input()
- Variables
- Strings
- Integers
- Floats
- Type conversion
- f-strings
- Basic arithmetic

## Projects

1. Personal Introduction Generator
2. Calculator
3. Age Calculator
4. Student Information Generator

## Goal

My goal is to build strong Python fundamentals and eventually become a Generative AI / AI Engineer.

# 🐍 Day 02 — Python Fundamentals

Day 02 of my **AI Engineering Journey**.

Today I revised Day 01 concepts and continued learning the fundamentals of Python through practical exercises and a mini project.

## 🎯 Topics Learned

- Python Data Types
  - `str`
  - `int`
  - `float`
  - `bool`
- `type()` function
- Type Conversion
  - `int()`
  - `float()`
  - `str()`
- Arithmetic Operators
  - `+`
  - `-`
  - `*`
  - `/`
  - `//`
  - `%`
  - `**`
- Comparison Operators
  - `>`
  - `<`
  - `>=`
  - `<=`
  - `==`
  - `!=`
- Logical Operators
  - `and`
  - `or`
  - `not`
- Basic debugging and identifying logic errors
- Using f-strings for formatted output

## 🧪 Practicals

I completed 8 practical exercises:

1. Check Data Type
2. Integer Data Type
3. Float Data Type
4. Boolean Data Type
5. Type Conversion
6. Arithmetic Playground
7. Comparison Playground
8. Logical Playground

All practicals are included in:

```text
Practice-02.py
````

## 🎓 Mini Project — Student Marks Calculator

For the final challenge, I built a **Student Marks Calculator**.

The program:

* Takes the student's name
* Takes Python marks
* Takes Database marks
* Takes Networking marks
* Calculates total marks
* Calculates average marks
* Displays a formatted student marks report

### Example

```text
=======================================================
                 STUDENT MARKS REPORT
=======================================================
Student Name: Zainab
Python Marks: 99.0
Database Marks: 98.0
Networking Marks: 89.0
Total Marks: 286.0
Average Marks: 95.33
=======================================================
```

The project is available in:

```text
student_marks_calculator.py
```

## 📂 Day 02 Structure

```text
Day-02/
│
├── Practice-02.py
├── student_marks_calculator.py
└── README.md
```

## 🧠 Key Learnings

* Variables can store different types of data.
* `input()` normally returns a `str`.
* Values can be converted using `int()`, `float()`, and `str()`.
* `%` returns the remainder of a division.
* `//` performs floor division.
* `=` is used for assignment.
* `==` is used for comparison.
* Comparison and logical operators return Boolean values.
* A program can run successfully and still contain a logic error.
* Debugging is an important part of programming.
* Writing practical programs helps turn concepts into actual programming skills.

## 🚀 AI Engineering Journey

My current learning path is:

```text
Python
   ↓
Software Development
   ↓
AI Fundamentals
   ↓
Generative AI
   ↓
RAG
   ↓
AI Agents
   ↓
AI Automation
   ↓
Deployment
   ↓
AI Engineer
```

### Progress

```text
Day 01 ✅
Day 02 ✅
```

## 👩‍💻 Author

**Zainab**
BS Information Technology — QAU

**Career Goal:** AI Engineer

---

⭐ Learning Python from zero and building my skills step by step toward AI Engineering.

```
```

# 🐍 Python Day 03 — Conditional Statements

## 📌 Overview

Day 03 focused on **decision-making in Python**. I learned how to make programs respond differently based on conditions using `if`, `elif`, `else`, logical operators, and nested `if` statements.

I also practiced these concepts through multiple practical programs and mini projects.

---

## 🎯 Learning Objectives

By the end of Day 03, I practiced:

* `if` statements
* `if-else` statements
* `if-elif-else` statements
* Nested `if` statements
* Comparison operators
* Logical operators
* Conditions with user input
* Combining multiple conditions
* Basic input validation
* Building small decision-based programs

---

## 🧠 Concepts Learned

### 1. `if` Statement

The `if` statement executes a block of code when a condition is `True`.

```python
if age >= 18:
    print("You are eligible.")
```

### 2. `if-else`

Used when there are two possible outcomes.

```python
if num % 2 == 0:
    print("Even")
else:
    print("Odd")
```

### 3. `if-elif-else`

Used when there are multiple conditions.

```python
if marks >= 90:
    print("A")
elif marks >= 80:
    print("B")
else:
    print("F")
```

### 4. Nested `if`

An `if` statement inside another `if` statement.

```python
if age >= 18:
    if marks >= 60:
        print("Eligible")
```

### 5. Logical Operators

I practiced:

* `and`
* `or`
* `not`

Example:

```python
if age >= 18 and is_student == "yes":
    print("Eligible")
```

---

## 📂 Practical Programs

| #  | Program                      | Main Concept             |
| -- | ---------------------------- | ------------------------ |
| 01 | Age Checker                  | `if-else`                |
| 02 | Positive/Negative Checker    | `if-elif-else`           |
| 03 | Even/Odd Checker             | Modulus + condition      |
| 04 | Grade Calculator             | `if-elif-else`           |
| 05 | Login System                 | `and` + comparison       |
| 06 | Eligibility Checker          | Logical operators        |
| 07 | University Admission Checker | Nested `if`              |
| 08 | Student Result Analyzer      | Nested `if` + validation |
| 09 | ATM Withdrawal               | Nested conditions        |
| 10 | Movie Ticket Booking         | Multiple conditions      |
| 11 | Password Strength Checker    | Conditional logic        |

---

## 💻 Mini Projects

### 🏧 ATM Withdrawal

Practiced:

* Account balance
* Withdrawal validation
* Insufficient balance checking
* Nested `if`

### 🎬 Movie Ticket Booking

Practiced:

* Age-based ticket pricing
* Student discount
* Multiple conditions
* Nested `if`

### 🔐 Password Strength Checker

Practiced:

* `len()`
* Password length checking
* Conditional classification

---

## 🧪 Testing & Debugging

During Day 03, I tested my programs with different inputs, including:

* Positive numbers
* Negative numbers
* Zero
* Different ages
* Different marks
* Correct and incorrect login credentials
* Valid and invalid marks
* Different student statuses

I also learned that **input placement matters**.

For example, if marks are only required when:

```python
if age >= 18:
```

then the `marks` input should be placed inside that condition so that it is not requested unnecessarily.

---

## 🛠️ Tools Used

* Python
* VS Code / Terminal
* PowerShell
* Git
* GitHub

---

## 📈 Day 03 Progress

### Completed

* [x] `if`
* [x] `if-else`
* [x] `if-elif-else`
* [x] Nested `if`
* [x] Comparison operators
* [x] Logical operators
* [x] User input with conditions
* [x] Conditional mini projects
* [x] Debugging and testing

---

## 💡 Key Takeaway

Day 03 taught me how Python can **make decisions based on conditions**.

I moved from writing simple sequential programs to creating programs that can make different decisions depending on user input.

> **Day 03 Focus:** Think → Check Condition → Make Decision → Execute Code

---

## 🚀 Next Step

**Day 04 — Loops**

Topics:

* `while` loop
* `for` loop
* `range()`
* Counters
* Accumulators
* Repetition
* Loop-based mini projects

---

**Python Learning Journey — Day 03 Complete ✅**

# 🐍 Python Day 04 — Loops & Iteration

## 📌 Overview

Day 04 focused on **loops and iteration in Python**.

I learned how to repeat a block of code using `while` and `for` loops. I also practiced counters, accumulators, `range()`, mathematical calculations, and finding the largest and smallest values.

The day ended with a **Number Analyzer mini project** that combined multiple concepts together.

---

## 🎯 Learning Objectives

By the end of Day 04, I practiced:

* `while` loops
* `for` loops
* `range()`
* Loop counters
* Accumulator variables
* Even/odd checking inside loops
* Calculating sums
* Calculating averages
* Finding largest numbers
* Finding smallest numbers
* Factorial calculation
* Building a loop-based mini project

---

## 🧠 Concepts Learned

### 1. `while` Loop

A `while` loop repeatedly executes code while a condition remains `True`.

```python
num = 1

while num <= 10:
    print(num)
    num = num + 1
```

The variable must be updated so that the loop can eventually stop.

---

### 2. `for` Loop

A `for` loop is useful when we know how many times we want to repeat something.

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

---

### 3. `range()`

I practiced different forms of `range()`.

```python
range(1, 6)
```

```python
range(5, 0, -1)
```

```python
range(2, 22, 2)
```

The third value represents the **step**.

---

### 4. Counters

A counter keeps track of how many times something happens.

Example:

```python
even_count = 0

even_count = even_count + 1
```

---

### 5. Accumulators

An accumulator stores an ongoing total.

Example:

```python
total = 0

total = total + num
```

This technique was used for calculating sums and totals.

---

## 📂 Practical Programs

| #  | Program                    | Main Concept           |
| -- | -------------------------- | ---------------------- |
| 01 | Print Numbers 1–10         | `while` loop           |
| 02 | Countdown                  | `while` loop           |
| 03 | Even Numbers               | `while` + condition    |
| 04 | Number Counter             | `while` + user input   |
| 05 | Print Numbers 1–5          | `for` + `range()`      |
| 06 | Countdown with For Loop    | `for` + negative step  |
| 07 | Even Numbers with For Loop | `for` + modulus        |
| 08 | Sum of Numbers             | Accumulator            |
| 09 | Multiplication Table       | `for` + arithmetic     |
| 10 | Even/Odd Counter           | Counters               |
| 11 | Largest Number             | Comparison + loop      |
| 12 | Factorial                  | Accumulator + loop     |
| 13 | Number Analyzer            | Multiple loop concepts |

---

## 🔢 Important Examples

### Even Numbers

I practiced two approaches:

```python
for i in range(1, 21):
    if i % 2 == 0:
        print(i)
```

And a more direct approach:

```python
for i in range(2, 22, 2):
    print(i)
```

This helped me understand how the `step` argument in `range()` works.

---

## ➕ Sum and Average

I practiced using an accumulator:

```python
total = 0

for i in range(1, 6):
    total = total + i
```

I also calculated averages using:

```python
average = total / 5
```

---

## 🔢 Factorial

I implemented factorial using a `for` loop.

For example:

```text
5 × 4 × 3 × 2 × 1 = 120
```

This helped me understand how a variable can continuously store and update a calculation inside a loop.

---

## 📊 Number Analyzer Mini Project

The final practical combined multiple concepts.

The program accepts **5 numbers** and calculates:

* Sum
* Average
* Number of even values
* Number of odd values
* Largest number
* Smallest number

Example:

```text
Enter numbers: 45
Enter numbers: 90
Enter numbers: 8
Enter numbers: 76
Enter numbers: 2

Sum of Numbers: 221
Average of Numbers: 44.2
Total Even Numbers: 4
Total Odd Numbers: 1
Largest Number: 90
Smallest Number: 2
```

---

## 🧠 Important Logic Learned

One important problem I solved was finding the smallest number.

Instead of assuming `0` is always the smallest, I used the **first entered number** as the initial largest and smallest value:

```python
if i == 0:
    largest = num
    smallest = num
```

Then subsequent numbers are compared:

```python
if num > largest:
    largest = num

if num < smallest:
    smallest = num
```

This approach also works correctly when negative numbers are entered.

---

## 🧪 Testing & Debugging

During Day 04, I tested programs using different inputs to verify:

* Counting logic
* Even/odd detection
* Countdown logic
* Sum calculations
* Multiplication tables
* Largest/smallest values
* Factorial calculations
* Average calculations

I also debugged a `smallest number` issue where initializing:

```python
smallest = 0
```

caused incorrect results for positive numbers.

---

## 🛠️ Tools Used

* Python
* VS Code / Terminal
* PowerShell
* Git
* GitHub

---

## 📈 Day 04 Progress

### Completed

* [x] `while` loop
* [x] `for` loop
* [x] `range()`
* [x] `range()` step
* [x] Counters
* [x] Accumulators
* [x] Even/Odd logic
* [x] Sum calculation
* [x] Average calculation
* [x] Largest number
* [x] Smallest number
* [x] Factorial
* [x] Number Analyzer mini project
* [x] Loop debugging

---

## 💡 Key Takeaway

Day 04 taught me how to **repeat operations efficiently** instead of writing the same code multiple times.

I learned that loops become much more powerful when combined with:

```text
Loops
  +
Conditions
  +
Counters
  +
Accumulators
  +
User Input
  =
Useful Programs
```

> **Day 04 Focus:** Repeat → Calculate → Count → Analyze

---

## 🚀 Next Step

Before starting the next Python topic, I will practice the concepts learned in Days 01–04 through revision, debugging exercises, and new mini projects.

---

**Python Learning Journey — Day 04 Complete ✅**

