import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout
from component import CalculatorComponent
import formulas

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Математические расчёты ВВСТ")
        self.setGeometry(100, 100, 800, 600)

        scroll_area = QScrollArea()
        self.setCentralWidget(scroll_area)

        container = QWidget()
        scroll_area.setWidget(container)
        scroll_area.setWidgetResizable(True)

        layout = QVBoxLayout(container)

        # Компонент 1: Коэффициент соответствия
        variables1 = {
            "Q_фтВВСТ": "коэффициент фактического значения обобщенных, наиболее значимых показателей вида ВВСТ",
            "Q_мрВВСТ": "коэффициент обобщенных требуемых показателей ТТХ"
        }
        comp1 = CalculatorComponent(
            "Коэффициент соответствия наиболее значимых показателей",
            variables1,
            formulas.coefficient_correspondence,
            is_percentage=False
        )
        layout.addWidget(comp1)

        # Компонент 2: Обеспеченность ВВСТ на год
        variables2 = {
            "N_ВВСТ": "количество образцов группы ВВСТ, имеющихся в наличии",
            "N_ВВСТштат": "потребное количество образцов группы ВВСТ на год"
        }
        comp2 = CalculatorComponent(
            "Обеспеченность ВВСТ на год",
            variables2,
            formulas.provision_VVST_year,
            is_percentage=True
        )
        layout.addWidget(comp2)

        # Компонент 3: Обеспеченность исправными образцами
        variables3 = {
            "N_испр.ВВСТ": "количество исправных образцов группы ВВСТ",
            "N_ВВСТштат": "потребное количество образцов группы ВВСТ на год"
        }
        comp3 = CalculatorComponent(
            "Обеспеченность исправными образцами",
            variables3,
            formulas.provision_serviceable,
            is_percentage=True
        )
        layout.addWidget(comp3)

        # Компонент 4: Обеспеченность современными образцами
        variables4 = {
            "N_совр.ВВСТ": "количество современных образцов группы ВВСТ",
            "N_ВВСТштат": "потребное количество образцов группы ВВСТ на год"
        }
        comp4 = CalculatorComponent(
            "Обеспеченность современными образцами ВВСТ",
            variables4,
            formulas.provision_modern,
            is_percentage=True
        )
        layout.addWidget(comp4)

        # Компонент 5: Доля современных образцов
        variables5 = {
            "N_совр.ВВСТ": "количество современных образцов группы ВВСТ",
            "N_ВВСТ": "количество образцов группы ВВСТ, имеющихся в наличии"
        }
        comp5 = CalculatorComponent(
            "Доля современных образцов ВВСТ",
            variables5,
            formulas.share_modern,
            is_percentage=True
        )
        layout.addWidget(comp5)

        # Компонент 6: Коэффициент технической готовности
        variables6 = {
            "N_исп.ВВСТ": "количество исправных образцов группы ВВСТ",
            "N_ВВСТ": "общее количество образцов группы ВВСТ"
        }
        comp6 = CalculatorComponent(
            "Коэффициент технической готовности ВВСТ",
            variables6,
            formulas.technical_readiness,
            is_percentage=False
        )
        layout.addWidget(comp6)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())