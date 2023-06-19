
from PyQt6.QtCore import QDate, Qt
from PyQt6.QtWidgets import (
    QCheckBox,
    QDateEdit,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class Window(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.resize(400, 350)
        self.setWindowTitle("Main")

        self._label = QLabel("<b> The last bill number</b>", self)
        self._label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._label.adjustSize()

        self._date_edit = QDateEdit()
        self._date_edit.setDate(QDate.currentDate())
        self._date_edit.setCalendarPopup(True)

        self._text_edit = QLineEdit()
        self._invalid_number_checkbox = QCheckBox("Помилка в номері рахунку")
        self._process_form_button = QPushButton("Відправити")

        layout = QVBoxLayout()
        layout.addWidget(self._label)
        layout.addWidget(self._text_edit)
        layout.addWidget(self._date_edit)
        layout.addWidget(self._invalid_number_checkbox)
        layout.addWidget(self._process_form_button)
        self.setLayout(layout)

    def get_information(self):
        details = self._text_edit.text()
        date = self._date_edit.date().toPyDate()
        checkbox = False
        if self._invalid_number_checkbox.isChecked():
            checkbox = True
        return details, date, checkbox

    def set_on_click(self, on_click):
        self._process_form_button.clicked.connect(on_click)

    def set_information_of_last_bill(self, account_number: int, details: str):
        self._label.setText(
            f"The last bill number: <b> {account_number} </b>,"
            f" {details}",
        )
