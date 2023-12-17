from PyQt5.QtWidgets import QVBoxLayout, QWidget
from charts.line_chart import LineChart
from PyQt5.QtCore import QSize


class NotificationLineChartWidget(QWidget):
    def __init__(self, dataframe):
        super().__init__(parent = None)
        color_map = {
            'positiva': 'green',
            'negativa': 'red',
            'notificando': 'blue'
        }
        self.layout = QVBoxLayout(self)
        self.chart = LineChart(dataframe=dataframe, title="Notificações por Tipo",
                        xlabel="", ylabel="Quantidade", color_map=color_map)
        self.layout.addWidget(self.chart)
        self.setMaximumSize(QSize(800, 600))
        self.setMinimumSize(QSize(600, 450))
        self.chart.draw()
