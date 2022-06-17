
from genericpath import exists


class QuizBrain:
    
    def __init__(self, q_list):
        self.question_number = 0
        self.correct=0
        self.question_list = q_list

    def still_has_questions(self):
        if self.question_number!=len(self.question_list):
            return False
        else:
            return True

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        answer=input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(answer,current_question.answer)
    
    def check_answer(self,answer,correct_answer):
        if answer.lower()==correct_answer.lower():
            print("You got it right!")
            self.correct+=1
        else:
            print("That's wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current socre is {self.correct}/{self.question_number}")