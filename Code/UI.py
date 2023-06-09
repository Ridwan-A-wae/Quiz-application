from tkinter import *
from controller import Controller
THEM_APP = "#375362"


class UserInterface:
    def __init__(self,controller:Controller):
        self.controller = controller
        # หน้าต่างโปรแกรม
        self.window = Tk()
        self.window.title("โปรแกรมทำข้อสอบ")
        self.window.config(padx=20,pady=20,bg=THEM_APP)

        #พื้นที่แสดงคะแนนสอบ
        self.scoreLable = Label(text="คะแนน : 0",fg="white",bg=THEM_APP)
        self.scoreLable.grid(row=0,column=2)

        #พื้นที่แสดงโจทย์ปัญหา
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.qusetion_text = self.canvas.create_text( 
            150,
            125,
            width=280,
            text="1+1 = 2",
            font=("Arial",18,"bold"),
            fill=THEM_APP
        )
        self.canvas.grid(row=1,column=1,columnspan=2,pady=50)

        #ปุ่มตัวเลือก
        ture_image = PhotoImage(file="images/check.png")
        self.ture_BTN = Button(image=ture_image,command=self.true_pressed)
        self.ture_BTN.grid(row=2,column=1)

        false_image = PhotoImage(file="images/remove.png")
        self.false_BTN = Button(image=false_image,command=self.false_pressed)
        self.false_BTN.grid(row=2,column=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question (self):
        if  self.controller.hasquestion():
            q_text = self.controller.nextQuestion()
            self.scoreLable.config(text=f"คะแนน : {self.controller.score}")
            self.canvas.itemconfig(self.qusetion_text, text=q_text)
        else :
            self.canvas.itemconfig(self.qusetion_text,text="สิ้นสุดการทำข้อสอบ")
            self.scoreLable.config(text=f"คะแนน : {self.controller.score}")
            self.ture_BTN.config(state="disabled")
            self.false_BTN.config(state="disabled")

        
    
    def true_pressed(self):
        self.controller.checkAnswer("true")
        self.nextQuestion()
    def false_pressed(self):
        self.controller.checkAnswer("false")
        self.nextQuestion()

    def nextQuestion(self):
        self.window.after(30,self.get_next_question)

