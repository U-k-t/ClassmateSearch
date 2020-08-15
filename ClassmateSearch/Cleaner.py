# Cleaner.py
# Used to convert HTML-Littered Class Roster to JSON File

import os, json, re

def clean(path):
    htmlMatch = re.compile('\<(.*?)\>')

    for file in os.listdir("{}/TXT_input".format(path)): #Iterate Over Files In TXT_Input
        output = []
        className = file.strip('.txt')
        with open('{}/TXT_Input/{}.txt'.format(path, className),'r') as input:
            for line in enumerate(input): # Clean the Names Line by Line
                cleaned = re.sub(htmlMatch,"",line[1].replace("            ","").replace(", ",",")).split(',')
                output.append('{} {}'.format(cleaned[1].replace('\n',''), cleaned[0])) #Append them as "FirstName LastName"
        with open('{}/JSON_Output/{}.json'.format(path, className),'w') as file:
            json.dump(output,file) # Write to JSON file in /JSON_output
