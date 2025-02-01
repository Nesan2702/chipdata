country_name="italy"


while True:
    name=input("guess the country name")
    if name == country_name:
        print("you guessed the correct answer")
        break

    else:
        print("your answer is wrong ,try again")


