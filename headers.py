#coding=utf-8
# 返回查询url需要的请求头
class Cookie:
    Cookie = ''
    def __init__(self,cookie):
        Cookie.Cookie = cookie

class Headers(Cookie):
    def __init__(self):
        super()

    def getHeaders(self,url):
        return  {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Referer': url,
            'Connection': 'keep-alive',
            'Cookie':self.Cookie
        }