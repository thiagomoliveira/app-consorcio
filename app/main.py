import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QHBoxLayout
from data_operations.notification_data_operations import *
from controllers.notification_controller import NotificationController
from widgets.filtros_widget import FilterWidget
from widgets.brasil_map_widget import BrasilMapWidget
from widgets.notification_line_chart_widget import NotificationLineChartWidget

# Create the main application
app = QApplication(sys.argv)
app.setStyle('Fusion')  # Optional: Set the application style to Fusion

# Create a QMainWindow
window = QMainWindow()
window.setWindowTitle('Notification Dashboard')
window.setGeometry(100, 100, 1000, 800)

# Create a central widget to hold the main layout
central_widget = QWidget()
window.setCentralWidget(central_widget)

# Create a QVBoxLayout for the central widget
layout = QVBoxLayout(central_widget)

# Set up the data controller
data_path = os.path.join('data', 'mock_pre-ajuizamento.xlsx')
controller = NotificationController(data_path)

# Create a horizontal layout to hold the chart and map side by side
chart_map_layout = QHBoxLayout()

# Create the NotificationLineChartWidget and add it to the chart_map_layout
line_chart_widget = NotificationLineChartWidget(controller.get_initial_data())
chart_map_layout.addWidget(line_chart_widget)

# Create the BrasilMapWidget and add it to the chart_map_layout
brasil_map_widget = BrasilMapWidget(controller.get_aggregated_data_by_state())
chart_map_layout.addWidget(brasil_map_widget)

# Create the FilterWidget and add it to the main layout
filter_widget = FilterWidget(controller)
def update_chart(start_date, end_date, states):
    filtered_data = controller.get_aggregated_data_by_type_and_date(start_date, end_date, states)
    line_chart_widget.update_data(filtered_data)

filter_widget.filtersApplied.connect(update_chart)

layout.addWidget(filter_widget)

# Add the chart_map_layout (containing chart and map) to the main layout
layout.addLayout(chart_map_layout)

# Show the main window
window.show()

# Start the application event loop
sys.exit(app.exec_())
