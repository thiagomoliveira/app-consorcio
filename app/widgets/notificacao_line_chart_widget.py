from PyQt5.QtWidgets import QVBoxLayout, QWidget
from charts.line_chart import LineChart

class NotificationLineChartWidget(QWidget):
    def __init__(self, dataframe):
        super().__init__(parent=None)
        self.color_map = {
            'positiva': 'green',
            'negativa': 'red',
            'total': 'blue'
        }
        self.layout = QVBoxLayout(self)
        self.chart = LineChart(dataframe=self.process_dataframe(dataframe),
                               title="Notificações por Tipo",
                               xlabel="", ylabel="Quantidade",
                               color_map=self.color_map)
        self.layout.addWidget(self.chart)
        self.chart.draw()

    def process_dataframe(self, dataframe):
        if 'notificando' in dataframe.columns:
            dataframe = dataframe.drop(columns=['notificando'])
        return dataframe

    def update_data(self, new_dataframe):
        processed_dataframe = self.process_dataframe(new_dataframe)
        self.chart.update_data(processed_dataframe)
