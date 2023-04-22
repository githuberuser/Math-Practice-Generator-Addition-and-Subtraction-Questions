# Math Practice Generator (Addition and Subtraction Questions)
import datetime
from fpdf import FPDF
import os
import random

class MathBook:
    def __init__(self):
        self.date = datetime.date.today()
        self.questions = []
        self.answers = []

    def generate_questions(self):
        for i in range(100):
            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operator = random.choice(['+', '-'])
            question = f"{num1} {operator} {num2} = "
            self.questions.append(question)

    def generate_answers(self):
        for i in range(100):
            question = self.questions[i]
            answer = eval(question[:-2])
            self.answers.append(str(answer))

    def create_pdf(self):

        self.generate_questions()
        self.generate_answers()

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        pdf.cell(200, 10, str(self.date), ln=1)

        for i in range(100):
            if i % 25 == 0:
                pdf.ln()
            pdf.cell(40, 10, self.questions[i], border=0)

        pdf.add_page()
        pdf.cell(200, 10, "Answers", ln=1)
        for i in range(100):
            if i % 25 == 0:
                pdf.ln()
            pdf.cell(40, 10, self.answers[i], border=0)

        file_path = os.path.join(os.getcwd(), "{} practice.pdf".format(self.date))
        pdf.output(file_path)

book = MathBook()

book.create_pdf()

print('Done, saved at:',os.getcwd())
