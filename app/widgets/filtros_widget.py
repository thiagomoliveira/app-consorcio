from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QScrollArea, QCheckBox
from PyQt5.QtCore import pyqtSignal, QRegExp, Qt, QSize
from PyQt5.QtGui import QRegExpValidator
import re

class FiltroWidget(QWidget):
    # Sinal que será emitido quando os filtros forem aplicados
    filtrosAplicados = pyqtSignal(str, str, list)

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout(self)
        self.setMaximumSize(QSize(200, 600))
        self.setMinimumSize(QSize(200, 450))

        # Label e campo de entrada para a data de início
        self.layout.addWidget(QLabel('Data de Início:'))
        self.data_inicio_edit = QLineEdit()
        self.data_inicio_edit.setPlaceholderText("01/2010")
        self.data_inicio_edit.setValidator(QRegExpValidator(QRegExp(r"(0[1-9]|1[0-2])\/\d{4}")))
        self.layout.addWidget(self.data_inicio_edit)

        # Label e campo de entrada para a data final
        self.layout.addWidget(QLabel('Data Final:'))
        self.data_final_edit = QLineEdit()
        self.data_final_edit.setPlaceholderText("12/2020")
        self.data_final_edit.setValidator(QRegExpValidator(QRegExp(r"(0[1-9]|1[0-2])\/\d{4}")))
        self.layout.addWidget(self.data_final_edit)
        self.setDefaultDateRange()

        # Label e ComboBox para o filtro de UF
        self.layout.addWidget(QLabel('Selecione as UFs:'))
        self.scroll_area = QScrollArea(self)
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        ufs = ['Todos', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
        self.checkboxes = []

        for uf in ufs:
            checkbox = QCheckBox(uf, self.scroll_widget)
            self.scroll_layout.addWidget(checkbox)
            self.checkboxes.append(checkbox)

        self.todos_checkbox = next((cb for cb in self.checkboxes if cb.text() == 'Todos'), None)
        self.todos_checkbox.setChecked(True)
        self.todos_checkbox.stateChanged.connect(self.handleTodosCheckbox)
        self.scroll_widget.setLayout(self.scroll_layout)
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_area.setWidgetResizable(True)
        self.layout.addWidget(self.scroll_area)

        for checkbox in self.checkboxes:
            if checkbox.text() != 'Todos':
                checkbox.stateChanged.connect(self.handleStateCheckboxes)

        # Botão de Aplicar Filtros
        self.btn_aplicar = QPushButton('Aplicar Filtros')
        self.btn_aplicar.clicked.connect(self.aplicarFiltros)
        self.layout.addWidget(self.btn_aplicar)

    def setDefaultDateRange(self):
        # Carrega os dados iniciais e define a data mais antiga e mais recente
        initial_data = self.controller.get_initial_data()
        min_date_str = initial_data.index.min()
        max_date_str = initial_data.index.max()
        self.data_inicio_edit.setText(self.format_date(min_date_str))
        self.data_final_edit.setText(self.format_date(max_date_str))

    def format_date(self, date_str):
        year, month = date_str.split('-')
        return f"{month}/{year}"

    def aplicarFiltros(self):
        # Emite o sinal com os valores dos filtros
        data_inicio_str = self.data_inicio_edit.text()
        data_final_str = self.data_final_edit.text()

        # Verifica se as datas estão no formato correto
        if re.match(r"(0[1-9]|1[0-2])\/\d{4}", data_inicio_str) and re.match(r"(0[1-9]|1[0-2])\/\d{4}", data_final_str):
            self.filtrosAplicados.emit(data_inicio_str, data_final_str, self.getSelectedUFs())
        else:
            print("Datas em formato incorreto")

 

    def getSelectedUFs(self):
        ufs_selecionadas = []
        if self.todos_checkbox and self.todos_checkbox.isChecked():
            return ufs_selecionadas

        for checkbox in self.checkboxes:
            if checkbox.isChecked() and checkbox.text() != 'Todos':
                ufs_selecionadas.append(checkbox.text())
        return ufs_selecionadas

 

    def handleTodosCheckbox(self, state):
        if state == Qt.Checked:
            for checkbox in self.checkboxes:
                if checkbox.text() != 'Todos':
                    checkbox.setChecked(False)

    def handleStateCheckboxes(self, state):
        if state == Qt.Checked:
            self.todos_checkbox.setChecked(False)
        elif all(not cb.isChecked() for cb in self.checkboxes if cb.text() != 'Todos'):
            self.todos_checkbox.setChecked(True)