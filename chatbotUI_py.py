# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:09:31 2020

@author: 현
"""
import sys
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *

import paramiko
import getpass
import time


global a



#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("chatbotUI.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self.fontSize = 10

        #버튼에 기능을 할당하는 코드
        self.sentence.returnPressed.connect(self.printTextFunction)
        self.input_text.clicked.connect(self.changeTextFunction)
        
        self.stop=True
        
    ##엔터키로 입력할때
    def printTextFunction(self) :
        ##나중에 입력하면 대답받을 때 이거 주면 됨.
        global a
        
        colorvar = QColor(0,0,255)
        self.textBrowser.setTextColor(colorvar)
        
        print(self.sentence.text())
        a=self.sentence.text()
        self.textBrowser.append("나 : "+self.sentence.text())
        self.sentence.setText("")
        self.answer()
    ##버튼으로 입력할때
    def changeTextFunction(self) :
        global a
        colorvar = QColor(0,0,255)
        self.textBrowser.setTextColor(colorvar)
        a=self.sentence.text()
        print(self.sentence.text())
        
        self.textBrowser.append("나 : "+self.sentence.text())
        self.sentence.setText("챗봇이 입력하는중...")
        self.answer()
        self.sentence.setText("")
    
    def answer(self) :
        global a
        cli = paramiko.SSHClient()
        cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)
 
        server = "155.230.26.195"  # 호스트명이나 IP 주소
        user = "brainai"  
        pwd = "053-950-5544" # 암호입력 숨김
        cli.connect(server, port=22, username=user, password=pwd)
        b=a.replace(" ","")
        question='cd anaconda3/KoGPT2-chatbot/ && source ~/anaconda3/etc/profile.d/conda.sh && conda activate zeropark && CUDA_VISIBLE_DEVICES=0 python train_torch.py --gpus 1 --chat --input'+' '+b
        
        stdin, stdout, stderr = cli.exec_command(question)
        lines = stdout.readlines()
        
        colorvar = QColor(255,0,0)
        self.textBrowser.setTextColor(colorvar)
        #print("크누아이 : 안녕")
        
        self.textBrowser.append("크누아이 : "+lines[3])
        self.stop=False
        cli.close()
    

if __name__ == "__main__" :
    #QApplication : 프로그램을 실행시켜주는 클래스


    
    app = QApplication(sys.argv) 

    #WindowClass의 인스턴스 생성
    myWindow = WindowClass() 

    #프로그램 화면을 보여주는 코드
    myWindow.show()
    
    #while myWindow.stop:
    #    continue
    #프로그램을 이벤트루프로 진입시키는(프로그램을 작동시키는) 코드
    app.exec_()
  