import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, QSize

class BrasilMapWidget(QWidget):
    def __init__(self, parent=None):
        super(BrasilMapWidget, self).__init__(parent)
        layout = QVBoxLayout()
        self.browser = QWebEngineView()
        self.setMaximumSize(QSize(800, 850))
        self.setMinimumSize(QSize(600, 650))
        
        # Obtém o diretório atual do arquivo Python
        current_dir = os.path.dirname(os.path.abspath(__file__))
        
        # Constrói o caminho relativo ao arquivo HTML
        html_file_path = os.path.join(current_dir, "brasil_map_resources/brasil_map.html")
        
        self.browser.setUrl(QUrl.fromLocalFile(html_file_path))
        layout.addWidget(self.browser)
        self.setLayout(layout)