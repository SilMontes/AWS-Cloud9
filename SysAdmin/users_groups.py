import os


# Add a user
def new_user(): 
    cont = "Y" 
    while cont != "N": 
        username = input("Enter the name of the user to add: ") 
        print("Use the username '" + username + "'? (Y/N)") 
        confirm = input().upper()
        if(confirm == "Y"):
            os.system("sudo adduser " + username)
        else:
            print("User "+username+" not added")
        print('Would you like to add another user (Y/N)')
        cont = input().upper()

#delete a user
def remove_user(): 
    cont = "Y"
    while cont != "N": 
        username = input("Enter the name of the user to remove: ") 
        print("Remove the user: '" + username + "'? (Y/N)") 
        confirm = input().upper()
        if(confirm == "Y"):
            os.system("sudo userdel -r " + username)
        else:
            print("User "+username+" not removed")
        print('Would you like to remove another user (Y/N)')
        cont = input().upper()
        
        
# add user to a group
def add_user_to_group(): 
    username = input("Enter the name of the user that you want to add to a group: ") 
    # output: performs the groups command and saves the result to a vaiable
    # which is output later for the user to select from
    output = subprocess.Popen('groups', stdout=subprocess.PIPE).communicate()[0] 
    print("Enter a list of groups to add the user to") 
    print("The list should be separated by spaces, for example:\r\n group1 group2 group3")
    print("The available groups are:\r\n " + output) 
    chosenGroups = str(input("Groups: "))
    output = output.split(" ") 
    chosenGroups = chosenGroups.split(" ") 
    print("Add To:") 
    found = True 
    groupString = ""
    
    for grp in chosenGroups: # for each member of the chosenGroup array
        for existingGrp in output: # for each member of the output array
            if grp == existingGrp: # if the member exists in both groups
                found = True 
                print("-Existing Group : " + grp) 
                groupString += grp + ","
        if found == False: 
            print("-New Group : " + grp) 
            groupString += grp + ","
        else: 
            found = False
        
    groupString = groupString[:-1] + " " # removes the final command (,) and adds a space at the end of the line
    confirm = ""
    while confirm != "Y" and confirm != "N" : 
        print("Add user '" + username + "' to these groups? (Y/N)") 
        confirm = input().upper()
    if confirm == "N": 
        print("User '" + username + "' not added")
    elif confirm == "Y": 
        os.system("sudo usermod -aG " + groupString + username) 
        print("User " + username + " added")
