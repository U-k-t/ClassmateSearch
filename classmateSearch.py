import subprocess, sys, platform, os, shutil
from ClassmateSearch.Scraper import scrape
from ClassmateSearch.Cleaner import clean

path = "{}/ClassmateSearch/chromedriver".format(os.path.abspath(os.getcwd()))

if platform.system() == 'Windows':
    print('Sorry, Scraping is for Unix Only')
    exit()
elif os.path.exists(path) and '/usr/local/bin' in sys.path:
    shutil.move(path, '/usr/local/bin/chromedriver')
    print('Moved chromedriver to ~/usr/local/bin')

## Install Required Libraries
with open("requirements.txt",'r') as requirements:
    for requirement in enumerate(requirements):
        package = requirement[1].replace('\n','')
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

print('''\n\n\n\n
\nWelcome to Classmate Search!
This program allows you to scrape your Blackboard Rosters to query who is in your class!
The program will prompt you for your CPP login information, but please be informed, it does not save your login information anywhere. We don't connect to any databases or anything.
Your login information is solely used to log in to Blackboard via SSO using a webdriver.
With that out of the way, have fun and happy searching!''')

print('\nBeginning Roster Scraping....\n\n')
scrape()
print('\nScraping Completed.\n')


print('\n\nReformatting Rosters to JSON....\n\n')
scrape()
print('\nReformatting Completed.\n')
