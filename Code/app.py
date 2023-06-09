# รันโปรแกรม
from Question import Question
from data import question_data
from controller import Controller
from UI import UserInterface


all_question=[]

# กำหนดโจทย์ปัญหา
for item in question_data:
    text = item["text"]
    answer = item["answer"]
    question=Question(text,answer)
    all_question.append(question)

# แผงควบคุม
controller = Controller(all_question)
# GUI
userinterface = UserInterface(controller)