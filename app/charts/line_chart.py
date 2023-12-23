import matplotlib.ticker as ticker
from utils.chart_utils import calculate_spacing
from charts.base_chart import BaseChart
from exceptions.chart_exceptions import ChartError

class LineChart(BaseChart):
    def __init__(self, parent=None, width=5, height=4, dpi=100, dataframe=None,
                 title='Chart', xlabel='X-axis', ylabel='Y-axis', color_map=None):
        super().__init__(parent, width, height, dpi)
        self.dataframe = dataframe
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.color_map = color_map if color_map is not None else {}

        if self.dataframe is not None:
            self.configure_plot()
        else:
            raise ChartError("Failed to initialize LineChart: 'dataframe' not provided or invalid.")

    def configure_plot(self):
        self.validate_dataframe()
        self.plot_data()
        self.configure_legend()
        self.axes.set_title(self.title)
        self.axes.set_ylabel(self.ylabel)
        self.axes.grid(which='major', axis='y', linestyle='--')
        self._figure.subplots_adjust(bottom=0.3)
        self.axes.set_xticklabels(self.dataframe.index, rotation=45, ha='right', fontsize=8)

    def plot_data(self):
        for column in self.dataframe.columns:
            color = self.color_map.get(column, None)
            self.axes.plot(self.dataframe.index, self.dataframe[column], label=column, color=color)

        max_value = self.dataframe.max().max()
        spacing = calculate_spacing(max_value)
        self.axes.yaxis.set_major_locator(ticker.MultipleLocator(spacing))
        self.axes.set_xticks(range(len(self.dataframe.index)))
