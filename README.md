# Classmate Search
> Used for parsing Blackboard rosters to identify classmates of interest

I've been fiddling around with using Python to scrap together what are kinda janky applications to automate processes. Spamming Google surveys with responses using post requests, automating the mass downloading of Assist.org agreements, etc. One thing I automated at the beginning of Spring 2020 while waiting for a professor to arrive on the first day was checking my course rosters to find any classmates I may have an overlap with. However, the program was inefficient (to the point where I named it InefficientCheck.py) and required a lot of formatting, so it was really a "one-time use" type of deal.

With the start of Fall 2020 coming around, everything is online due to COVID-19. Only <em>ONE</em> professor left "Email Select Users" enabled on Blackboard. However, I wasn't about to let that stop me. One professor left "Email the Instructor" enabled; that was easy: you can access "Select Users" via a 2 clicks of a hyperlink at the top of the page. Upon further analysis, I noticed a trend in URL patterns and tried it for the classes that left no easily-followable hyperlinks visible to students - it worked. I started cleaning the rosters using Atom's regex find and replace, and we were off to the races.


## Development setup

Everything is within the Python Standard Library


## Instructions

* Go to your Blackboard Class
* Access the "Email Select Users" at
```
/webapps/blackboard/execute/displayEmail?navItem=email_select_students&course_id={YOUR CLASS ID HERE}
```
* View Page Source and Copy the Options in USERS_AVAIL
* Save the Text to a .txt File in TXT_Input
* Repeat for All Other Classes
* Run Cleaner.py to Format the Text Files as JSON
* Navigate Directories and Run Either FindOverlap.py or FindGirls.Py

Example Text Inputs are Included

## Release History

* 0.1.0
    * Initial Release - FindGirls.Py and FindOverlap.Py

## Known Bugs

* FindGirls.py Will Omit Some Girls with Obscure Names and Names Included on the Unisex List. A Variable can be Changed to Adjust the Output of Unisex Names.
