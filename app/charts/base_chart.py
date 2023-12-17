from abc import abstractmethod
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class BaseChart(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self._width = width
        self._height = height
        self._dpi = dpi
        self._figure = Figure(figsize=(self._width, self._height), dpi=self._dpi)
        super().__init__(self._figure)
        self.setParent(parent)
        self.axes = self._figure.add_subplot(*[1, 1, 1])
        
    @abstractmethod
    def configure_plot(self):
        # This method should contain specific plot configuration in subclasses
        pass
