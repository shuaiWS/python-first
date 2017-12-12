import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import time


USERNAME='13534050714'
PASSWORD='ws9239264'
def getHeaders(url):
    return  {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Referer': url,
        'Connection': 'keep-alive'
    }

def login():
    LOGIN_URL = 'https://www.qichacha.com/user_loginaction'
    cookie_filename = 'cookie.txt'
    headers = getHeaders('https://www.qichacha.com')
    plyload = {
        "nameNormal":USERNAME,
        "pwdNormal":PASSWORD,
        # "keep":'on',
        # 'csessionid_one':"01wi1omrEcgHNunM9_cPMUigdpELda59Xu9iu1J4QdTm1LkYwUyL3tEvSPDmf_sgwI6mZpQS__-B_UZKsRKyMQHdJnavP8mSexe_2IDdzBces",
        # 'sig_one':"05jlvGB4hM6gXLbAzm5bD_USfBXinT1m-LHlyMkY4oJygPmng5CPaSjCOswOhGO1ubJ5qNanSuH41qGJdkjGRTarTm1FmZ-7wLMSkuV6IX1cspdXhia8QAmURc0c57i8pUzwI_54XBnU_PO3sohynTns2j3Zgoh8_VBl3adh9BHkl7qlzuivXN72i0iEV4uc0p7CLai8SOEEicPdFITuY_30BvWl0wXyBDRG8IyP8SI_vDwI0HGqOnbIw0cx0LY31dsXUD39YpPVF",
        # 'token_one':'QNYX:1501053848563:0.9227271635497938',
        # "scene_one":"login",
        # "verify_type":'1'
    }
    postdata = urllib.parse.urlencode(plyload).encode()
    cookie = http.cookiejar.MozillaCookieJar(cookie_filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    # request = urllib.request.Request(LOGIN_URL, postdata, headers = headers)
    request = urllib.request.Request(LOGIN_URL,  headers = headers)
    try:
        response = opener.open(request)
        page = response.read().decode()
        cookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
        time.sleep(3)
        print(page)
    except urllib.error.URLError as e:
        print(e, ':', e.reason)
