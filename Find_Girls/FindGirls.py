# FindGirls.py
# Parses Rosters to Identify Names of Girls in Class with ~70% Accuracy
# Accuracy Deficit Caused by Unisex Names and Obscure Names

import os, json

path = os.path.dirname(os.path.abspath(os.getcwd()))
targetDir = '{}/JSON_Output'.format(path)
includeUnisex = False # Set this to true to ignore unisex names

with open('girls_names.json','r') as masterList: # Open the List of Girl's Names
    with open('unisex_names.json','r') as unisexList:
        unisexNames = json.loads(unisexList.read())
        names = json.loads(masterList.read())
        for file in os.listdir(targetDir): # Iterate Over Each JSON in JSON_Output
            targetFile = '{}/{}'.format(targetDir,file)
            with open(targetFile,'r') as classes:
                roster = json.loads(classes.read())
                for name in roster:
                    first = name.split(" ")[0]
                    if first in names: # If Somebody's First Name is in the List of Girl's Names, Print it
                        if includeUnisex or first not in unisexNames:
                            print('{} is in {}'.format(name,file.split('.')[0]))
