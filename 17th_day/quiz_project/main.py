# from data import *
from api_data import *
from quiz_brain import *
from question import *

# Create the question bank
question_brain = QuestionBrain(
    Question.create_question_bank(questions_data["results"]))

while question_brain.still_has_questions():
    question_brain.next_question()
print(question_brain.get_final_message())
