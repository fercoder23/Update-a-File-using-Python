# Code to check whether the allow list contains any IP addresses identified on the remove list. 

# Assign 'import_file' to the name of the text file.

import_file = "allow_list.txt"

# Assign 'remove_list' to the list of IP addresses that are no longer allowed to access restricted information.

remove_list = "remove_list.txt"

# Open txt allow_list.txt and remove_list.txt in read mode and asign that to a variable. 

with open(import_file, "r")as file:
    allow_ips = file.read()

with open(remove_list, "r")as file:
    remove_ips = file.read()

# Converting string into list
# By using 'split()', we will convert 'allow_ips' and 'remove_ips' from a string to a list

allow_ips = allow_ips.split()

remove_ips = remove_ips.split()

# Build iterative statement 
# Name loop variable 'element'
# Loop through 'allow_ips' 

# 'if' statement will check if any element is within the remove_ips variable and if true, 
# it will remove that element within the 'allow_ips'

for element in allow_ips:
    if element in remove_ips:
        allow_ips.remove(element)


# Converting 'allow_ips' into string to update the original allow_list.txt with the updated list.

allow_ips = "\n".join(allow_ips)


# Build 'with' statement to rewrite the original file

with open(import_file, 'w') as file:
    
    # Rewrite the file, replacing its contents with 'ip_addresses'
    file.write(allow_ips)
