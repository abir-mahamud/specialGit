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

