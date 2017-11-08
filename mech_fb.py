import mechanize
from bs4 import BeautifulSoup
import sys
import lxml
import urllib



class acadIITR:

    baseUrl = 'http://acad.iitr.ac.in/Student/'

    def __init__(self):
        self.browser = mechanize.Browser()
        self.browser.set_handle_robots(False)
        cookies = mechanize.CookieJar()
        self.browser.set_cookiejar(cookies)
        self.browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
        self.browser.set_handle_refresh(False)

    def login(self,username, password):
        print self.baseUrl
        self.browser.open(acadIITR.baseUrl + 'Default.aspx')
        for form in self.browser.forms():
            if form.attrs['id'] == 'form1':
                self.browser.form = form
                break
        self.browser.form['LoginView1$txtusername'] = username
        self.browser.form['LoginView1$password'] = password
        self.response = self.browser.submit()

    def subjectReg(self):
        self.response = self.browser.open(acadIITR.baseUrl + 'SubjectCorrection.aspx')
        soup = BeautifulSoup(self.response.read(),"lxml")
        table = soup.find(id = "maincontent_grdSubList")
        data = "Random : 0 ,Strongly Agree : 1 ,Agree : 2 ,Neutral :3,Disagree : 4,Strongly Disagree :5"
        for row in table.find_all("tr")[1:]:
            for professors in row.find_all("a"):
                if (professors):
                    print professors.text
                    option = raw_input(data)
                    self.responsePage(professors.get("href"), option)

    def responsePage(self, pageUrl, option):
        try:
            data = {u'maincontent_grdResponseA_rblResponseA_0_0_0'}
            self.response = self.browser.open(acadIITR.baseUrl + pageUrl)
            soup = BeautifulSoup(self.response.read(),"lxml")
            post_data = dict()
            for element in soup.find_all("input", {'type': 'hidden'}):
                post_data[element.get("name")] = element.get("value")

            for table in soup.find(id = 'maincontent_grdResponseA').find_all("table"):
                name = table.find("input").get("name")
                if option != 0:
                    post_data[name] = option
                else:
                    post_data[name] = random.randint(1, 5)

            for table in soup.find(id = 'maincontent_grdResponseB').find_all("table"):
                name = table.find("input").get("name")
                if option != 0:
                    post_data[name] = option
                else:
                    post_data[name] = random.randint(1, 5)

            print(post_data)
            self.response = self.browser.open(acadIITR.baseUrl + pageUrl, urllib.urlencode(post_data))
            self.browser.select_form(nr=0)
            self.response = self.browser.submit()
            self.print_response()
            print("done")
            sys.exit(0)
        except:
            print('An error occured.')


    def print_response(self):
        file=open("fb.html","w")
        file.write(self.response.read())
        file.close()


acad = acadIITR()
acad.login(sys.argv[1], sys.argv[2])
#acad.print_response()
acad.subjectReg()
#acad.print_response()