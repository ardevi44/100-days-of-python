import math


class QuestionBrain:
    def __init__(self, question_list):
        """Receives a list of Question objects and initialize the question_list attribute of its class"""
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Get a question based on its 'question_number' attribute and ask the user for the answer"""
        current_question = self.question_list[self.question_number]
        answer = input(
            f"Q.{self.question_number + 1}: {current_question.text}. (True/False)?: ")
        self.question_number += 1
        self.check_answer(answer, current_question.answer)

    def still_has_questions(self):
        """Return True if there are questions remaining based on the question number"""
        return True if self.question_number < len(self.question_list) else False

    def get_final_message(self):
        decimal_rating = (self.score / len(self.question_list)) * 100
        rating = math.floor(decimal_rating) if decimal_rating - \
            math.floor(decimal_rating) < 0.5 else math.ceil(decimal_rating)
        return "You've completed the quiz\n" + f"Your final score was: {self.score}/{len(self.question_list)}\n" + f"Your rating is {rating}"

    def check_answer(self, answer, correct_answer):
        """Check the answer against the correct answer, increments the score in 1 if both
        are the equal, and print the score till now"""
        if answer.lower().strip() == correct_answer.lower().strip():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong!")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
