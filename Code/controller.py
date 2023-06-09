class Controller:
    def __init__(self,data,):
        self.question_list = data
        self.question_number = 0
        self.score = 0
        self.current =None

    
    def checkAnswer(self,userInput):
        self.correctAnswer = self.current.answer
        if(userInput.lower() == self.correctAnswer.lower()):
            self.score += 1
            return True
        else :
            return False

    def nextQuestion(self):
        self.current = self.question_list[self.question_number]
        self.question_number += 1
        # print("NO.",self.question_number,":",current.text," (True/False)",)
        # user_answer = input("Your answer :")
        # self.checkAnswer(user_answer,current.answer)
        return f"{self.question_number}) {self.current.text}"


    def hasquestion(self):
        return self.question_number <len(self.question_list)
    

    
