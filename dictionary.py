#Joel Avery #CSD 205
#11/14/22

#This program creates a dictionary with 15 nfl teams and locations
#The program then displays all key values and then asks the user to select a key
#and then displays the value paired to the key. 

#created a dictionary with 15 key, value nfl teams and where they are from. 
nfl_teams = {
    'titans': 'tennessee',
    'chiefs': 'kansas city',
    'ravens': 'baltimore', 
    'rams': 'los angeles', 
    'colts': 'indianapolis', 
    'jets': 'new york', 
    'giants': 'new york', 
    'packers': 'green bay', 
    'cowboys': 'dallas', 
    'texans': 'houston', 
    'saints': 'new orleans', 
    'commanders': 'washington', 
    'seahawks': 'seattle', 
    'eagles': 'philadelphia', 
    'dolphins': 'miami', 
    }

print() # for space. 

loop_active = True #created this variable to enter the while loop. 

#loop through the dictionary. 
for team, location in nfl_teams.items(): 
    location = nfl_teams.values() # sets the location to the value of the pair. 
    print(team.title()) # prints the team in title format. 

print() # blank print statement for space. 

#if loop_active is true we enter the while loop. 
while loop_active:

    # ask for input and store it as team. 
    team = input("Please select a team to see where they are from: \n")
    team = team.lower() # takes whatever the input is and puts in lower case. 

    # while the team is not in the dictionary off the input we enter the loop. 
    # this helps us with input validation. 
    while team not in nfl_teams:
        print("\nPlease enter a team from the selection above.\n")
        team = input("\nPlease select a team to see where they are from:\n")
        team = team.lower()

    # prints the team and location of the team. 
    print(f"\nThe {team.title()} are from {nfl_teams[team].title()}.\n")

    #creates a repeat variable to either continue or exit the loop. 
    repeat = input("Type yes to continue or press anything else to exit.\n")
    print()

    #conditional if repeat does not equal yes, then we exit the loop. 
    if repeat != 'yes': 
        loop_active = False 
       

    
