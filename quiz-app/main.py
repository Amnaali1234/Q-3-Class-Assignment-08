import streamlit as st
import random
import time

class BaseQuiz:
    def __init__(self):
        self.questions = []

    def get_random_question(self):
        return random.choice(self.questions)

class OOPQuiz(BaseQuiz):
    def __init__(self):
        super().__init__()
        self.questions = [
            {
                "question": "What is Encapsulation in OOP?",
                "options": [
                    "Binding data and methods together",
                    "Creating child classes",
                    "Hiding class name",
                    "Writing long code"
                ],
                "answer": "Binding data and methods together"
            },
            {
                "question": "What does Inheritance allow in OOP?",
                "options": [
                    "To hide internal details",
                    "To use the same method in multiple ways",
                    "To create new class from an existing class",
                    "To limit access to methods"
                ],
                "answer": "To create new class from an existing class"
            },
            {
                "question": "Which of the following best defines Abstraction?",
                "options": [
                    "Showing all details to the user",
                    "Hiding internal logic and showing only necessary parts",
                    "Making variables global",
                    "None of the above"
                ],
                "answer": "Hiding internal logic and showing only necessary parts"
            },
            {
                "question": "What is Polymorphism in OOP?",
                "options": [
                    "Ability to change variable types",
                    "Ability of one function to behave differently based on context",
                    "Using multiple inheritance",
                    "Creating global variables"
                ],
                "answer": "Ability of one function to behave differently based on context"
            },
            {
                "question": "Which keyword is used to define a class in Python?",
                "options": ["object", "def", "function", "class"],
                "answer": "class"
            },
            {
                "question": "What is the default access modifier in Python?",
                "options": ["private", "protected", "public", "none"],
                "answer": "public"
            },
            {
                "question": "Which symbol is used for inheritance in Python?",
                "options": [":", "->", "()", "{}"],
                "answer": "()"
            },
            {
                "question": "How do you create an object in Python?",
                "options": [
                    "obj = class()",
                    "object.create(class)",
                    "obj = new class",
                    "create object class"
                ],
                "answer": "obj = class()"
            },
            {
                "question": "What is `__init__` in Python?",
                "options": [
                    "A loop",
                    "A constructor method",
                    "A variable",
                    "A class"
                ],
                "answer": "A constructor method"
            },
            {
                "question": "Which method is automatically called when an object is created?",
                "options": ["__str__", "__del__", "__init__", "start"],
                "answer": "__init__"
            },
            {
                "question": "Which OOP principle restricts direct access to data?",
                "options": ["Inheritance", "Abstraction", "Encapsulation", "Polymorphism"],
                "answer": "Encapsulation"
            },
            {
                "question": "Which of the following is not a feature of OOP?",
                "options": ["Modularity", "Procedural execution", "Code Reusability", "Data Hiding"],
                "answer": "Procedural execution"
            },
            {
                "question": "Which function is used to represent objects as strings?",
                "options": ["__init__", "__str__", "repr", "print"],
                "answer": "__str__"
            },
            {
                "question": "Which symbol is used to access methods from an object?",
                "options": [".", "->", "::", "#"],
                "answer": "."
            },
            {
                "question": "How can you prevent a method from being overridden?",
                "options": ["Use 'private' keyword", "Use '__' before the method name", "Make it static", "You can't prevent it"],
                "answer": "Use '__' before the method name"
            },
            {
                "question": "Which keyword is used to inherit from a class?",
                "options": ["inherits", "extends", "class", "None – just use ()"],
                "answer": "None – just use ()"
            },
            {
                "question": "Can Python classes support multiple inheritance?",
                "options": ["Yes", "No", "Only with decorators", "Only with modules"],
                "answer": "Yes"
            },
            {
                "question": "What does `super()` do in Python?",
                "options": [
                    "Calls the base class constructor",
                    "Skips to the next method",
                    "Ends the class",
                    "None of the above"
                ],
                "answer": "Calls the base class constructor"
            },
            {
                "question": "Which of the following best defines a class?",
                "options": [
                    "A block of reusable code",
                    "A blueprint for creating objects",
                    "A function that returns values",
                    "An operator"
                ],
                "answer": "A blueprint for creating objects"
            },
            {
                "question": "Which of the following is an example of polymorphism?",
                "options": [
                    "Two classes having the same method name with different behavior",
                    "A class inside a class",
                    "A function calling itself",
                    "None of these"
                ],
                "answer": "Two classes having the same method name with different behavior"
            }
        ]



st.title("OOP Concepts Quiz 🎯📝")

quiz = OOPQuiz()

if "current_question" not in st.session_state:
    st.session_state.current_question = quiz.get_random_question()

question = st.session_state.current_question

st.subheader(question["question"])
selected_option = st.selectbox("Choose your answer", question["options"], key="answer")

if st.button("Submit Answer"):
    if selected_option == question["answer"]:
        st.success("✅ Correct!🎉")
    else:
        st.error("❌ Incorrect! The correct answer is: " + question["answer"])

    time.sleep(3)
    st.session_state.current_question = quiz.get_random_question()
    st.rerun()


