# Project 1 - Rule-Based AI Chatbot 

## **What is this?**

This is the foundation phase of my **Artificial Intelligence Engineer** role at **DecodeLabs**. Instead of "learning" on its own, this chatbot uses a **Logic Engine** to follow my exact instructions.


---

# How It Works

## 1. Input

The chatbot takes text from the user.

Example:

```python id="kx6jqo"
user_input = input("You: ")
```

### Cleaning the Input

Users may type words in different ways like:

* `HELLO`
* `hello`
* `Hello`

To make the input easier to check, we use:

```python id="b3o1zl"
.lower()
.strip()
```

Example:

```python id="wt1y80"
user_input = input("You: ").lower().strip()
```

---

## 2. Process

The chatbot checks the message using `if-else` statements.

Example:

```python id="3bkqzm"
if user_input == "hello":
    print("Bot: Hello!")
```

### Rules

* If the user says `"hello"` → respond with a greeting
* If the user says `"exit"` or `"bye"` → stop the chatbot
* Anything else → show an unknown message

Example:

```python id="6v7qg2"
if user_input == "hello":
    print("Bot: Hello!")

elif user_input == "bye":
    print("Bot: Goodbye!")
    break

else:
    print("Bot: I don't understand.")
```

---

## 3. Output

The chatbot prints a response and keeps running using a loop.

Example:

```python id="1v2j4c"
while True:
```

---

# Goal of the Project

Learn how a basic chatbot works using:

* User input
* String cleaning
* `if-else` conditions
* Loops

---

# Task Checklist

* [ ] Create a `while` loop
* [ ] Use `.lower()` and `.strip()`
* [ ] Add greeting responses
* [ ] Add exit commands
* [ ] Add fallback response
* [ ] Test the chatbot
