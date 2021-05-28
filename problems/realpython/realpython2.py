shout_response = input("What should I shout? ")


whisper_response = input("What should I whisper? ")
print(shout_response[0].upper() + shout_response[1:].lower())
print(shout_response.capitalize())
print(whisper_response[0:-1].lower() + whisper_response[-1].upper())

# last letter upper the rest lower

