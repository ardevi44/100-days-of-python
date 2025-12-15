
class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        self.questions_bank = []

    def get_question_and_answer(self):
        return f"Question: {self.text} Answer: {self.answer}"

    @staticmethod
    def create_question_bank(data):
        """Static method that receives a list of dictionaries with questions in form: {question: string, correct_answer: string} and returns
        a list of Question objects"""
        question_bank = []
        for question in data:
            question_bank.append(
                Question(question["question"], question["correct_answer"]))
        return question_bank
