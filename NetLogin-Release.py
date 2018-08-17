import re
import requests

login_url = "http://202.204.48.82/"
getv6_url = "http://cippv6.ustb.edu.cn/get_ip.php"

Student_ID = 'xxxxxx' # Input your ID
Student_Password = 'yyyyyy' # Input your net password

post_header = \
{
    'Host': '202.204.48.82',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:61.0) Gecko/20100101 Firefox/61.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://202.204.48.82/',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '112',
    'Cookie': 'myusername=xxxxxx; username=xxxxxx; pwd=yyyyyy', #Don't FORGET to change this line with your ID and PW!
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

def getv6ip():
    v6_response = requests.get(getv6_url)
    pattern = re.compile('\'(.*)\'')
    v6_addr = pattern.findall(v6_response.text)[0]
    return v6_addr;

def main():
    getv6ip()
    post_data = \
    {
        'DDDDD': Student_ID,
        'upass': Student_Password,
        '0MKKey': '123456789',
        'v6ip': getv6ip()
    }
    requests.post(login_url, data=post_data, headers=post_header)

main()
