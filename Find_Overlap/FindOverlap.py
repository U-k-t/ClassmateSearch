# FindOverlap.py
# Parses Rosters to Identify Names of Classmates that Share Multiple Classmates with User

import os, json

def overlap(path):
    targetDir = '{}/JSON_Output'.format(path)
    classmates = {}

    for file in os.listdir(targetDir): # Iterate over Files in /JSON_Output
        targetFile = '{}/{}'.format(targetDir,file)
        with open(targetFile,'r') as classes:
            roster = json.loads(classes.read())
            for name in roster: # Create Key-Value Pairs in the Format {Name: [Class]}
                if name not in classmates:
                    classmates.update({name:[file.split('.')[0]]})
                else:
                    classmates[name].append(file.split('.')[0]) # Add Classes to List if Key Exists

    for classmate in classmates: # Iterate Over Keys
        courses = classmates[classmate]
        if len(courses)>1: # If Classmate Shares More Than One Class, Output Their Name and Classes Shared
            output = "{} is in ".format(classmate)
            if len(courses)==2:
                output+= "{} and {}.".format(courses[0],courses[1])
                print(output)
                continue
            for crn in courses:
                print("Hello")
                if crn != (courses[-1] or courses[-2]):
                    output+= "{}, ".format(crn)
                elif crn == courses[-2]:
                    output+="{}, and".format(crn)
                else:
                    output+="{}.".format(crn)
