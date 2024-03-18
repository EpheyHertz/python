#imports
import os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QFileDialog, QListWidget, QComboBox, QHBoxLayout, QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PIL import Image, ImageFilter, ImageEnhance

app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("imagify app")
main_window.resize(800,600)
#all widgets
btn_folder = QPushButton("Folder")
file_list = QListWidget()
 
btn_left = QPushButton("Left")
btn_right = QPushButton("Right")
mirror =  QPushButton("Mirror")
sharpness =  QPushButton("Sharpness")
gray =  QPushButton("B/W")
saturaton =  QPushButton("Colour Depth")
contrast =  QPushButton("Contrast")
blur =  QPushButton("Blur")

#drop downlist
filter_box = QComboBox()
filter_box.addItem("Original")
filter_box.addItem("Left")
filter_box.addItem("Right")
filter_box.addItem("Mirror")
filter_box.addItem("Sharpness")
filter_box.addItem("B/W")
filter_box.addItem("Colour Depth")
filter_box.addItem("Contrast")
filter_box.addItem("Blur")

picture_box = QLabel("Image will appear here")

#App design
master_layout = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()


col1.addWidget(btn_folder)
col1.addWidget(file_list)
col1.addWidget(filter_box)
col1.addWidget(btn_left)
col1.addWidget(btn_right)
col1.addWidget(mirror)
col1.addWidget(sharpness)
col1.addWidget(gray)
col1.addWidget(saturaton)
col1.addWidget(contrast)
col1.addWidget(blur)

#add picture holder
col2.addWidget(picture_box)


master_layout.addLayout(col1,20)
master_layout.addLayout(col2,80)
main_window.setLayout(master_layout)
#all the functionalites
working_directory = ""

#filter files and etensions
def filter(files,extensions):
    results = []
    for file in files:
        for extension in extensions:
            if file.endswith(extension):
                results.append(file)
    return results

#choose current work directory
def getWorkDirectory():
    global working_directory
    working_directory = QFileDialog.getExistingDirectory()
    extensions = [".jpg",".jpeg",".png",".svg"]
    filenames = filter(os.listdir(working_directory),extensions)
    file_list.clear()
    for filename in filenames:
        file_list.addItem(filename)


class Editor():
    def __init__(self):
        self.image = None
        self.original =None
        self.filename =None
        self.save_folder = "edits/"
    def load_image(self,filename):
        self.filename = filename
        fullname = os.path.join(working_directory,self.filename)
        self.image = Image.open(fullname)
        self.original = self.image.copy()

    def save_image(self):
        path = os.path.join(working_directory,self.save_folder)
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path)

        fullname = os.path.join(path,self.filename)
        self.image.save(fullname)

    def show_image(self,path):
        picture_box.hide()
        image= QPixmap(path)
        w, h = picture_box.width(), picture_box.height()
        image = image.scaled(w,h, Qt.KeepAspectRatio)
        picture_box.setPixmap(image)
        picture_box.show()

    def gray(self):
        self.image = self.image.convert("L")
        self.save_image()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)

    def left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.save_image()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)

    def right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.save_image()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)

    def mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        self.save_image()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)

    def sharpness(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        self.save_image()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)
    
    def saturation(self):
        self.image = ImageEnhance.Color(self.image).enhance(1.7)
        self.save_image()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)

    def contrast(self):
        self.image = ImageEnhance.Contrast(self.image).enhance(1.5)
        self.save_image()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)

    def blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)
        self.save_image()
        image_path=os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)

    def filter_apply(self,filter_type):
        if filter_type == "Original":
            self.image = self.original.copy()
        else:
            advance = {
                "Left":lambda image:image.transpose(Image.ROTATE_90),
                "Right": lambda image :image.transpose(Image.ROTATE_270),
                "Mirror": lambda image:image.transpose(Image.FLIP_LEFT_RIGHT),
                "Sharpness": lambda image:image.filter(ImageFilter.SHARPEN),
                "B/W" : lambda image:image.convert("L"),
                "Colour Depth" : lambda image:ImageEnhance.Color(image).enhance(1.7),
                "Contrast" : lambda image:ImageEnhance.Contrast(image).enhance(1.5),
                "Blur" : lambda image:image.filter(ImageFilter.BLUR)
            }
            filter_function = advance.get(filter_type)
            if filter_function:
                self.image = filter_function(self.image)
                self.save_image()
                image_path = os.path.join(working_directory,self.save_folder,self.filename)
                self.show_image(image_path)
            pass
        self.save_image()
        image_path = os.path.join(working_directory,self.save_folder,self.filename)
        self.show_image(image_path)

def handle_filter():
    if file_list.currentRow() >= 0:
        select_filter = filter_box.currentText()
        main.filter_apply(select_filter)
    

def displayImage():
    if file_list.currentRow() >= 0:
        filename = file_list.currentItem().text()
        main.load_image(filename)
        main.show_image(os.path.join(working_directory, main.filename))




main = Editor()


btn_folder.clicked.connect(getWorkDirectory)
file_list.currentRowChanged.connect(displayImage)
filter_box.currentTextChanged.connect(handle_filter)

gray.clicked.connect(main.gray)
btn_left.clicked.connect(main.left)
btn_right.clicked.connect(main.right)
mirror.clicked.connect(main.mirror)
sharpness.clicked.connect(main.sharpness)
saturaton.clicked.connect(main.saturation)
contrast.clicked.connect(main.contrast)
blur.clicked.connect(main.blur)
main_window.show()
app.exec()



