from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(q_text=question_text, q_answer=question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
      quiz.next_quetion()


#new_q =  Question()

# for index in range(len(question_data)):
#     for key in question_data[index]:
#         print(question_data[index][key])


