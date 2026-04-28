from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QDoubleSpinBox, QPushButton, QHBoxLayout, QLineEdit, QMessageBox,  QGridLayout, QFrame, QSizePolicy
from PySide6.QtCore import Qt

class CalculatorComponent(QWidget):
    def __init__(self, title, variables, calc_function, is_percentage=False):
        super().__init__()
        self.variables = variables
        self.calc_function = calc_function
        self.is_percentage = is_percentage
        self.spin_boxes = {}

        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignLeft)  # 👈 ВАЖНО: прижать всё влево

        self.setObjectName("calculator_component")
        self.setStyleSheet("""
            #calculator_component {
                border: 1px solid #C0C0C0;
                border-radius: 8px;
                padding: 10px;
            }
        """)

        # Title
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        layout.addWidget(title_label, alignment=Qt.AlignLeft)

        # Variables descriptions
        desc_widget = QWidget()
        desc_layout = QVBoxLayout(desc_widget)
        desc_layout.setAlignment(Qt.AlignLeft)

        for symbol, desc in variables.items():
            display_symbol = self._format_symbol(symbol)
            desc_label = QLabel(f"{display_symbol} - {desc}")
            desc_label.setTextFormat(Qt.RichText)
            desc_layout.addWidget(desc_label, alignment=Qt.AlignLeft)

        layout.addWidget(desc_widget, alignment=Qt.AlignLeft)

        # Input fields (табличное выравнивание)
        form_widget = QWidget()
        form_layout = QGridLayout(form_widget)

        form_layout.setHorizontalSpacing(10)
        form_layout.setVerticalSpacing(6)

        row = 0

        for symbol in variables.keys():
            display_symbol = self._format_symbol(symbol)

            symbol_label = QLabel(display_symbol)
            symbol_label.setTextFormat(Qt.RichText)
            symbol_label.setMinimumWidth(60)   # 👈 фиксируем колонку

            spin_box = QDoubleSpinBox()
            spin_box.setRange(0, 1000000)
            spin_box.setDecimals(2)
            spin_box.setFixedWidth(140)        # 👈 одинаковая ширина
            self.spin_boxes[symbol] = spin_box

            form_layout.addWidget(symbol_label, row, 0)
            form_layout.addWidget(spin_box, row, 1)

            row += 1

        layout.addWidget(form_widget, alignment=Qt.AlignLeft)

        # ===== RESULT + BUTTON =====
        bottom_widget = QWidget()
        bottom_layout = QHBoxLayout(bottom_widget)
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom_layout.setAlignment(Qt.AlignLeft)  # 👈 прижать строку

        self.result_edit = QLineEdit()
        self.result_edit.setPlaceholderText("Результат")
        self.result_edit.setReadOnly(True)
        self.result_edit.setFixedWidth(180)   # 👈 не растягивается

        calc_button = QPushButton("Рассчитать")
        calc_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 6px 12px;
                border-radius: 10px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        calc_button.clicked.connect(self.calculate)
        calc_button.setFixedSize(calc_button.sizeHint())  # 👈 фикс по контенту

        bottom_layout.addWidget(self.result_edit)
        bottom_layout.addWidget(calc_button)

        layout.addWidget(bottom_widget, alignment=Qt.AlignLeft)

        line = QFrame()
        line.setFrameShape(QFrame.HLine)
        line.setFrameShadow(QFrame.Plain)
        line.setStyleSheet("background-color: black; border: none;")
        line.setFixedHeight(1)

        line.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

        layout.addWidget(line)
        self.setLayout(layout)

    def _format_symbol(self, symbol):
        if not symbol:
            return ""

        first = symbol[0]
        rest = symbol[2:] if len(symbol) > 1 and symbol[1] == "_" else symbol[1:]
        mapping = {
            "ft": "фт",
            "mr": "мр",
            "VVST": "ВВСТ",
            "shtat": "штат",
            "isp": "испр",
            "sovr": "совр"
        }
        parts = rest.split("_")
        ru_rest = "".join(mapping.get(part, part) for part in parts)
        return f"{first}<sub>{ru_rest}</sub>"

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