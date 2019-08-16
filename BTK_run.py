import sys
import os
import time
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow,QMessageBox,QFileDialog, QGraphicsPixmapItem ,QGraphicsScene
from modules.MainWindow import *
from modules.run_parameter import run_parameter

class MyWindow(QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.cwd = os.getcwd()
        self.image = QPixmap()
        self.run.clicked.connect(self.run_event)  # 绑定登陆函数
        self.add_file.clicked.connect(self.add_file_event)

    #添加文件
    def add_file_event(self):
        fileName1, filetype = QFileDialog.getOpenFileName(self,"选取文件", self.cwd ,"All Files (*);;Text Files (*.txt)")  # 设置文件扩展名过滤,
        # 注意用双分号间隔
        if len(fileName1) == 0:
            return 
        #fileName1 = fileName1.replace('/', "\\")#win下需要进行文件分隔符转换
        self.datafilenames = fileName1
        self.FileName.clear()
        self.FileName.append(fileName1)#读取excel的内容，返回是一个字典列表

    #会话窗提醒，数据读取成功
    
    # 登陆函数
    def run_event(self):
        if self.DeltaEdit_low.text() == "":
            QMessageBox.about(self, 'Parameter Error!', 'Please input lower bound of Delta!')
        elif self.DeltaEdit_high.text() == "":
            QMessageBox.about(self, 'Parameter Error!', 'Please input higher bound of Delta!')
        elif self.GamaEdit_high.text() == "":
            QMessageBox.about(self, 'Parameter Error!', 'Please input higher bound of Gama!')
        elif self.GamaEdit_low.text() == "":
            QMessageBox.about(self, 'Parameter Error!', 'Please input lower bound of Gama!')
        elif self.ZEdit_high.text() == "":
            QMessageBox.about(self, 'Parameter Error!', 'Please input higher bound of Z!')
        elif self.ZEdit_low.text() == "":
            QMessageBox.about(self, 'Parameter Error!', 'Please input lower bound of Z!') 
        elif self.PEdit_high.text() == "":
            QMessageBox.about(self, 'Parameter Error!', 'Please input higher bound of spin polarization!')
        elif self.PEdit_low.text() == "":
            QMessageBox.about(self, 'Parameter Error!', 'Please input lower bound of spin polarization!') 
        elif self.TempEdit.text() == "":
            QMessageBox.about(self, 'Parameter Error!', 'Please input temperature!') 
        elif len(self.FileName.toPlainText()) == 0 :
            QMessageBox.about(self, 'Parameter Error!', 'Please input file!') 
        else:
            Ts = [float(self.TempEdit.text())]
            Delta_low  = float(self.DeltaEdit_low.text()) 
            Delta_high  = float(self.DeltaEdit_high.text()) 
            Gama_low  = float(self.GamaEdit_low.text()) 
            Gama_high  = float(self.GamaEdit_high.text()) 
            Z_low  = float(self.ZEdit_low.text()) 
            Z_high  = float(self.ZEdit_high.text()) 
            P_low  = float(self.PEdit_low.text())
            P_high  = float(self.PEdit_high.text())  
            bound = [[(Delta_low,Delta_high),(Gama_low,Gama_high),(Z_low,Z_high),(P_low,P_high)]]
            filenames = [self.datafilenames.replace('/', " ").split()[-1]]
            print(filenames)
            run_parameter(filenames,Ts,bound)
            self.image.load(self.datafilenames.replace('.csv', ".png"))
            self.LoadImage()


    def LoadImage(self):
        self.graphicsView.scene = QGraphicsScene()            # 创建一个图片元素的对象
        item = QGraphicsPixmapItem(self.image)                # 创建一个变量用于承载加载后的图片
        self.graphicsView.scene.addItem(item)                 # 将加载后的图片传递给scene对象
        self.graphicsView.setScene(self.graphicsView.scene)   
          

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())