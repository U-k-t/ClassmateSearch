import subprocess, sys, platform, os, shutil
from ClassmateSearch.Scraper import scrape
from ClassmateSearch.Cleaner import clean
from Find_Overlap.FindOverlap import overlap
from Find_Classmates.FindClassmates import findClassmates
def main():
    path = os.path.abspath(os.getcwd())
    req_path = "{}/ClassmateSearch/chromedriver".format(path)

    if platform.system() == 'Windows':
        print('Sorry, Scraping is for Unix Only')
        exit()
    elif os.path.exists('/usr/local/bin/chromedriver'):
        sys.path.append('/usr/local/bin')
        print('Chromedriver Requirement Satisfied\n')
    else:
        sys.path.append('/usr/local/bin')
        shutil.copy2(req_path, '/usr/local/bin/chromedriver')
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
    With that out of the way, have fun and happy searching!\n''')
    toScrape = ''
    while True:
        toScrape = input('Would you like to scrape Blackboard for rosters? (y/n): ')
        if toScrape is 'y':
            print('\nBeginning Scrapping Process\n')
            scrape(path)
            print('\nDone Scraping\n')
            break
        elif toScrape is 'n':
            break
        else:
            print('Wrong input; please enter \'y\' or \'n\'\n')
    while True:
        toScrape = input('Would you like to parse your text files to JSON format (do this if you don\'t already have JSON files in JSON output)? (y/n): ')
        if toScrape is 'y':
            print('\nProcessing Files as JSON')
            clean(path)
            print('Done Processing Files')
            break
        elif toScrape is 'n':
            break
        else:
            print('Wrong input; please enter \'y\' or \'n\'\n')
    menu(path)
def menu(path):
    while True:
        print('''\nMENU:\n
        0: Exit\n
        1: Find Classmates With Overlapping Classes\n
        2: Find Girls in Your Classes (~70% Accuracy)\n
        3: Find Guys in Your Classes\n''')
        selection = input('Select Menu Option [0-3]: ')
        if selection is '0':
            print('\nThank You for Using This Program!')
            exit()
        elif selection is '1':
            print('')
            overlap(path)
        elif selection is '2':
            print('')
            findClassmates(path, True)
        elif selection is '3':
            print('')
            findClassmates(path, False, True)
        else:
            print('Invalid Menu Option. Please Try Again')
main()
