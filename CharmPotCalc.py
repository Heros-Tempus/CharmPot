class NotPositiveError(UserWarning):
    pass
print("Charming Potion Caclulator")
while True:
    
    goldToGreen = 0
    greenToCrimson = 0
    crimsonToBlue = 0
    
    while True:
        try:
            gold = int(input("Enter number of gold charms\n"))
            if gold < 0:
                raise NotPositiveError
        except ValueError:
            print("Not a positive integer.\n")
            continue
        except NotPositiveError:
            print("Not a positive integer.\n")
            continue
        else:
            break
    while True:
        try:
            green = int(input("Enter number of green charms\n"))
            if green < 0:
                raise NotPositiveError
        except ValueError:
            print("Not an integer.\n")
            continue
        except NotPositiveError:
            print("Not a positive integer.\n")
            continue
        else:
            break
    while True:
        try:
            crimson = int(input("Enter number of crimson charms\n"))
            if crimson < 0:
                raise NotPositiveError
        except ValueError:
            print("Not an integer.\n")
            continue
        except NotPositiveError:
            print("Not a positive integer.\n")
            continue
        else:
            break
    while True:
        try:
            blue = int(input("Enter number of blue charms\n"))
            if blue < 0:
                raise NotPositiveError
        except ValueError:
            print("Not an integer.\n")
            continue
        except NotPositiveError:
            print("Not a positive integer.\n")
            continue
        else:
            break

    minCharm = min(gold, green, crimson, blue) // 4
    print("Without transmutation, you can make at most " + str(minCharm) + " charming potions.")
    print("Which will give " + str(minCharm * 1000) + " herblore exp.\n")

    while True:
        if crimson > blue and crimson > 20:
            crimson = crimson - 20
            blue = blue + 10
            crimsonToBlue += 1
        elif green > crimson and green > 30:
            green = green - 30
            crimson = crimson + 10
            greenToCrimson += 1
        elif gold > green and gold > 20:
            gold = gold - 20
            green = green + 10
            goldToGreen += 1
        else:
            break

    maxCharm = min(gold, green, crimson, blue) // 4

    print("Efficiently transmuting these charms will produce:")
    print(str(gold) + " gold charms")
    print(str(green) + " green charms")
    print(str(crimson) + " crimson charms")
    print(str(blue) + " blue charms\n")
    print("You will transmute from gold to green " + str(goldToGreen) + " times.")
    print("You will transmute from green to crimson " + str(greenToCrimson) + " times.")
    print("You will transmute from crimson to blue " + str(crimsonToBlue) + " times.\n")
    print("This will require " + str(250 * goldToGreen) + " vibrant energy, " + str(750 * greenToCrimson) + " lustrous energy, and " + str(1500 * crimsonToBlue) + " brilliant energy.\n")
    print("With transmutation, you can make at most " + str(maxCharm) + " charming potions.")
    print("This will give " + str(maxCharm * 1000) + " herblore exp. Which is an increase of " + str((maxCharm - minCharm) * 1000) + " exp.")
    answer = input("perform new calculation? (y/n):") 
    if answer not in ('y', 'n'):
        print ("Invalid input.") 
        break
    if answer == 'y':
        continue
    else:
        print ("Goodbye") 
        break
