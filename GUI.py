import datetime
import os
import random
from fpdf import FPDF
from PyQt5 import QtWidgets

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

class MathBookGUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Math Practice Generator')
        self.setGeometry(100, 100, 400, 200)

        self.title_label = QtWidgets.QLabel('Click the button below to generate a PDF file!', self)
        self.title_label.setGeometry(50, 50, 300, 50)


        self.generate_button = QtWidgets.QPushButton('Generate PDF', self)
        self.generate_button.setGeometry(125, 125, 150, 50)

        self.generate_button.clicked.connect(self.generate_pdf)


    def generate_pdf(self):
        book = MathBook()
        book.create_pdf()
        QtWidgets.QMessageBox.about(self, "Message", "Successfully Generated!\nPDF file has been saved at: {}".format(os.getcwd()))

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    math_book_gui = MathBookGUI()
    math_book_gui.show()
    app.exec_()
