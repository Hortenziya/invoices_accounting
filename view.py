from PyQt6.QtCore import QDate, Qt
from PyQt6.QtGui import QStandardItemModel, QStandardItem
from PyQt6.QtWidgets import (
    QCheckBox,
    QDateEdit,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTableView, QSizePolicy,
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
        self._invalid_number_checkbox = QCheckBox("Bills error ")
        self._process_form_button = QPushButton("Send")
        self._process_table_button = QPushButton("Show orders")

        layout = QVBoxLayout()
        layout.addWidget(self._label)
        layout.addWidget(self._text_edit)
        layout.addWidget(self._date_edit)
        layout.addWidget(self._invalid_number_checkbox)
        layout.addWidget(self._process_form_button)
        layout.addWidget(self._process_table_button)
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

    def set_table(self, on_click):
        self._process_table_button.clicked.connect(on_click)

    def set_information_of_last_bill(self, account_number: int, details: str):
        self._label.setText(
            f"The last bill number: <b> {account_number} </b>,"
            f" {details}",
        )


class WindowTable(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("DB Table")

        self.table_view = QTableView(self)
        self.table_view.setSizePolicy(QSizePolicy.Policy.Expanding,
                                      QSizePolicy.Policy.Expanding)
        layout = QVBoxLayout()
        layout.addWidget(self.table_view)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

    def populate_orders(self, all_orders):
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(
            ["ID", "Account Number", "Total", "Details", "Date Send"])
        for order in all_orders:
            row = [
                QStandardItem(str(order.id)),
                QStandardItem(order.account_number),
                QStandardItem(str(order.total)),
                QStandardItem(order.details),
                QStandardItem(str(order.date_send)),
            ]
            model.appendRow(row)

        self.table_view.setModel(model)
        self.table_view.resizeColumnsToContents()
        self.table_view.horizontalHeader().setStretchLastSection(True)
