from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QDoubleSpinBox, QPushButton, QHBoxLayout, QLineEdit, QMessageBox
from PySide6.QtCore import Qt

class CalculatorComponent(QWidget):
    def __init__(self, title, variables, calc_function, is_percentage=False):
        super().__init__()
        self.variables = variables
        self.calc_function = calc_function
        self.is_percentage = is_percentage
        self.spin_boxes = {}

        layout = QVBoxLayout()

        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title_label)

        # Variables descriptions
        for symbol, desc in variables.items():
            desc_label = QLabel(f"{symbol} - {desc}")
            layout.addWidget(desc_label)

        # Input fields
        for symbol in variables.keys():
            hbox = QHBoxLayout()
            symbol_label = QLabel(symbol)
            spin_box = QDoubleSpinBox()
            spin_box.setRange(0, 1000000)
            spin_box.setDecimals(2)
            self.spin_boxes[symbol] = spin_box
            hbox.addWidget(symbol_label)
            hbox.addWidget(spin_box)
            layout.addLayout(hbox)

        # Calculate button
        calc_button = QPushButton("Рассчитать")
        calc_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        calc_button.clicked.connect(self.calculate)
        layout.addWidget(calc_button)

        # Result edit
        self.result_edit = QLineEdit("Результат: ")
        self.result_edit.setReadOnly(True)
        layout.addWidget(self.result_edit)

        self.setLayout(layout)

    def calculate(self):
        values = {symbol: spin.value() for symbol, spin in self.spin_boxes.items()}
        try:
            result = self.calc_function(**values)
            if self.is_percentage:
                self.result_edit.setText(f"Результат: {result:.2f}%")
            else:
                self.result_edit.setText(f"Результат: {result:.4f}")
        except ZeroDivisionError:
            QMessageBox.warning(self, "Ошибка", "Деление на ноль! Проверьте введённые значения.")
        except Exception as e:
            QMessageBox.warning(self, "Ошибка", f"Произошла ошибка: {str(e)}")