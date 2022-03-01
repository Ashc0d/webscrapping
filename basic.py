import requests
import config
from bs4 import BeautifulSoup


headers = {
    'User-Agent' : 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0'

}

login_data = {
    'txtUserName':	config.username,
    'txtPassword':	config.passwd,
    'hdnloginwith':	'username',
    'save':	'LogIn'
}

def login():
    with requests.session() as rs:

        url = config.url
        #home_url = ''
        req = rs.get(url, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')


        login_data['__VIEWSTATE'] = soup.find('input', attrs={'id': '__VIEWSTATE'})['value']

        login_data['__VIEWSTATEGENERATOR'] = soup.find('input', attrs={'id': '__VIEWSTATEGENERATOR'})['value']

        login_data['__EVENTVALIDATION'] = soup.find('input', attrs={'id': '__EVENTVALIDATION'})['value']


        req = rs.post(url, data = login_data, headers=headers)
        soup = BeautifulSoup(req.content, 'html.parser')
        history = req.history
        status_code = req.status_code
        #time.sleep(4)
        expiry_data = soup.find("span", {"id" : "lbUsageType", "class" : "GuagealterCol"}) 
        #expiry_data = soup.find("form", {"id" : "post"}) 

        print(expiry_data)
        print(history)
        print(status_code)
        
login()