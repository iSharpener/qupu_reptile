'''
Created on 2018年3月16日

@author: Xiaopeng
这个脚本是从所有的网页中提取每首歌曲乐谱图所在网页的地址，存储到resource.txt文件中
从所有乐谱图所在网页提取所有乐谱图的地址，并且存储到imageurl.txt中
'''


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchWindowException
import urllib.request
from time import sleep
import sys
import time
from bs4 import BeautifulSoup
import re
class Reptile1:
    def __init__(self,url):
        self.wholeurl = url
        self.url = "http://www.qupu123.com/"
    def builddriver(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--referer=http://www.qupu123.com/qiyue/jita')
        obj = webdriver.Chrome(executable_path='/Users/xiaopeng/Downloads/chromedriver',chrome_options=chrome_options) #加载网址

       # obj = webdriver.Chrome(executable_path='/Users/xiaopeng/Downloads/chromedriver')  # 加载网址
        print("浏览器最大化")
        obj.maximize_window()
        self.obj = obj
    def destroy(self):
        self.obj.quit()
    #获取每一页的歌曲条目
    def getPageItems(self):
        image = open('imageurl.txt','w',encoding='utf-8')
        f = open("resource.txt", "r")
        lines = f.readlines()  # 读取全部内容
        print(len(lines))
        imglist = dict()
        for i in range(int(len(lines)/2)):
            imglist[lines[2*i]] = lines[2*i+1]
        for dic in imglist:
            flag = 0
            while flag==0:
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
                    header = newsoup.find(name = 'div',attrs={'class':'content_head'})
                    h1 = header.find(name ='h1')
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
                    #print(dic)
                    image.write(songname+'\n')
                    if status == 1:
                        image.write(imglist[dic])
                    for imgtag in imgtags:
                        print(imgtag)
                        wholeurl = self.url+imgtag['src']
                        print(wholeurl)
                        image.write(wholeurl+'\n')
                    if status == 1:
                        for tag in frameimagetags:
                            print(tag)
                            wholeurl = self.url + tag['src']
                            print(wholeurl)
                            image.write(wholeurl+'\n')
                    image.write('\n')
                    print('\n')
                    imageurls = list()
                    flag = 1
                except AttributeError:
                    print('作者版权保护')
                    flag = 1
                except selenium.common.exceptions.NoSuchWindowException:
                    sys.exit(0)
                except:
                    continue
        #=========================================================================



