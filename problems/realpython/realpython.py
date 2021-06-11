print(len("Hello world"))

my_string = 'I\'m a string!!!    '
my_string_2 = "I'm a string!!!     "
print(len(my_string))
print(len(my_string_2))

print(3 + len(my_string))

a_third_thing = my_string + my_string_2 + "three things " + my_string_2
print(my_string + my_string_2)


a_fourth_thing = str(len(my_string_2)) + " " + str(len(my_string))
print(a_fourth_thing)

my_number = (15)
my_numbers_length = len(my_number)
my_string = str(my_numbers_length)
print(str(len(str(15))))
print(my_string)


print("hi")
