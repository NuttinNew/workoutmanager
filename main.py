#!/usr/bin/env python3
path = '~/work/python/workout/key.db'
key = open(path, 'x')

def file_opener():
    # opens key.db file
    db_dict = dict(read(key))
    for db in db_dict:
        
   
while True:
    # Menu
    print('----Workout Weight Tracker----')
    print('Press number to access that option')
    print('1.) Enter new weight(Existing Workout)')
    print('2.) Enter new workout')
    print('3.) Show maxes')
    print('4.) Remove Weight')
    print('5.) Remove Workout')
    print('6.) Display DataBase')
    print('7.) Quit')
    choice = input('--> ')
    choice = int(choice)

    if choice == 1:
        # New Weight
        print("Not available yet")
        
    elif choice == 2:
        # New Workout
        print("Not available yet")
        
    elif choice == 3:
        # Print Maxes
        print("Not available yet")
        

    elif choice == 4:
        # Remove Weight
        print("Not available yet")
        

    elif choice == 5:
        # Remove Workout
        print("Not available yet")
        

    elif choice == 6:
        # Display the database
        print(db.read())

    elif choice == 7:
        # Quit
        print('Stay Jacked')
        break

    else:
        print('Please input a number between 1 and 6\n')
