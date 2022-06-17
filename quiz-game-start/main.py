from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

def main():
    database=[]
    counter=0
    for x in question_data:
        new_data=Question(x["text"],x["answer"])
        database.append(new_data)

    quiz=QuizBrain(database)
    while not quiz.still_has_questions():
        quiz.next_question()


main()
