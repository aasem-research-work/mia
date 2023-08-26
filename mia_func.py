from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QAction
from PyQt5.QtGui import QPixmap, QImage
import pydicom
import numpy as np

def show_todo_message():
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Information)
    msg.setText("To-Do: This function is not yet implemented.")
    msg.setWindowTitle("To-Do")
    msg.exec_()

def add_menu_item(main_window, menu, title, action_function):
    action_item = QAction(title, main_window)
    action_item.triggered.connect(action_function)
    menu.addAction(action_item)
    return action_item

def open_image(main_window, image_type):
    options = QFileDialog.Options()
    file_path, _ = QFileDialog.getOpenFileName(main_window, f"Open {image_type} Image", "", "Images (*.png *.jpg *.jpeg *.bmp *.gif *.dcm)", options=options)
    
    if file_path:
        file_name = file_path.split("/")[-1]
        if file_path.lower().endswith('.dcm'):
            dicom_file = pydicom.dcmread(file_path)
            image_data = dicom_file.pixel_array
            image_data = np.uint8((image_data / image_data.max()) * 255)  # Normalize the data
            qimage = QImage(image_data, image_data.shape[1], image_data.shape[0], QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(qimage)
        else:
            pixmap = QPixmap(file_path)
        main_window.image_label.setPixmap(pixmap)
        main_window.image_label.setAlignment(Qt.AlignCenter)
        main_window.image_dict[file_name] = pixmap
