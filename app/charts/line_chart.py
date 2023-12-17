import pandas as pd
import matplotlib.ticker as ticker
from charts.base_chart import BaseChart
from utils.chart_utils import calculate_spacing
from exceptions.chart_exceptions import ChartError

class LineChart(BaseChart):
    """Line chart plotting class."""

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
            raise ChartError("Failed to initialize LineChart: 'dataframe' not provided or invalid. Ensure that a valid pandas DataFrame is passed as an argument.")
        
    def configure_plot(self):
        self.validate_dataframe()
        self.plot_data()
        self.configure_legend()
        self.axes.set_title(self.title)
        self.axes.set_ylabel(self.ylabel)
        self.axes.grid(which='major', axis='y', linestyle='--')
        self.figure.subplots_adjust(bottom=0.3)
        self.axes.set_xticklabels(self.dataframe.index, rotation=45, ha='right', fontsize=8)

    def validate_dataframe(self):
        if not isinstance(self.dataframe, pd.DataFrame):
            raise ChartError("The provided data is not a pandas DataFrame.")
    
    def configure_legend(self, loc='upper center', bbox_anchor=(0.5, -0.2), frame_on=False):
        self.axes.legend(
            loc=loc,
            bbox_to_anchor=bbox_anchor,
            fancybox=True, 
            shadow=True, 
            ncol=len(self.dataframe.columns),
            frameon=frame_on
        )
        
    def plot_data(self):
        for column in self.dataframe.columns:
            color = self.color_map.get(column, None)
            self.axes.plot(self.dataframe.index, self.dataframe[column], label=column, color=color)

        valor_maximo = self.dataframe.max().max()
        espacamento_grade = calculate_spacing(valor_maximo)
        self.axes.yaxis.set_major_locator(ticker.MultipleLocator(espacamento_grade))

        self.axes.set_xticks(range(len(self.dataframe.index))) 
    
    def update_data(self, new_dataframe):
        self.axes.clear()
        self.dataframe = new_dataframe
        self.configure_plot()
        self.draw()

    def draw(self):
        super().draw()

