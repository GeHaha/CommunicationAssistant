# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 20:37:48 2018

@author: Administrator
"""

import sys
import serial
import threading
import binascii 
from PyQt5 import QtCore, QtGui, QtWidgets
import serial.tools.list_ports
from PyQt5.QtWidgets import QFileDialog ,QDialog,QWidget
 

import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.patches import Circle
import time
import math

import socket



class Ui_MainWindow(QWidget):
    
    ser = serial.Serial()
    
    def setupUi(self, MainWindow):
        #串口助手界面
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 141, 500))
        self.groupBox.setObjectName("groupBox")
        
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 31, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 41, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 80, 41, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 140, 41, 16))
        self.label_5.setObjectName("label_5")
        
        #端口
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 330, 41, 16))
        self.label_6.setObjectName("label_6")
        
        #模式
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 360, 41, 16))
        self.label_7.setObjectName("label_7")
        
        #IP地址
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 390, 41, 16))
        self.label_8.setObjectName("label_8")
        
        #端口号
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 415, 41, 16))
        self.label_9.setObjectName("label_9")
        
        
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_4.setGeometry(QtCore.QRect(60, 20, 71, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        
        
        #端口
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_5.setGeometry(QtCore.QRect(60, 330, 71, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        
        #模式
        self.comboBox_6 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_6.setGeometry(QtCore.QRect(60, 360, 71, 22))
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")


       #数据位
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(60, 80, 71, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        #更改波特率
        self.comboBox_1 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_1.setGeometry(QtCore.QRect(60, 50, 71, 22))
        self.comboBox_1.setObjectName("comboBox_1")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        self.comboBox_1.addItem("")
        
        #校验位
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 110, 71, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        
        #停止位
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_3.setGeometry(QtCore.QRect(60, 140, 71, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        #打开
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 240, 51, 23))
        self.pushButton.setObjectName("pushButton")
        
        #关闭
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 240, 51, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        
        #打开文件
        self.pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 280, 58, 23))
        self.pushButton_7.setObjectName("pushButton_7")
        
       
        #发送文件
        self.pushButton_8 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_8.setGeometry(QtCore.QRect(80, 280, 58, 23))
        self.pushButton_8.setObjectName("pushButton_8")
       
        
        #检测串口
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 200, 61, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        
        
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 170, 41, 16))
        self.label_11.setObjectName("label_11")
        
        
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(70, 170, 54, 16))
        font = QtGui.QFont()
        font.setFamily("Aharoni")
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        
        #接收区
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(160, 10, 411, 181))
        self.groupBox_2.setObjectName("groupBox_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox_2)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 391, 151))
        self.textBrowser.setObjectName("textBrowser")
        
        #发送区
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 200, 261, 121))
        self.groupBox_3.setObjectName("groupBox_3")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 241, 91))
        self.textEdit.setObjectName("textEdit")
        
        #IP地址
        self.textEdit_1 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_1.setGeometry(QtCore.QRect(60, 390, 75, 24))
        self.textEdit_1.setObjectName("textEdit_1")
        
        
        #端口号
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(60, 415, 75, 24))
        self.textEdit_2.setObjectName("textEdit_2")
        
        
        #Hex显示
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(430, 210, 61, 16))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(500, 210, 61, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        
        #清除
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(430, 240, 61, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        
        #发送
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(430, 280, 61, 23))
        self.pushButton_5.setObjectName("pushButton_5")
        
        #离线读取数据得出图像
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(510, 280, 61, 23))
        self.pushButton_9.setObjectName("pushButton_5")
        
        
        #新加pushButton_6是显示按钮，弹出实时图像
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 240, 61, 23))
        self.pushButton_6.setObjectName("pushButton_6")
        
        #连接服务器 
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(190, 330, 73, 23))
        self.pushButton_10.setObjectName("pushButton_6")
        
        #关闭连接
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(300, 330, 73, 23))
        self.pushButton_11.setObjectName("pushButton_6")
       
      
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 579, 23))
        self.menubar.setObjectName("menubar")
    
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        MainWindow.setFixedSize(MainWindow.width(), MainWindow.height());  
        self.retranslateUi(MainWindow) 
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        #串口界面设置
        MainWindow.setWindowTitle(_translate("MainWindow", "Serial_tcp"))
        self.groupBox.setTitle(_translate("MainWindow", "串口设置"))
        
        self.label.setText(_translate("MainWindow", "串 口"))
        self.label_2.setText(_translate("MainWindow", "波特率"))
        self.label_3.setText(_translate("MainWindow", "校验位"))
        self.label_4.setText(_translate("MainWindow", "数据位"))
        self.label_5.setText(_translate("MainWindow", "停止位"))
                    
        #数据位
        self.comboBox.setItemText(0, _translate("MainWindow", "8"))
        self.comboBox.setItemText(1, _translate("MainWindow", "7"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6"))
        self.comboBox.setItemText(3, _translate("MainWindow", "5"))
         
        #增加的波特率
        self.comboBox_1.setItemText(0, _translate("MainWindow", "9600"))
        self.comboBox_1.setItemText(1, _translate("MainWindow", "14400"))
        self.comboBox_1.setItemText(2, _translate("MainWindow", "19200"))
        self.comboBox_1.setItemText(3, _translate("MainWindow", "38400"))
        self.comboBox_1.setItemText(4, _translate("MainWindow", "56000"))
        self.comboBox_1.setItemText(5, _translate("MainWindow", "57600"))
        self.comboBox_1.setItemText(6, _translate("MainWindow", "115200"))
        self.comboBox_1.setItemText(7, _translate("MainWindow", "128000"))
            
        #校验位
        self.comboBox_2.setItemText(0, _translate("MainWindow", "N"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "E"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "O"))
        self.comboBox_2.setItemText(3, _translate("MainWindow", "M"))
        self.comboBox_2.setItemText(4, _translate("MainWindow", "S"))
        
        #停止位
        self.comboBox_3.setItemText(0, _translate("MainWindow", "1"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "1.5"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "2"))
        
        #串口号
        self.comboBox_4.setItemText(0, _translate("MainWindow", "COM1"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "COM2"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "COM3"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "COM4"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "COM5"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "COM6"))
        self.comboBox_4.setItemText(6, _translate("MainWindow", "COM7"))
        self.comboBox_4.setItemText(7, _translate("MainWindow", "COM8"))
        self.comboBox_4.setItemText(8, _translate("MainWindow", "COM9"))
        self.comboBox_4.setItemText(9, _translate("MainWindow", "COM10"))
        
        #端口
        self.comboBox_5.setItemText(0, _translate("MainWindow", "TCP"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "UDP"))
        
        #模式
        self.comboBox_6.setItemText(0, _translate("MainWindow", "TCP Server"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "TCP Client"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "UDP Server"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "UDP Client"))
        
        #打开设置
        self.pushButton.setText(_translate("MainWindow", "打开"))
        self.pushButton.clicked.connect(self.port_open)
        
        #关闭设置
        self.pushButton_2.setText(_translate("MainWindow", "关闭"))
        self.pushButton_2.clicked.connect(self.port_close)
        
        #检测串口设置
        self.pushButton_3.setText(_translate("MainWindow", "检测串口"))
        self.pushButton_3.clicked.connect(self.port_cheak)
        
        
        #发送设置
        self.pushButton_5.setText(_translate("MainWindow", "发送"))
        self.pushButton_5.clicked.connect(self.send_data)
        
        #清除设置
        self.pushButton_4.setText(_translate("MainWindow", "清除"))
        self.pushButton_4.clicked.connect(self.clean_data)
            
         #显示实时图像
        self.pushButton_6.setText(_translate("MainWindow", "实时PID"))
        self.pushButton_6.clicked.connect(self.on_line)
        
        #离线读取数据画图
        self.pushButton_9.setText(_translate("MainWindow", "离线PID"))
        self.pushButton_9.clicked.connect(self.off_line)
           
        #打开文件
        self.pushButton_7.setText(_translate("MainWindow", "打开文件"))  
        self.pushButton_7.clicked.connect(self.open_file)
            
        #发送文件
        self.pushButton_8.setText(_translate("MainWindow", "发送文件"))   
        self.pushButton_8.clicked.connect(self.send_file)
              
        #各标签设置
        self.label_11.setText(_translate("MainWindow", "状 态："))
        self.label_12.setText(_translate("MainWindow", "串口状态"))
        self.groupBox_2.setTitle(_translate("MainWindow", "接收区"))
        self.groupBox_3.setTitle(_translate("MainWindow", "发送区"))
        self.checkBox.setText(_translate("MainWindow", "Hex显示"))
        self.checkBox_2.setText(_translate("MainWindow", "Hex发送"))
        
        #通讯设置     
        self.label_6.setText(_translate("MainWindow","端 口"))
        self.label_7.setText(_translate("MainWindow","模式"))
        self.label_8.setText(_translate("MainWindow","IP地址"))
        self.label_9.setText(_translate("MainWindow","端口号"))
        #ip地址
        self.textEdit_1.setText(_translate("MainWindow","127.0.0.1"))
        #端口号
        self.textEdit_2.setText(_translate("MainWindow","8888"))
        
        #连接服务器
        self.pushButton_10.setText(_translate("MainWindow", "连接服务器"))  
        self.pushButton_10.clicked.connect(self.connect_server)
        
        #关闭连接
        self.pushButton_11.setText(_translate("MainWindow", "关闭连接"))  
        #self.pushButton_11.clicked.connect(self.close_server)
    
    """
    def combobox_change(self):
        if self.comboBox_6.currentIndex() == 0 or self.comboBox_6.currentInd:
            self.
    """  
        
        
        
    
        
        
    #打开串口    
    def port_open(self):       
        self.ser.port = self.comboBox_4.currentText()
        self.ser.baudrate = self.comboBox_1.currentText()
        self.ser.bytesize = int(self.comboBox.currentText()) 
        self.ser.stopbits = int(self.comboBox_3.currentText())
        self.ser.parity = self.comboBox_2.currentText()
        self.ser.open()
        if(self.ser.isOpen()):
            self.pushButton.setEnabled(False) #打开不成功
            self.label_12.setText("打开成功")
            self.t1 = threading.Thread(target=self.receive_data)   #线程
            #isdaemon()判断
            self.t1.setDaemon(True) #daemon，用一个布尔值来判断一个布尔值，指示该线程是否是守护线程（True）或not（False）,setDaemon用于守护进程的旧的getter/setter API;直接使用它作为一个属性
            self.t1.start()
        else:
            self.label_12.setText("打开失败")
            
    #关闭串口
    def port_close(self):   
        self.ser.close()
        if(self.ser.isOpen()):
            self.label_12.setText("关闭失败")
        else:
            self.pushButton.setEnabled(True)
            self.label_12.setText("关闭成功")

    #发送数据
    def send_data(self):       
        if(self.ser.isOpen()):
            if(self.checkBox_2.isChecked()):
                 self.ser.write(binascii.a2b_hex(self.textEdit.toPlainText()))
            else:
                self.ser.write(self.textEdit.toPlainText().encode('utf-8'))
            self.label_12.setText("发送成功")
    #       self.ser.flushOutput()
        else:
            self.label_12.setText("发送失败")
            
    #接收数据
    def receive_data(self):
        print("The receive_data threading is start")
        res_data = '' 
        num = 0   #接收次数，初始为零，每接收一次增加一次
        while (self.ser.isOpen()):
            size = self.ser.inWaiting()  #获取接收缓存区的字数节
            if size:
                res_data = self.ser.read_all() #读取所以数据
                if(self.checkBox.isChecked()):  #检查是什么形式的数据
                    self.textBrowser.append(binascii.b2a_hex(res_data).decode())
                else:
                    self.textBrowser.append(res_data.decode())
                   
                #指读到textbrowser末尾
                self.textBrowser.moveCursor(QtGui.QTextCursor.End) #The QTextCursor class offers an API to access and modify QTextDocuments
                self.ser.flushInput()        #清空缓存区       
                num +=1
                self.label_12.setText("接收："+str(num))
    
    #清空数据
    def clean_data(self):
        self.textBrowser.setText("")
        self.label_12.setText("接收清空")
    
    #检查串口
    def port_cheak(self):
        Com_List=[]
        port_list = list(serial.tools.list_ports.comports())
        self.comboBox_4.clear()
        for port in port_list:
            Com_List.append(port[0])
            self.comboBox_4.addItem(port[0])
        if(len(Com_List) == 0):
            self.label_12.setText("没串口")
            
    #打开文件       
    def open_file(self):  
            filename = QFileDialog.getOpenFileName(self, "打开文件", "./", "All Files (*);;Text Files (*.)")   
            if filename[0]:
                f = open(filename[0],'r')         
                with f:
                    data = f.read()
                    self.textEdit.setText(data)
                    
    #发送文件    
    def send_file(self):
        if(self.ser.isOpen()):
            if(self.checkBox_2.isChecked()):
                 self.ser.write(binascii.a2b_hex(self.textEdit.toPlainText()))
            else:
                self.ser.write(self.textEdit.toPlainText().encode('utf-8'))
            self.label_12.setText("发送成功")
           #self.ser.flushOutput()         #清空缓存区
        else:
            self.label_12.setText("发送失败")

    #离线绘图
    def off_line(self):
        plt.rcParams['font.sans-serif']=['Simhei']  #显示中文字体
        plt.rcParams['axes.unicode_minus']=False    #显示负数
        plt.xlim(-10,250)  
        plt.ylim(-10,250)
        plt.title("PID实时数据图像")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.grid(True)
        plt.show()
        print('开始仿真')

    #读取文件
        path = "H:\PythonPort\串口\XY数据.txt"
        file = open(path,'r')

    #读取文件中的内容放到列表中
        X_list=[]; Y_list=[];
        try:
            for line in file.readlines():
                lineArr = line.strip().split()
                X_list.append(int(lineArr[0]))  #
                Y_list.append(int(lineArr[1]))    

            plt.plot(X_list,Y_list,'r',label='pid')
            plt.show() 
        except Exception as error:
            print(error)
            

   #实时绘图     
    def on_line(self):
        
        plt.rcParams['font.sans-serif']=['Simhei']  #显示中文字体
        plt.rcParams['axes.unicode_minus']=False    #显示负数
        plt.ion()   #开启interactive mode 成功的关键函数
        plt.xlabel("时间轴")
        plt.ylabel("PID变化")
        plt.grid(True) #添加网格       
        plt.ylim(-300,300)
        plt.pause(1)  #停顿间隔1秒 
        X_list= []
        x = np.linspace(0,1000,num=5000)#在指定的时间间隔内返回均匀间隔的数字,返回的是均匀间隔的样本，在间隔开始时计算，停止,区间的端点可以选择性地排除。
        for x1 in x:
            X_list.append(x1)           
        Y_list = []                 
        while True:
            Y_list =[]
            size = self.ser.inWaiting()         
            if size != 0:    
                pid_data = self.ser.read(size)  #读取数据，从缓存区size读取数据放到pid_data中
                #print(3)
                # time.sleep(1) #延迟1秒                  
        try:
            for line in pid_data.readlines():
                lineArr = line.strip().split() # line.strip()剔除首尾的空格,line.strip().split(),针对一个字符串返回一个字符串列表
                Y_list.append(int(lineArr[0]))
                plt.plot(X_list,Y_list,'r')
                plt.show()      
        except Exception as error:            
            print(error)
            
    
    #连接服务器        
    def connect_server(self):
     
        self.ser.model = self.comboBox_6.currentText()      
        address =('127.0.0.1')  #服务器的IP地址
        port = 8888 #服务器的端口
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #连接服务端
        client.connect((address,port))
                
        #while 循环时为了保证能持续进行数据传输
        while True:
            data = self.ser.write(binascii.a2b_hex(self.textEdit.toPlainText()))
            if not data:
                break
            data = self.ser.write(self.textEdit.toPlainText().encode('utf-8'))
            client.send_data(data)  #发送客户端信息
            client.close()
    """
      #关闭服务器
    def close_server(self):
        
        self.ser.model = self.comboBox_6.currentText()      
        address =('127.0.0.1')  #服务器的IP地址
        port = 8888 #服务器的端口
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        #连接服务端
        client.close((address,port))
        
    """
        
        
        
            
            
            
            
    
        
        
        

            
#调用程序    
if __name__ == '__main__':
    
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)     
    MainWindow.show() 
    sys.exit(app.exec_()) 




    

                                                                                                                                        