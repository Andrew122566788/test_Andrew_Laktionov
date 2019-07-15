from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import bs4
import time


driver = webdriver.Firefox(executable_path='./geckodriver')
driver.get('https://rabota.ua/employer/login')

login_password = driver.find_element_by_id("ctl00_content_ZoneLogin_txPassword")
login_password.clear()
login_password.send_keys('Q2eV6uVXgge4Ze5')

login_username = driver.find_element_by_id("ctl00_content_ZoneLogin_txLogin")
login_username.clear()
login_username.send_keys('oksana@theadmasters.com', Keys.RETURN)

list_of_candidates = []
time.sleep(3)
driver.get('https://notebook.rabota.ua/employer/notepad/cvs?vacancyId=-1')
soup = bs4.BeautifulSoup(driver.page_source, "html.parser")
url_link = soup.find_all('a', class_="rua-p-t_16 rua-p-c-default ga_cv_view_cv")
for i in url_link:
    list_of_candidates.append(i.get('href'))


count = 2
for count in range(18):
    driver.get(f'https://notebook.rabota.ua/employer/notepad/cvs?vacancyId=-1&pg={count}')
    url = soup.find_all('a', class_="rua-p-t_16 rua-p-c-default ga_cv_view_cv")
    for i in url_link:
        list_of_candidates.append(i.get('href'))
    count += 1


with open("parse.txt", "w") as fp:
    fp.write('/n' + str(list_of_candidates) + '/n')




print(list_of_candidates)

driver.close()




