from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QFileDialog, QLabel, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Medical Image Processing Software")
        self.setGeometry(100, 100, 800, 600)

        # Create menu bar
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)
        file_menu = menu_bar.addMenu("File")

        # Disable native menu bar on macOS to make it visible within the window
        menu_bar.setNativeMenuBar(False)

        # Create menu items
        browse_action = QAction("Browse", self)
        browse_action.triggered.connect(self.browse_image)
        file_menu.addAction(browse_action)

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.exit_app)
        file_menu.addAction(exit_action)

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Use a layout to include the QLabel
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def browse_image(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image File", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif)", options=options)
        
        if file_path:
            pixmap = QPixmap(file_path)
            self.image_label.setPixmap(pixmap)
            self.image_label.setAlignment(Qt.AlignCenter)

    def exit_app(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
