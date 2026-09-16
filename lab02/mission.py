##Troy
##Introduction to Programming
##Super secret mission

name = input('What is your name agent: ')
age = int(input('How old are you: '))
training_years = int(input('How many years have you been training: '))
fav_color = input('What is your favorite color: ')
num_gadgets = int(input('How many gadgets are you carrying: '))
minutes = int(input('How many minutes do you have: '))

#Mission stats
training_percentage = training_years / age

if training_years > 0:
    gadget_density = num_gadgets / training_years
else:
    gadget_density = 0

mission_seconds = minutes * 60


mission_code = f'{name.upper()}-{fav_color.upper()}-{str(age)}'

#Boolean Expressions
is_adult = age >= 18
has_many_gadgets = num_gadgets >= 5
has_training_experience = training_years > 0



#Output
print(f'''====================================
        SECRET MISSION BRIEFING
====================================
 
Agent: {name}
Mission Code: {mission_code}
 
Age: {age}
Training: {training_years} years
Training Percentage: {training_percentage * 100}%
 
Gadgets: {num_gadgets}
Gadget Density: {gadget_density} per training year
 
Mission Time: 37 minutes
Mission Time Remaining: {minutes} minutes
Mission Time in Seconds: {mission_seconds}

Adult Agent: {is_adult}
Many Gadgets: {has_many_gadgets}
Training Experience: {has_training_experience}
 
====================================
        GOOD LUCK, AGENT!
====================================''')