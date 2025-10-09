from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

class HomePage(QWidget):
    def __init__(self, switch_page):
        super().__init__()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        title = QLabel("Generalized\nObservation and\nReflection\nPlatform\n")
        title.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(title)

        btn_new = QPushButton("Start New Observation")
        btn_view = QPushButton("View Observation Data")
        for b in (btn_new, btn_view):
            b.setFixedHeight(40)
            layout.addWidget(b)

        btn_new.clicked.connect(lambda: switch_page(1))
        btn_view.clicked.connect(lambda: switch_page(2))

        self.setLayout(layout)
