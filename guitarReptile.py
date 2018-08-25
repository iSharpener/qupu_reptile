'''
Created on 2018年3月16日

@author: Xiaopeng
这个脚本是从所有的网页中提取每首歌曲乐谱图所在网页的地址，存储到resource.txt文件中
从所有乐谱图所在网页提取所有乐谱图的地址，并且存储到imageurl.txt中
'''


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import urllib.request
from time import sleep
import time
from bs4 import BeautifulSoup
import re
class Reptile:
    def __init__(self,url,filepath,startpage,endpage):
        self.wholeurl = url+'/'+str(startpage)+'.html'
        self.page = endpage-startpage+1
        self.url = "http://www.qupu123.com/"
        self.dir = filepath
    def builddriver(self):
        chrome_options = webdriver.ChromeOptions()
        prefs = {"profile.managed_default_content_settings.images": 2}
        chrome_options.add_experimental_option("prefs", prefs)
        chrome_options.add_argument('--referer=http://www.qupu123.com/qiyue/jita')
        obj = webdriver.Chrome(executable_path='/Users/xiaopeng/Downloads/chromedriver',chrome_options=chrome_options) #加载网址

       # obj = webdriver.Chrome(executable_path='/Users/xiaopeng/Downloads/chromedriver')  # 加载网址
        print("浏览器最大化")
        obj.maximize_window()
        obj.get(self.wholeurl)
        self.obj = obj
    def destroy(self):
        self.obj.quit()
    #获取每一页的歌曲条目
    def getPageItems(self):
        #=========================================================================
        #操作一
        #此段代码是将267页的所有歌曲信息抓取下来，先存到resource.txt文件中，避免之后出现问题，若此段不用，
        #可注释掉，直接进行操作二
        #=========================================================================
        fin = open('resource.txt','w',encoding='utf-8')
        i = 0
        while i<self.page:
            pagesoup = BeautifulSoup(self.obj.page_source.encode('utf-8'), 'html.parser');
            div = pagesoup.find(name = 'div',attrs={'class':'body'})
            tbody = div.find(name = 'tbody')
            trs = tbody.findAll(name = 'tr')
            pageitems = dict()
            #获取图片资源所在url
            for tr in trs:
                try:
                        name = tr.find(name = 'td',attrs={'class':'f1'})
                        atag = name.find(name = 'a')
                        songname = atag.getText()
                        suburl = atag['href']
                        author = tr.find(name = 'td',attrs={'class':'f3'}).getText()
                        singer = tr.find(name = 'td',attrs={'class':'f4'}).getText()
                        print('歌曲名:',songname)
                        print('作词/作曲:',author)
                        print('演唱:',singer)
                        print('资源地址',self.url+suburl)
                        infostr = songname +'-词/曲:'+author+'-演唱:'+singer
                        print(infostr)
                        resourceurl = self.url+suburl
                        print('\n')
                        pageitems[infostr] = resourceurl
                        fin.write(infostr+'\n')
                        fin.write(resourceurl+'\n')
                except:
                    continue
            try:
                f = self.obj.find_element_by_link_text('下一页')
                f.click()
            except:
                self.obj.close()

            i=i+1
        print(pageitems)
        fin.close()



