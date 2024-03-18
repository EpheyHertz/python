from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit

class Calcapp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CALCULATOR App")
        self.resize(250, 300)
        self.text_box = QLineEdit()
        self.text_box.setStyleSheet("font-size: 20px;")  # Set font size for the text box
        self.setStyleSheet("background-color:blue")
        self.grid = QGridLayout()
        self.buttons = ["1", "2", "3", "/",
                        "4", "5", "6", "*",
                        "7", "8", "9", "-",
                        "0", ".", "=", "+"]
        row = 0
        col = 0
        for text in self.buttons:
            button = QPushButton(text)
            button.setStyleSheet("font-size: 16px;")  # Set font size for the buttons
            button.clicked.connect(self.button_click)
            self.grid.addWidget(button, row, col)
            col += 1
            if col > 3:
                col = 0
                row += 1

        self.clear = QPushButton("Clear")
        self.clear.setStyleSheet("background-color: #4CAF50; color: white;")  # Set background color and text color for the "Clear" button
        self.delete = QPushButton("Del")
        self.delete.setStyleSheet("background-color: #f44336; color: white;")  # Set background color and text color for the "Del" button
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear)
        button_row.addWidget(self.delete)

        master_layout.addLayout(button_row)

        self.setLayout(master_layout)

        self.clear.clicked.connect(self.clear_text)
        self.delete.clicked.connect(self.delete_text)

    def button_click(self):
        button = app.sender()
        text = button.text()
        if text == "=":
            symbol = self.text_box.text()
            try:
                res = eval(symbol)
                self.text_box.setText(str(res))
            except Exception as e:
                print("ERROR!", e)
        else:
            current_expression = self.text_box.text()
            self.text_box.setText(current_expression + text)

    def clear_text(self):
        self.text_box.clear()

    def delete_text(self):
        current_expression = self.text_box.text()
        self.text_box.setText(current_expression[:-1])

if __name__ == "__main__":
    app = QApplication([])
    main_window = Calcapp() 
    main_window.show()
    app.exec()