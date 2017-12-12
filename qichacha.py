#coding=utf-8
# 根据企查查网站返回查询信息
from urllib import request
from bs4 import BeautifulSoup
import re
import headers as hd

class Qichacha:
    headers = hd.Headers()

    def __init__(self,companyName,call):
        self.company_info_dist = {}
        self.call = call
        soup = self.__getSoup(companyName)
        for i in range(1, len(soup)):
            if i % 2 == 1:
                key = soup[i - 1].text.replace("：", '').replace("\n", '')
                if key == '企业地址':
                    self.company_info_dist[key] = soup[i].text.split("查看地图")[0].replace("\n",'').strip().rstrip()
                elif key == '法定代表人':
                    self.company_info_dist[key] = soup[i].text.replace("\n",'').replace(">",'').strip().rstrip()
                else:
                    self.company_info_dist[key] = soup[i].text.replace("\n",'').strip().rstrip()
                if key == '历史股东':
                    break

    def getHtml(self,url):
        html = ""
        headers = self.headers.getHeaders(url)
        try:
            req = request.Request(url, headers=headers)
            page = request.urlopen(req).read()
            html = page.decode('utf-8')
        except OSError as err:
            print("OS Error: {}".format(err))
        except ValueError as err:
            print("Value Error: {}".format(err))
        except:
            print('执行出错')
        return html

    def __getComInfo(self,companyName):
        info = {}
        htmlText = self.getHtml("https://www.qichacha.com/search?key=%s" % (request.quote(companyName)))
        re_html = re.compile('</?\w+[^>]*>')  # 去除HTML标签
        re_phone = re.compile(r"电话：(.*)\n")  # 匹配电话
        re_email = re.compile(r"邮箱：(.*)")  # 匹配邮箱
        re_dress = re.compile(r"\：(.*)")  # 匹配地址
        try:
            html = BeautifulSoup(htmlText, features='html.parser')
            attrs = html.select(".m-t-xs a")[0].attrs
            href = attrs["href"]
            attrsList = href[href.index("?") + 1:].split("&")
            for item in attrsList:
                info[item.split("=")[0]] = re_html.sub('', request.unquote(item.split("=")[1]))
            self.company_info_dist['企业名称'] = companyName
            self.company_info_dist['电话'] = re.findall(re_phone, html.select(".m-t-xs")[1].text)[0]
            self.company_info_dist['邮箱'] = re.findall(re_email, html.select(".m-t-xs")[1].text)[0]
            self.company_info_dist['地址'] = re.findall(re_dress, html.select(".m-t-xs")[2].text)[0]
        except:
            print("没有查询到相应公司！")
        return info

    def __getSoup(self,companyName):
        comInfo = self.__getComInfo(companyName)
        if 'companyname' not in comInfo:
            return []
        if comInfo['companyname'] != companyName:
            if self.call:
                self.call("未能准确匹配，默认匹配第一条！")
        url = ('https://www.qichacha.com/company_getinfos?unique=%s&companyname=%s&tab=base' % (
        comInfo['companykeyNo'], request.quote(companyName)))
        # page = getHtml(r"https://www.qichacha.com/firm_%s.shtml" % comInfo['companykeyNo'])
        page = self.getHtml(url)
        soup = BeautifulSoup(page, features='html.parser').select('.ma_left')
        return soup

    def getInfoDist(self):
        return self.company_info_dist






