# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor
from guitarReptile import Reptile
from getpictureurl import Reptile1
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchWindowException
import urllib.request
from time import sleep
import time
from bs4 import BeautifulSoup
import re
import os
# class EmittingStream(QtCore.QObject):
#     textWritten = QtCore.pyqtSignal(str)  # 定义一个发送str的信号
#     def write(self, text):
#         self.textWritten.emit(str(text))
class Ui_MainWindow(object):
    # 接收信号str的信号槽
    # def outputWritten(self, text):
    #     cursor = self.textEdit_2.textCursor()
    #     cursor.movePosition(QtGui.QTextCursor.End)
    #     cursor.insertText(text)
    #     self.textEdit_2.setTextCursor(cursor)
    #     self.textEdit_2.ensureCursorVisible()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(839, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        # self.scrollArea.setGeometry(QtCore.QRect(60, 60, 311, 421))
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        # self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 309, 419))
        # self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(50, 45, 321, 461))
        self.textEdit_2.setObjectName("textEdit_2")
        # self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.cunchulujing = QtWidgets.QLabel(self.centralwidget)
        self.cunchulujing.setGeometry(QtCore.QRect(430, 20, 81, 20))
        self.cunchulujing.setObjectName("cunchulujing")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(450, 50, 60, 16))
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.wangyelianjie = QtWidgets.QLabel(self.centralwidget)
        self.wangyelianjie.setGeometry(QtCore.QRect(450, 50, 71, 20))
        self.wangyelianjie.setObjectName("wangyelianjie")
        self.getpictureurl = QtWidgets.QPushButton(self.centralwidget)
        self.getpictureurl.setGeometry(QtCore.QRect(650, 280, 131, 32))
        self.getpictureurl.setObjectName("getpictureurl")
        self.getpicture = QtWidgets.QPushButton(self.centralwidget)
        self.getpicture.setGeometry(QtCore.QRect(650, 320, 131, 32))
        self.getpicture.setObjectName("getpicture")
        self.ispicture = QtWidgets.QRadioButton(self.centralwidget)
        self.ispicture.setGeometry(QtCore.QRect(650, 150, 100, 20))
        self.ispicture.setObjectName("ispicture")
        self.notpicture = QtWidgets.QRadioButton(self.centralwidget)
        self.notpicture.setGeometry(QtCore.QRect(650, 180, 121, 20))
        self.notpicture.setObjectName("notpicture")
        self.xiaoxilan = QtWidgets.QLabel(self.centralwidget)
        self.xiaoxilan.setGeometry(QtCore.QRect(440, 360, 111, 20))
        self.xiaoxilan.setObjectName("xiaoxilan")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 80, 60, 16))
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.qishiyema = QtWidgets.QLabel(self.centralwidget)
        self.qishiyema.setGeometry(QtCore.QRect(450, 80, 51, 20))
        self.qishiyema.setObjectName("qishiyema")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(450, 110, 60, 16))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.jieshuyema = QtWidgets.QLabel(self.centralwidget)
        self.jieshuyema.setGeometry(QtCore.QRect(450, 110, 61, 20))
        self.jieshuyema.setObjectName("jieshuyema")
        self.filelink = QtWidgets.QLineEdit(self.centralwidget)
        self.filelink.setGeometry(QtCore.QRect(550, 20, 231, 21))
        self.filelink.setObjectName("filelink")

        self.filelink.setText("/Users/xiaopeng/Music/曲谱")
        self.startpagelabel = QtWidgets.QLineEdit(self.centralwidget)
        self.startpagelabel.setGeometry(QtCore.QRect(550, 80, 231, 21))
        self.startpagelabel.setObjectName("startpagelabel")
        self.endpagelabel = QtWidgets.QLineEdit(self.centralwidget)
        self.endpagelabel.setGeometry(QtCore.QRect(550, 110, 231, 21))
        self.endpagelabel.setObjectName("endpagelabel")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(440, 398, 351, 81))
        self.textEdit.setObjectName("textEdit")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 50, 231, 26))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.clearxiaoxilan = QtWidgets.QPushButton(self.centralwidget)
        self.clearxiaoxilan.setGeometry(QtCore.QRect(660, 490, 131, 32))
        self.clearxiaoxilan.setObjectName("clearxiaoxilan")
        self.clearkongzhitai = QtWidgets.QPushButton(self.centralwidget)
        self.clearkongzhitai.setGeometry(QtCore.QRect(240, 510, 131, 32))
        self.clearkongzhitai.setObjectName("clearkongzhitai")
        self.kongzhitailabel = QtWidgets.QLabel(self.centralwidget)
        self.kongzhitailabel.setGeometry(QtCore.QRect(70, 20, 111, 20))
        self.kongzhitailabel.setObjectName("kongzhitailabel")
        self.confirmall = QtWidgets.QPushButton(self.centralwidget)
        self.confirmall.setGeometry(QtCore.QRect(650, 230, 131, 32))
        self.confirmall.setObjectName("confirmall")
        self.guge = QtWidgets.QLineEdit(self.centralwidget)
        self.guge.setGeometry(QtCore.QRect(440, 200, 191, 21))
        self.guge.setObjectName("guge")
        self.guge.setText("/Users/xiaopeng/Downloads/chromedriver")
        self.huohu = QtWidgets.QLineEdit(self.centralwidget)
        self.huohu.setGeometry(QtCore.QRect(440, 280, 191, 21))
        self.huohu.setObjectName("huohu")
        self.huohu.setText('/Users/xiaopeng/Downloads/geckodriver')
        self.gugelabel = QtWidgets.QLabel(self.centralwidget)
        self.gugelabel.setGeometry(QtCore.QRect(440, 170, 101, 20))
        self.gugelabel.setObjectName("gugelabel")
        self.huohulabel = QtWidgets.QLabel(self.centralwidget)
        self.huohulabel.setGeometry(QtCore.QRect(440, 240, 91, 20))
        self.huohulabel.setObjectName("huohulabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 839, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.textEdit.setReadOnly(True)
        self.textEdit_2.setReadOnly(True)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.confirmall.clicked.connect(self.confirm)
        self.clearxiaoxilan.clicked.connect(self.clearmessage)
        self.getpictureurl.clicked.connect(self.getpu)
        self.clearkongzhitai.clicked.connect(self.clearconsole)
        self.getpicture.clicked.connect(self.downloadpicture)
        # sys.stdout = EmittingStream(textWritten=self.outputWritten)
        # sys.stderr = EmittingStream(textWritten=self.outputWritten)
    def clearconsole(self):
        self.textEdit_2.setText("")
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cunchulujing.setText(_translate("MainWindow", "文件存储路径"))
        self.wangyelianjie.setText(_translate("MainWindow", "曲谱类型"))
        self.getpictureurl.setText(_translate("MainWindow", "获取曲谱图片地址"))
        self.getpicture.setText(_translate("MainWindow", "下载曲谱图片"))
        self.ispicture.setText(_translate("MainWindow", "图片格式曲谱"))
        self.notpicture.setText(_translate("MainWindow", "pdf以及其他格式"))
        self.xiaoxilan.setText(_translate("MainWindow", "消息栏"))
        self.qishiyema.setText(_translate("MainWindow", "起始页码"))
        self.jieshuyema.setText(_translate("MainWindow", "结束页码"))
        self.comboBox.setItemText(0, _translate("MainWindow", "声乐：民歌"))
        self.comboBox.setItemText(1, _translate("MainWindow", "声乐：通俗"))
        self.comboBox.setItemText(2, _translate("MainWindow", "声乐：美声"))
        self.comboBox.setItemText(3, _translate("MainWindow", "声乐：合唱"))
        self.comboBox.setItemText(4, _translate("MainWindow", "声乐：少儿"))
        self.comboBox.setItemText(5, _translate("MainWindow", "声乐：外国"))
        self.comboBox.setItemText(6, _translate("MainWindow", "器乐：钢琴"))
        self.comboBox.setItemText(7, _translate("MainWindow", "器乐：笛箫"))
        self.comboBox.setItemText(8, _translate("MainWindow", "器乐：电子琴"))
        self.comboBox.setItemText(9, _translate("MainWindow", "器乐：葫芦丝"))
        self.comboBox.setItemText(10, _translate("MainWindow", "器乐：手风琴"))
        self.comboBox.setItemText(11, _translate("MainWindow", "器乐：胡琴谱"))
        self.comboBox.setItemText(12, _translate("MainWindow", "器乐：萨克斯"))
        self.comboBox.setItemText(13, _translate("MainWindow", "器乐：琵琶谱"))
        self.comboBox.setItemText(14, _translate("MainWindow", "器乐：长笛"))
        self.comboBox.setItemText(15, _translate("MainWindow", "器乐：扬琴"))
        self.comboBox.setItemText(16, _translate("MainWindow", "器乐：铜管"))
        self.comboBox.setItemText(17, _translate("MainWindow", "器乐：口琴"))
        self.comboBox.setItemText(18, _translate("MainWindow", "器乐：吉他"))
        self.comboBox.setItemText(19, _translate("MainWindow", "器乐：提琴"))
        self.comboBox.setItemText(20, _translate("MainWindow", "器乐：古筝古琴"))
        self.comboBox.setItemText(21, _translate("MainWindow", "器乐：其他乐谱"))
        self.comboBox.setItemText(22, _translate("MainWindow", "戏曲：京剧"))
        self.comboBox.setItemText(23, _translate("MainWindow", "戏曲：豫剧"))
        self.comboBox.setItemText(24, _translate("MainWindow", "戏曲：越剧"))
        self.comboBox.setItemText(25, _translate("MainWindow", "戏曲：评剧"))
        self.comboBox.setItemText(26, _translate("MainWindow", "戏曲：黄梅戏"))
        self.comboBox.setItemText(27, _translate("MainWindow", "戏曲：二人转"))
        self.comboBox.setItemText(28, _translate("MainWindow", "戏曲：花鼓戏谱"))
        self.comboBox.setItemText(29, _translate("MainWindow", "戏曲：其他唱谱"))
        self.comboBox.setItemText(30, _translate("MainWindow", "PDF乐谱：声乐"))
        self.comboBox.setItemText(31, _translate("MainWindow", "PDF乐谱：弦乐"))
        self.comboBox.setItemText(32, _translate("MainWindow", "PDF乐谱：钢琴"))
        self.comboBox.setItemText(33, _translate("MainWindow", "PDF乐谱：吉他"))
        self.comboBox.setItemText(34, _translate("MainWindow", "PDF乐谱：长笛"))
        self.comboBox.setItemText(35, _translate("MainWindow", "PDF乐谱：其他"))
        self.clearxiaoxilan.setText(_translate("MainWindow", "清空消息栏"))
        self.clearkongzhitai.setText(_translate("MainWindow", "清空控制台"))
        self.kongzhitailabel.setText(_translate("MainWindow", "控制台"))
        self.confirmall.setText(_translate("MainWindow", "确定所填信息"))
        self.gugelabel.setText(_translate("MainWindow", "谷歌驱动器地址"))
        self.huohulabel.setText(_translate("MainWindow", "火狐驱动器地址"))
    def clearmessage(self):
        self.textEdit.setText("")
    def getpu(self):
        try:
            print(self.wholeurl)
            print(self.startpage)
            print(self.endpage)
            print(self.qupuname)
            print(self.filepath)
        except:
            self.textEdit.append("请先填完爬取信息，确定之后再爬取")
            return
        #爬取所有曲谱地址
        sp = self.qupuname.split("：")
        self.initreptile(self.wholeurl, self.filepath, self.startpage,self.endpage)
        try:
            self.builddriver()
        except:
            self.textEdit.append("驱动器加载失败，请检查路径")
            return
        self.getPageItems()
        self.getPageItems1()
        self.destroy()

    def confirm(self):
        self.textEdit.setText("")
        self.filepath = self.filelink.text()
        self.qupuname = self.comboBox.currentText()
        self.startpage = self.startpagelabel.text()
        self.endpage = self.endpagelabel.text()
        self.gugedriver = self.guge.text()
        self.huohudriver = self.huohu.text()
        if os.path.isfile(self.filepath):
            print("对不起，您应该选取一个目录,请重新输入")
            self.textEdit.moveCursor(QTextCursor.End)
            self.textEdit.append("对不起，您应该选取一个目录,请重新输入")
            return
        try:
            if os.path.isdir(self.filepath):
                print("目录存在,并将该目录作为存储目录")
                self.textEdit.append("目录存在,并将该目录作为存储目录：\n"+self.filepath)
            else:
                os.mkdir(filepath)
                print("目录不存在，新建目录，作为存储目录：" + filepath)
                self.textEdit.append("目录不存在，新建目录，作为存储目录：\n" + self.filepath)
        except:
            print("目录名称有误，请重新输入")
            self.textEdit.moveCursor(QTextCursor.End)
            self.textEdit.append("目录名称有误，请重新输入")
            return
        sp = self.qupuname.split("：")
        quputype = sp[0]
        qupu = sp[1]
        self.wholeurl = ''
        if quputype == "声乐":
            baseurl = "http://www.qupu123.com/"
            if qupu == "民歌":
                self.wholeurl = baseurl+'minge'
            if qupu == "通俗":
                self.wholeurl = baseurl+'tongsu'
            if qupu == "美声":
                self.wholeurl = baseurl+'meisheng'
            if qupu == "合唱":
                self.wholeurl = baseurl+'hechang'
            if qupu == "少儿":
                self.wholeurl = baseurl+'shaoer'
            if qupu == "外国":
                self.wholeurl = baseurl+'waiguo'
        if quputype == "器乐":
            baseurl = "http://www.qupu123.com/qiyue/"
            if qupu == "钢琴":
                self.wholeurl = baseurl+'gangqin'
            if qupu == "电子琴":
                self.wholeurl = baseurl+'dianziqin'
            if qupu == "手风琴":
                self.wholeurl = baseurl+'shoufengqin'
            if qupu == "萨克斯":
                self.wholeurl = baseurl+'sakesi'
            if qupu == "长笛":
                self.wholeurl = baseurl+'changdi'
            if qupu == "铜管":
                self.wholeurl = baseurl+'tongguan'
            if qupu == "吉他":
                self.wholeurl = baseurl+'jita'
            if qupu == "古筝古琴":
                self.wholeurl = baseurl+'guzhengguqin'
            if qupu == "笛箫":
                self.wholeurl = baseurl+'dixiao'
            if qupu == "葫芦丝":
                self.wholeurl = baseurl+'hulusi'
            if qupu == "胡琴谱":
                self.wholeurl = baseurl+'huqin'
            if qupu == "琵琶谱":
                self.wholeurl = baseurl+'pipa'
            if qupu == "扬琴":
                self.wholeurl = baseurl+'yangqin'
            if qupu == "口琴":
                self.wholeurl = baseurl+'kouqin'
            if qupu == "提琴":
                self.wholeurl = baseurl+'tiqin'
            if qupu == "其他乐谱":
                self.wholeurll = baseurl+'qita'
        if quputype == "戏曲":
            baseurl = "http://www.qupu123.com/xiqu/"
            if qupu == "京剧":
                self.wholeurl = baseurl +'jingju'
            if qupu == "越剧":
                self.wholeurl = baseurl +'yueju'
            if qupu == "黄梅戏":
                self.wholeurl = baseurl +'huangmeixi'
            if qupu == "花鼓戏":
                self.wholeurl = baseurl +'huaguxi'
            if qupu == "豫剧":
                self.wholeurl = baseurl +'yuju'
            if qupu == "评剧":
                self.wholeurl = baseurl +'pingju'
            if qupu == "二人转":
                self.wholeurl = baseurl +'errenzhuan'
            if qupu == "其他唱谱":
                self.wholeurl = baseurl +'qita'
        if quputype == "PDF乐谱":
            baseurl = "http://www.qupu123.com/pdf/"
            if qupu == "声乐":
                self.wholeurl = baseurl +'shengyue'
            if qupu == "钢琴":
                self.wholeurl = baseurl +'gangqin'
            if qupu == "长笛":
                self.wholeurl = baseurl +'changdi'
            if qupu == "弦乐":
                self.wholeurl = baseurl +'xianyue'
            if qupu == "吉他":
                self.wholeurl = baseurl + 'jita'
            if qupu == "其他":
                self.wholeurl= baseurl + 'qita'
        print(self.wholeurl)
        if self.gugedriver =='':
            self.textEdit.append("请输入谷歌驱动器所在路径")
            return
        else:
            self.textEdit.append("谷歌驱动器路径："+self.gugedriver)
        if self.huohudriver == '':
            self.textEdit.append("请输入火狐驱动器所在路径")
            return
        else:
            self.textEdit.append("火狐驱动器路径："+self.huohudriver)
        if self.startpage =='':
            self.textEdit.append("请输入起始页码")
            return
        else:
            try:
                self.startpage = int(self.startpage)
            except:
                self.textEdit.append("请输入有效起始页码")
                return
            self.textEdit.append("爬取从该种类曲谱的第" + str(self.startpage)+"页开始爬取")
        if self.endpage =='':
            self.textEdit.append("请输入结束页码")
            return
        else:
            try:
                self.endpage = int(self.endpage)
            except:
                self.textEdit.append("请输入有效结束页码")
                return
            self.textEdit.append("爬取从该种类曲谱的第" + str(self.endpage) + "页结束爬取")
        self.textEdit.append("您将要爬取的网页为\n" + self.wholeurl)
        self.textEdit.append("您将要爬取的曲谱类型为" + quputype)
        self.textEdit.append("您将要爬取的曲谱种类为" + qupu)
        QtGui.QDesktopServices.openUrl(QtCore.QUrl(self.wholeurl))
        self.textEdit.append("目前可以进行爬取，请点击按钮爬取")
    def initreptile(self, url, filepath, startpage, endpage):
        self.wholeurluse = url + '/' + str(startpage) + '.html'
        self.page = endpage - startpage + 1
        self.url = "http://www.qupu123.com/"
        self.dir = filepath

    def builddriver(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--referer=http://www.qupu123.com/qiyue/jita')
        obj = webdriver.Chrome(executable_path=self.gugedriver,
                               chrome_options=chrome_options)  # 加载网址

        # obj = webdriver.Chrome(executable_path='/Users/xiaopeng/Downloads/chromedriver')  # 加载网址
        print("浏览器最大化")
        self.textEdit_2.append("浏览器最大化")
        obj.maximize_window()
        obj.get(self.wholeurluse)
        self.obj = obj

    def destroy(self):
        self.obj.quit()

    # 获取每一页的歌曲条目
    def getPageItems(self):
        # =========================================================================
        # 操作一
        # 此段代码是将267页的所有歌曲信息抓取下来，先存到resource.txt文件中，避免之后出现问题，若此段不用，
        # 可注释掉，直接进行操作二
        # =========================================================================
        fin = open('resource.txt', 'w', encoding='utf-8')
        i = 0
        while i < self.page:
            try:
                pagesoup = BeautifulSoup(self.obj.page_source.encode('utf-8'), 'html.parser');
                div = pagesoup.find(name='div', attrs={'class': 'body'})
                tbody = div.find(name='tbody')
                trs = tbody.findAll(name='tr')
                pageitems = dict()
                # 获取图片资源所在url
                for tr in trs:
                    try:
                        name = tr.find(name='td', attrs={'class': 'f1'})
                        atag = name.find(name='a')
                        songname = atag.getText()
                        suburl = atag['href']
                        author = tr.find(name='td', attrs={'class': 'f3'}).getText()
                        singer = tr.find(name='td', attrs={'class': 'f4'}).getText()
                        print('歌曲名:', songname)
                        self.textEdit_2.append('歌曲名:'+songname)
                        print('作词/作曲:', author)
                        self.textEdit_2.append('作词/作曲:'+author)
                        print('演唱:', singer)
                        self.textEdit_2.append('演唱:'+singer)
                        print('资源地址', self.url + suburl)
                        self.textEdit_2.append('资源地址'+self.url + suburl)
                        infostr = songname + '-词/曲:' + author + '-演唱:' + singer
                        print(infostr)
                        self.textEdit_2.append(infostr)
                        resourceurl = self.url + suburl
                        print('\n')
                        self.textEdit_2.append('\n')
                        pageitems[infostr] = resourceurl
                        fin.write(infostr + '\n')
                        fin.write(resourceurl + '\n')
                    except:
                        continue
                try:
                    f = self.obj.find_element_by_link_text('下一页')
                    f.click()
                except:
                    self.obj.close()

                i = i + 1
            except:
                return
        fin.close()
        self.textEdit.append("曲谱链接获取完成")
    def getPageItems1(self):
        image = open('imageurl.txt', 'w', encoding='utf-8')
        f = open("resource.txt", "r")
        lines = f.readlines()  # 读取全部内容
        print(len(lines))
        imglist = dict()
        for i in range(int(len(lines) / 2)):
            imglist[lines[2 * i]] = lines[2 * i + 1]
        for dic in imglist:
            flag = 0
            while flag == 0:
                try:
                    splits = dic.split('-')
                    self.obj.get(imglist[dic])
                    try:
                        # 模拟鼠标单击事件，由于存在图片不自动加载需要手动点击的情况
                        self.obj.find_element_by_xpath('// *[ @ id = "look_all"]').click()
                        # print(clickdiv)
                        # ActionChains(self.obj).click(clickdiv)

                    except:
                        print('没有div方块')
                    newsoup = BeautifulSoup(self.obj.page_source.encode('utf-8'), 'html.parser')
                    header = newsoup.find(name='div', attrs={'class': 'content_head'})
                    h1 = header.find(name='h1')
                    songname = h1.getText()
                    print(songname)
                    status = 1
                    imageList = newsoup.find(name='div', attrs={'class': 'imageList'})
                    imgtags = imageList.findAll(name='img')
                    try:
                        frame = self.obj.find_element_by_xpath('//*[@id="get_all_iframe"]')
                        self.obj.switch_to.frame('get_all_iframe')
                        sleep(4)
                        newsoup1 = BeautifulSoup(self.obj.page_source.encode('utf-8'), 'html.parser')
                        #  print(newsoup1)
                        frameimglist = newsoup1.find(name='div', attrs={'id': 'imglist'})
                        #  print(frameimglist)
                        frameimagetags = frameimglist.findAll(name='img')
                    except:
                        status = 0
                        print('没有frame')
                    # print(self.obj.page_source)
                    # print(dic)
                    image.write(songname + '\n')
                    if status == 1:
                        image.write(imglist[dic])
                    for imgtag in imgtags:
                        print(imgtag)
                        wholeurl = self.url + imgtag['src']
                        print(wholeurl)
                        image.write(wholeurl + '\n')
                    if status == 1:
                        for tag in frameimagetags:
                            print(tag)
                            wholeurl = self.url + tag['src']
                            print(wholeurl)
                            image.write(wholeurl + '\n')
                    image.write('\n')
                    print('\n')
                    imageurls = list()
                    flag = 1
                except AttributeError:
                    print('作者版权保护')
                    flag = 1
                except NoSuchWindowException:
                    self.textEdit.setText("对不起，浏览器意外退出，请重试")
                    return
                except:
                    continue
        self.textEdit.append("获取图片链接完成，可以下载图片")
    def downloadpicture(self):
        oripath = self.filepath+'/'
        f = open('imageurl.txt', 'r')
        lines = f.read()
        # print(lines)
        newlines = lines.split('\n\n')
        lists = list()
        for line in newlines:
            lists.append(line)
        for l in lists:
            sp = l.split('\n')
            sp[0] = sp[0].replace('/', '&')
            # 输出文件夹名称
            print(sp[0])
            songname = sp[0]
            # makdir(oripath+sp[0],sp[0])
            for s in range(1, len(sp)):
                # 输出网址
                print(sp[s])
                sps = sp[s].split('.')
                # 输出网址后缀，防盗链图片后缀以com开头
                type = sps[len(sps) - 1]
                if type == 'html':
                    print("使用特殊方式对防盗链图片所在网站进行爬取")
                    # ------------------------------------------------------------------------------
                    try:
                        driver = webdriver.Firefox(executable_path=self.huohudriver)
                    except:
                        self.textEdit.append("驱动器加载失败，请检查路径")
                        return
                    driver.maximize_window()
                    url = sp[s]
                    driver.get(url)
                    try:
                        # 模拟鼠标单击事件，由于存在图片不自动加载需要手动点击的情况
                        driver.find_element_by_xpath('// *[ @ id = "look_all"]').click()
                    except:
                        print('没有div')
                    soup = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                    imgList = soup.find(name='div', attrs={'class': 'imageList'})
                    # print(imgList)
                    u = imgList.find(name='img')
                    sp = u.get('src').split('.')
                    # sp = imgList.get_attribute('src').split('.')
                    # print(sp[len(sp)-1])
                    print(sp[0])
                    wholepath = oripath + songname + '-page1.jpg'
                    print("正在下载到:" + wholepath)
                    urllib.request.urlretrieve('http://www.qupu123.com' + u.get('src'), wholepath)
                    print("下载完成")
                    num = 0
                    try:
                        frame = driver.find_element_by_xpath('//*[@id="get_all_iframe"]')
                        driver.switch_to_frame('get_all_iframe')
                        sleep(4)
                        newsoup1 = BeautifulSoup(driver.page_source.encode('utf-8'), 'html.parser')
                        frameimglist = newsoup1.find(name='div', attrs={'id': 'imglist'})
                        print(frameimglist)
                        frameimagetags = frameimglist.findAll(name='img')
                        num = len(frameimagetags)
                    except:
                        print('没有frame')
                    print(num)
                    for i in range(num):
                        xpath = '// *[ @ id = "imglist"] / img[' + str(i + 1) + ']'
                        ele = driver.find_element_by_xpath(xpath)
                        sleep(3)
                        print("正在下载到:" + oripath + songname + '-page' + str(i + 2) + '.jpg')
                        with open(oripath + songname + '-page' + str(i + 2) + '.jpg', 'wb') as im:
                            im.write(ele.screenshot_as_png)
                            im.write(ele.screenshot_as_png)
                        print("下载成功")
                    driver.close()
                    # ------------------------------------------------------------------------------
                    break
                else:
                    d = sp[0].split('-')
                    print("此图不含有防盗链")
                    print('正在下载到:' + oripath + sp[0] + '-page' + str(s) + '.jpg')
                    try:
                        #  print(wholepath+str(s)+'.'+type)
                        urllib.request.urlretrieve(sp[s], oripath + sp[0] + '-page' + str(s) + '.jpg')
                    except:
                        print('下载失败')
                        continue;
                    print('下载成功')
            print('\n')
        self.textEdit.append("所有图片下载完成，请到文件夹查看")
