# FindClassmates.py
# Parses Rosters to Identify Names of Girls in Class with ~70% Accuracy
# Accuracy Deficit Caused by Unisex Names and Obscure Names

import os, json

def findClassmates(path, girls = True, includeUnisex = False):
    targetDir = '{}/JSON_Output'.format(path)

    with open('{}/Find_Classmates/girls_names.json'.format(path),'r') as masterList: # Open the List of Girl's Names
        with open('{}/Find_Classmates/unisex_names.json'.format(path),'r') as unisexList:
            unisexNames = json.loads(unisexList.read())
            names = json.loads(masterList.read())
            for file in os.listdir(targetDir): # Iterate Over Each JSON in JSON_Output
                targetFile = '{}/{}'.format(targetDir,file)
                with open(targetFile,'r') as classes:
                    roster = json.loads(classes.read())
                    for name in roster:
                        first = name.split(" ")[0]
                        if not girls or first in names: # If Somebody's First Name is in the List of Girl's Names, Print it
                            if includeUnisex or first not in unisexNames:
                                print('{} is in {}'.format(name,file.split('.')[0]))
