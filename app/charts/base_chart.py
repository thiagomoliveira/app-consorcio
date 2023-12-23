from abc import abstractmethod
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
from exceptions.chart_exceptions import ChartError

class BaseChart(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self._width = width
        self._height = height
        self._dpi = dpi
        self._figure = Figure(figsize=(self._width, self._height), dpi=self._dpi)
        super().__init__(self._figure)
        self.setParent(parent)
        self.axes = self._figure.add_subplot(1, 1, 1)

    @abstractmethod
    def configure_plot(self):
        pass

    @abstractmethod
    def plot_data(self):
        pass

    def draw(self):
        super().draw()

    def update_data(self, new_dataframe):
        self.axes.clear()
        self.dataframe = new_dataframe
        self.configure_plot()
        self.draw()

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