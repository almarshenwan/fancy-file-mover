import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QFileDialog, QVBoxLayout,
    QLabel, QPushButton, QTextEdit, QCheckBox, QHBoxLayout
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QPalette, QColor


class FileMoverGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fancy File Mover 🗂️")
        self.setMinimumSize(600, 400)
        self.set_dark_mode()

        # Layouts
        layout = QVBoxLayout()

        # Folder selectors
        self.sourceLabel = QLabel("Source Folder: Not selected")
        self.destLabel = QLabel("Destination Folder: Not selected")
        btnSource = QPushButton("Select Source")
        btnDest = QPushButton("Select Destination")
        btnSource.clicked.connect(self.select_source)
        btnDest.clicked.connect(self.select_dest)

        # Toggles
        self.dryRunCheck = QCheckBox("Dry Run")
        self.copyCheck = QCheckBox("Copy Instead of Move")
        self.renameCheck = QCheckBox("Rename on Conflict")
        self.dryRunCheck.setChecked(True)

        toggleLayout = QHBoxLayout()
        toggleLayout.addWidget(self.dryRunCheck)
        toggleLayout.addWidget(self.copyCheck)
        toggleLayout.addWidget(self.renameCheck)

        # Run button
        runButton = QPushButton("Run")
        runButton.clicked.connect(self.run_script)

        # Log output
        self.logOutput = QTextEdit()
        self.logOutput.setReadOnly(True)
        self.logOutput.setFont(QFont("Consolas", 10))

        # Add widgets to layout
        layout.addWidget(btnSource)
        layout.addWidget(self.sourceLabel)
        layout.addWidget(btnDest)
        layout.addWidget(self.destLabel)
        layout.addLayout(toggleLayout)
        layout.addWidget(runButton)
        layout.addWidget(QLabel("Log Output:"))
        layout.addWidget(self.logOutput)

        self.setLayout(layout)

    def select_source(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Source Folder")
        if folder:
            self.sourceLabel.setText(f"Source Folder: {folder}")
            self.sourcePath = folder

    def select_dest(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Destination Folder")
        if folder:
            self.destLabel.setText(f"Destination Folder: {folder}")
            self.destPath = folder

    def run_script(self):
        self.logOutput.append("▶️ Running script...")
        self.logOutput.append(f"Dry Run: {self.dryRunCheck.isChecked()}")
        self.logOutput.append(f"Copy: {self.copyCheck.isChecked()}")
        self.logOutput.append(f"Rename on Conflict: {self.renameCheck.isChecked()}")

        # Placeholder
        self.logOutput.append("🚧 (File operation logic coming next!)")

    def set_dark_mode(self):
        app_palette = QPalette()
        app_palette.setColor(QPalette.Window, QColor(30, 30, 30))
        app_palette.setColor(QPalette.WindowText, Qt.white)
        app_palette.setColor(QPalette.Base, QColor(45, 45, 45))
        app_palette.setColor(QPalette.Text, Qt.white)
        app_palette.setColor(QPalette.Button, QColor(50, 50, 50))
        app_palette.setColor(QPalette.ButtonText, Qt.white)
        app_palette.setColor(QPalette.Highlight, QColor(38, 79, 120))
        app_palette.setColor(QPalette.HighlightedText, Qt.white)
        self.setPalette(app_palette)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileMoverGUI()
    window.show()
    sys.exit(app.exec())
