#Numbers and Math

print("I will now count my chickens:")

print("Hens",25 + 30 / 6)
print("Roosters", 100 -25 * 3 % 4)

print("Now i will count the eggs:")

print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, That's why it's False. ")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)



#Variables &names
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("We can transport", carpool_capacity, "people today")
print("we need to put about", average_passengers_per_car, "in each car")



#More variables & printing
Crush_name = 'Mumu'
her_age = 23 #probably
her_height = 61 #inches
her_weight = 127 #lbs
her_eyes = 'Black'
her_smile = 'amazing'
her_hair = 'Black'

print(f"Let's talk about {Crush_name}")
print(f"She's {her_height} inches tall")
print(f"She's {her_weight} pounds heavy")
print("Actually i love her chubbiness")
print(f"She's got {her_hair} hair & {her_smile} smile")

#this is a tricky one, there is no inverted comma
total = her_age + her_height + her_weight
print(f"If i add {her_age}, {her_height} and {her_weight} I get {total}")



#String & text
types_of_girls = 2
x = f"there are {types_of_girls} types og girls"

hot_chicks = "Korra Maal"
cute_and_pretty = "Shundori's"
y = f"One is {hot_chicks} another one is {cute_and_pretty}"

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = True
speech_evalution = "Is that statement is right? {}"
print(speech_evalution.format(hilarious))

w = "sometimes i love korra maal "
e = "sometimes both"
print(w + e)




#More printing

print("Mary is such a hot milf")
snow = True
print("it's fleece was white as {}.".format(snow))
print("and everywhere that mary went")
print("." * 10)

end1 = "H"
end2 = "o"
end3 = "t"
end4 = "M"
end5 = "i"
end6 = "l"
end7 = "f"
end8 = "L"
end9 = "o"
end10 = "v"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3, end=' ')
print(end4 + end5 + end6 + end7, end=' ')
print(end8 + end9 + end10 + end11 + end12)



#Printing Printing 
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, True, True))
print(formatter.format("this stge is", "so hard", "but don't", "loose confidence" ))




#Asking questions
print("How old are you?", end='')
age = input()
print("How tall are you?", end='')
height = input()
print("How much do you weigh?", end='')
weight = input()

print(f"So, you're {age} year's old, {height} tall and {weight} heavy.")



#Prompting People
age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")

print(f"So, you're {age}years old, {height}inch tall and {weight}lbs heavy")





#Reading & Writing Files

from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, Hit RETURN")

input("?")

print("Opening the file...")
target = open(filename, 'w') #permission to write

print("Truncating the file. Goodbye!")
target.truncate() #with or without this it will run

print("Now I'm going to ask you three lines.")

line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()

### Command Line Run --- Ex. python Basic.py(filename) convert.txt(converted_file_name)




# Name Variables Code Functions
# this one is like my scripts with argv
def first_function(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, args2: {arg2}")

# ok, that *args is actually pointless, we can just do this
def second_function(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this one takes one argument
def third_function(arg1):
    print(f"arg1: {arg1}")

# this one take no arguments
def fourth_function():
    print("I got nothin")

first_function("Bidgette", "B")
second_function("Britney", "Amber")
third_function("Milf")
fourth_function()



# Functions and variables
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket.\n")

print("We can just give the function numbers correctly:")
amount_of_cheese = 10    or  # int(input("amount of cheese:"))
amount_of_crackers = 20  or  # int(input("amount of crackers:"))

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)





#Functions can return something
def add(a,b):
    print(f"Adding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

print(f"Let's do some math with just functions!")

age = add(20, 2)
height = subtract(78, 4)
weight = multiply(120, 2)
iq = divide(146, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

# A puzzel for the extra credit, type it anyway.
print("Here is a puzzel.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
print("That becomes", what, "Can you do it by hand?")





#What IF
people = 20
milf = 25
hot_chicks = 19

if people < milf:
    print("I love 'em")

if people > milf:
    print("That's disappointing")

if people < hot_chicks:
    print("oh babes! let's do something naughty")

if people > hot_chicks:
    print("have to move Las Vegas")

hot_chicks += 1

if people >= hot_chicks:
    print("people are greater than or equal to hot chicks")

if people <= hot_chicks:
    print("may be that's interisting")

if people == hot_chicks:
    print("all of them are hot_chicks")

    
    
        

#Else and if
men = 30
women = 40
hot_women = 15

if women > men:
    print("we should take care of them and our wives as well")

elif women < men:
    print("poor luck man")

else:
    print("it's not happening")

if hot_women > women:
    print("majority will get the priority")

elif hot_women < women:
    print("you guy's needs to be hot")
else :
    print("That's not happening either")

if men > hot_women:
    print("you have to be lucky enough")
else:
    print("me to hot women: you're not alone")
    
    
    
        
    
#Making Decisions
print("As you're a renowned film director in town. Two girls came to you as both wants to be actress and you're gonna choose one from Girl #1 and Girl #2")

girl = input("> ")

if girl == "1":
    print("She is damn hot milf")
    print("Now what do you do?")
    print("1.Ask for give and take in return")
    print("2.Fuck her instant")

    hot_milf = input("> ")

    if hot_milf == "1":
        print("You're straight forward")

    elif hot_milf == "2":    
        print("You're damn bro")

    else:
        print(f"Well!! This is insane, {hot_milf} mr.director!")

elif girl == "2":
    print("She is your ex and now she is more hot")
    print("Now what do you do?")
    print("1.Insult her")
    print("2.Fall in love again")
    print("3.As she becomes more hot so fuck her then cast her for your movie and fuck till the end")
    
    ex = input("> ")

    if ex == "1" or ex == "2":
        print("You're an asshole")
    
    else:
        print("Congrats mr.director! Enjoy")

else:
    print("OH you pressed enter without giving an input")

    
    
    
#Loop and Lists
the_count = [1, 2, 3, 4, 5]
top_milf = ['britney', 'bridgette', 'lena', 'audrey']
position = [1, 'mumu', 2, 'piya bipasha', 3, 'badhon']

#this first kind of for-loop goes through a list
for number in the_count:
    print(f"This is count {number}")

#same as above
for milf in top_milf:
    print(f"Top milf women are: {milf}")

#also we can go through mixed list too
#noitce we have to use {} since we dont know whats in it
for milf in position:
    print(f"Positions in ascending order {milf}")


#we can also build lists, first start with an empty one
elements = []
#then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list")
    #append is a function that lists understand
    elements.append(i)

#now we can print them out too
for i in elements:
    print(f"Element was: {i}")



    
 

#While Loops
my_girlfriend = 0
gf_list = []

while my_girlfriend < 13:
    print(f"Babe let's count my ex's: {my_girlfriend}")
    gf_list.append(my_girlfriend) # The append() method adds a single item to the end of the list.

    my_girlfriend = my_girlfriend + 1

    print("So Counting my ex's no. ", gf_list)
    print(f"and still counting... {my_girlfriend}")

print("Final list till now: ")

for my_girls in gf_list:
    print(my_girls)

    
    
    
# Branches and Functions
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man!Learn to type a number")
    
    if how_much < 50:
        print("Nice! You're not greedy")
        exit(0)
    else:
        dead("You greedy bastard")

def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")

def cthulu_room():
    print("Here you see the great evil Cthulu")
    print("He, it, whatever stares at you and go insane")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty")
    else:
        cthulu_room()

def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room")
    print("There is a door to your right and left")
    print("Which one do you take?")

    choice = input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve")

start()





# Dictionary 
#create a mapping of website to abbreviation
sites = {
    'Naughty America': 'NA',
    'Brazzers': 'BR',
    'Xvideos': 'XV',
    'Bangbros': 'BGR',
    'Porn Hub': 'PH'

}

#create a basic set of sites and some stars in them
stars = {
    'BR': 'Leana Paul',
    'XV': 'Brooke Beretta',
    'PH': 'Skyla Novea'
}

#add some more stars
stars['BGR'] = 'Anissa Kate'
stars['NA'] = 'Desiree Dulce'

#print out some stars
print('-' * 10)
print("NA site has: ", stars['NA'])
print("BR site has: ", stars['BR'])

#print some sites
print('-' * 10)
print("Naughty America's abbreviation is: ", sites['Naughty America'])
print("Bangbros abbreviation is: ", sites['Bangbros'])

#do it by using the star's name then sites dict
print('-' * 10)
print("Bangbros has: ", stars[sites['Bangbros']])
print("Brazzers has: ", stars[sites['Brazzers']])

#print every site abbreviation
print('-' * 10)
for site, abbrev in list(sites.items()):
    print(f"{site} has abbreviated {abbrev}")

#print every star in site
print('-' * 10)
for abbrev, star in list(stars.items()):
    print(f"{abbrev} has the stars {star}")

#now do both at the same time
print('-' * 10)
for site, abbrev in list(sites.items()):
    print(f"{site} site is abbreviated {abbrev}")
    print(f"and has stars {stars[abbrev]}")

print('-' * 10)
#safely get a abbreviation by site that might not be there
site = sites.get('pornhd')
if not site:
    print("Sorry, no pornhd")

#get a star with a default value
star = stars.get('PHD', 'Does not exist')
print(f"The star for the site 'PHD' is: {star}")




# Modules,Clsses and Objects
#MODULES
#get boobs from dictionary
mystuff = {'boobs': "I Love Boobs!"}
print(mystuff['boobs'])

#PreDefence1.tits() --- get tits from the module cuz this goes in PreDefence1.py
def tits():
    print("wanna squeeze?")

import PreDefence1
PreDefence1.tits()

#PreDefence1.pervert ---same thing its just a variable
def tits():
    print("wanna squeeze?")

pervert = "Yes!! i do!" #this is just a variable

import PreDefence1
PreDefence1.tits()

print(PreDefence1.pervert)

