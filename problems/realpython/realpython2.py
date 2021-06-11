# shout_response = input("What should I shout?")
# whisper_response = input("What should I whisper? ")
# print(shout_response[0].upper() + shout_response[1:].lower())
# print(shout_response.capitalize())
# print(whisper_response[0:-1].lower() + whisper_response[-1].upper())

# last letter upper the rest lower
# weight = 500
# animal = "gorilla"

# print(float(weight), "is the weight of the", str(animal))
# print("{} is the weight of the {}".format(weight, animal))
# print("{0} is the weight of the {1}".format(weight, animal))
# print("{weight2} is the weight of the {animal2}".format(weight2=300, animal2="tiger"))
# print(f"{weight} is the weight of the {animal}")



# phrase = "the surprise is in here somewhere (surprise!)"
# print(phrase.find("Surprise"))

# number = "My phone number is 555-838-3984"
# print(number.find("5"))

# phrase2 = "good luck trying to pronounce ejafjallajokull to to to"
# # print(phrase2.find("ejafjalllajokull"))

# # utensil = "I have a pink writing utensil"
# # print(utensil.find("pink"))

# phrase3 = phrase2.replace('to', "boo")
# print(phrase2)
# print(phrase3)


# 1. In one line, display the result of trying to
# find()
# the substring "a" in the string
# "AAA"; the result should be -1

# phrase="AAA"
# print(phrase.find("a"))

# user_input = input("do you love chocolate cake?\n")
# print(user_input.find("l"))


# 2. Create a string object that contains the value "version 2.0";
# find()
# the first
# occurrence of the number 2.0 inside of this string by first creating a "float" object that
# stores the value 2.0 as a floating-point number, then converting that object to a
# string using the
# str()
# function

# something = "version 2.0"
# number = 2.0
# print(something.find(str(number)))

# 3. Write and test a script that accepts user input using
# result of trying to
# find()
# input()
# , then displays the
# a particular letter in that input

# Assignment: Leet Haxor

# a = 4
# b = 8
# e = 3
# l = 1
# o = 0
# s = 5
# t = 7

user_input = input("Enter some text: ")

y = (user_input
        .replace("a", "4")
        .replace("b", "8")
        .replace("e", "3")
        .replace("l", "1")
        .replace("o", "0")
        .replace("s", "5")
        .replace("t", "7")
    )

print(y)


