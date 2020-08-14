import os, time, re
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from ClassmateSearch.config import getUsername
from ClassmateSearch.config import getPassword

def scrape():

    class_ids = []
    path = os.path.dirname(os.path.abspath(os.getcwd()))

    ## Webdriver Config
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)


    ## LogIn to MyCPP with SSO
    driver.get('https://my.cpp.edu')
    time.sleep(2)
    if (driver.find_element_by_name('_eventId_proceed')!= None):
        driver.find_element_by_id('username').send_keys(getUsername())
        driver.find_element_by_id ('password').send_keys(getPassword())
        driver.find_element_by_name('_eventId_proceed').click()

    ## Access Blackboard
        driver.get('https://blackboard.cpp.edu/auth-saml/saml/login?apId=_172_1&redirectUrl=https%3A%2F%2Fblackboard.cpp.edu%2Fwebapps%2Fportal%2Fexecute%2FdefaultTab')
        time.sleep(2)
        source = driver.find_element_by_id('My_Courses_Tools')
        courses = source.get_attribute('outerHTML').split('Course&amp')

    ## Reduce HTML Source to Course List
        for course in courses:
            reduced = course.split(';url=')[0]
            if ';id=' in reduced :
                class_ids.append(reduced.replace('&amp','').replace(';id=',''))

    ## Access the rosters
    for id in class_ids:
        url = 'https://blackboard.cpp.edu/webapps/blackboard/execute/displayEmail?navItem=email_select_students&course_id={}'.format(id)
        driver.get(url)
        courseName = driver.page_source.split('Select Users ')[1].split('.')[0]
        fileName = courseName.replace('– ','').replace(' ','')
        dump = driver.page_source.split('<select name="USERS_AVAIL" size="8" id="USERS_AVAIL" multiple="multiple" style="visibility: hidden;">\n')[1].split('</select>')[0]
        with open('{}/TXT_Input/{}.txt'.format(path,fileName),'w') as txt:
            txt.write(dump[:-11])
    driver.close()
