import mechanize
from bs4 import BeautifulSoup
import sys

browser = mechanize.Browser()
browser.set_handle_robots(False)
cookies = mechanize.CookieJar()
browser.set_cookiejar(cookies)
browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.517.41 Safari/534.7')]
browser.set_handle_refresh(False)

url = 'http://acad.iitr.ac.in/Student/'
browser.open(url + 'Default.aspx')
for form in browser.forms():
    if form.attrs['id'] == 'form1':
        browser.form = form
        break

browser.form['LoginView1$txtusername'] = sys.argv[1]
browser.form['LoginView1$password'] = sys.argv[2]
response = browser.submit()
response = browser.open(url + "SubjectCorrection.aspx")
soup = BeautifulSoup(response)
table = soup.find(id="maincontent_grdSubList")
for row in table.find_all("tr")[1:]:
    print row.find_all("td")[5].find("a")
file=open("fb.html","w")
file.write(response.read())
file.close()

