from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QCheckBox
from PyQt5.QtCore import pyqtSignal, QRegExp, Qt, QSize
from PyQt5.QtGui import QRegExpValidator
import re

class FilterWidget(QWidget):
    # Signal emitted when filters are applied
    filtersApplied = pyqtSignal(str, str, list)

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.setMaximumSize(QSize(200, 600))
        self.setMinimumSize(QSize(200, 450))

        # Label and input field for start date
        self.layout.addWidget(QLabel('Data de início:'))
        self.start_date_edit = QLineEdit()
        self.start_date_edit.setPlaceholderText("01/2010")
        self.start_date_edit.setValidator(QRegExpValidator(QRegExp(r"(0[1-9]|1[0-2])\/\d{4}")))
        self.layout.addWidget(self.start_date_edit)

        # Label and input field for end date
        self.layout.addWidget(QLabel('Data final:'))
        self.end_date_edit = QLineEdit()
        self.end_date_edit.setPlaceholderText("12/2023")
        self.end_date_edit.setValidator(QRegExpValidator(QRegExp(r"(0[1-9]|1[0-2])\/\d{4}")))
        self.layout.addWidget(self.end_date_edit)
        self.setDefaultDateRange()

        # Label and ComboBox for state filter
        self.layout.addWidget(QLabel('Selecione os Estados:'))
        self.scroll_area = QScrollArea(self)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        states = ['Todos', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        self.checkboxes = []

        for state in states:
            checkbox = QCheckBox(state, self.scroll_widget)
            self.scroll_layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)

        self.all_checkbox = next((cb for cb in self.checkboxes if cb.text() == 'Todos'), None)
        self.all_checkbox.setChecked(True)
        self.all_checkbox.stateChanged.connect(self.handleAllCheckbox)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        for checkbox in self.checkboxes:
            if checkbox.text() != 'Todos':
                checkbox.stateChanged.connect(self.handleStateCheckboxes)

        # Apply Filters Button
        self.apply_button = QPushButton('Aplicar filtros')
        self.apply_button.clicked.connect(self.applyFilters)
        self.layout.addWidget(self.apply_button)

    def setDefaultDateRange(self):
        # Load initial data and set the earliest and latest date
        initial_data = self.controller.get_initial_data()
        min_date_str = initial_data.index.min()
        max_date_str = initial_data.index.max()
        self.start_date_edit.setText(self.formatDate(min_date_str))
        self.end_date_edit.setText(self.formatDate(max_date_str))

    def formatDate(self, date_str):
        year, month = date_str.split('-')
        return f"{month}/{year}"

    def applyFilters(self):
        # Emit the signal with filter values
        start_date_str = self.start_date_edit.text()
        end_date_str = self.end_date_edit.text()

        # Check if the dates are in the correct format
        if re.match(r"(0[1-9]|1[0-2])\/\d{4}", start_date_str) and re.match(r"(0[1-9]|1[0-2])\/\d{4}", end_date_str):
            self.filtersApplied.emit(start_date_str, end_date_str, self.getSelectedStates())
        else:
            print("Incorrect date format")

    def getSelectedStates(self):
        selected_states = []
        if self.all_checkbox and self.all_checkbox.isChecked():
            return selected_states

        for checkbox in self.checkboxes:
            if checkbox.isChecked() and checkbox.text() != 'Todos':
                selected_states.append(checkbox.text())
        return selected_states

    def handleAllCheckbox(self, state):
        if state == Qt.Checked:
            for checkbox in self.checkboxes:
                if checkbox.text() != 'Todos':
                    checkbox.setChecked(False)

    def handleStateCheckboxes(self, state):
        if state == Qt.Checked:
            self.all_checkbox.setChecked(False)
        elif all(not cb.isChecked() for cb in self.checkboxes if cb.text() != 'Todos'):
            self.all_checkbox.setChecked(True)
