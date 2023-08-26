
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QMenuBar, QAction, QLabel, QVBoxLayout, QWidget, QToolBar
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import sys
from mia_func import show_todo_message, add_menu_item, open_image

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.image_dict = {}  # Dictionary to hold image data

        self.setWindowTitle("Mia: Medical Image Analysis:")
        self.setGeometry(100, 100, 800, 600)

        # Create menu bar
        menu_bar = QMenuBar(self)
        self.setMenuBar(menu_bar)

        # Disable native menu bar on macOS to make it visible within the window
        menu_bar.setNativeMenuBar(False)

        # Create File menu and its items
        file_menu = menu_bar.addMenu("File")
        self.open_mri_action = add_menu_item(self, file_menu, "Open MRI", self.open_mri)
        self.open_xray_action = add_menu_item(self, file_menu, "Open X-Ray", self.open_xray)
        self.save_images_action = add_menu_item(self, file_menu, "Save Images", show_todo_message)
        self.print_images_action = add_menu_item(self, file_menu, "Print Images", show_todo_message)
        self.exit_app_action = add_menu_item(self, file_menu, "Exit", self.exit_app)

        # Create Edit menu and its items
        edit_menu = menu_bar.addMenu("Edit")
        self.draw_arrows_action = add_menu_item(self, edit_menu, "Draw Arrows", show_todo_message)
        self.overlay_images_action = add_menu_item(self, edit_menu, "Overlay Images", show_todo_message)
        self.edit_overlay_action = add_menu_item(self, edit_menu, "Edit Overlay", show_todo_message)
        self.erase_overlay_action = add_menu_item(self, edit_menu, "Erase Overlay", show_todo_message)

        # Create a toolbar and add grouped menu items
        toolbar = QToolBar("Main Toolbar")
        self.addToolBar(toolbar)
        
        # Add File menu items to the toolbar
        file_group = QAction(QIcon(), "File Operations", self)
        toolbar.addAction(file_group)
        toolbar.addSeparator()
        toolbar.addAction(self.open_mri_action)
        toolbar.addAction(self.open_xray_action)
        toolbar.addAction(self.save_images_action)
        toolbar.addAction(self.print_images_action)
        toolbar.addAction(self.exit_app_action)
        toolbar.addSeparator()
        
        # Add Edit menu items to the toolbar
        edit_group = QAction(QIcon(), "Edit Operations", self)
        toolbar.addAction(edit_group)
        toolbar.addSeparator()
        toolbar.addAction(self.draw_arrows_action)
        toolbar.addAction(self.overlay_images_action)
        toolbar.addAction(self.edit_overlay_action)
        toolbar.addAction(self.erase_overlay_action)

        # Create a QLabel to display the image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Use a layout to include the QLabel
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def open_mri(self):
        open_image(self, "MRI")

    def open_xray(self):
        open_image(self, "X-Ray")

    def exit_app(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec_())
