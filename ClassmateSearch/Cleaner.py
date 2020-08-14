# Cleaner.py
# Used to convert HTML-Littered Class Roster to JSON File

# Instructions:
# Roster Available on Blackboard at /webapps/blackboard/execute/displayEmail?navItem=email_select_students&course_id=
# View Page Source and Copy the Options in USERS_AVAIL
# Save to a .txt file in TXT_Input

import os, json, re

def clean():
    path = os.path.dirname(os.path.abspath(os.getcwd()))
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
