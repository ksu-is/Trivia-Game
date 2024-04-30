def game():
    global total
    global count
    global genre_choice
    while count < 4:
        print("The categories are: Science, History, Pop Culture, and Sports")
        genre_choice = input("Chose a category: ")
        genre()
    return total
        
def genre():
    global total
    global count
    if genre_choice == "Science":
        Science()
    elif genre_choice == "History":
        History()
    elif genre_choice == "Pop Culture":
        Pop_Culture()
    elif genre_choice == "Sports":
        Sports()
    else:
        print(genre_choice)

def Science():
    global total
    global count
    if genre_choice == "Science":
        print("You chose Science")
        print("Your question is: What element makes up the majority of Earth's air?")
        answer = input("Is it Oxygen, Nitrogen, Helium, or Carbon Dioxide? ")
        if answer == "Nitrogen":
            total += 1
            print("Correct!")
            print("Your score is now: ", total)
            count += 1
        else:
            print("Incorrect")     
            count += 1
def History():
    global total
    global count
    if genre_choice == "History":
        print("You chose History")
        print("Your question is: Who was not a world leader during World War II?")
        answer = input("Was it Roosevelt, Mussolini, Stalin, or Gorbachev? ")
        if answer == "Gorbachev":
            total += 1
            print("Correct!")
            print("Your score is now: ", total)
            count += 1
        else:
            print("Incorrect")     
            count += 1

def Pop_Culture():
    global total
    global count
    if genre_choice == "Pop Culture":
        print("You chose Pop Culture")
        print("Your question is: Who is currently topping the Billboard Arttist 100 list?")
        answer = input("Is it Taylor Swift, Morgan Wallen, Drake, or SZA? ")
        if answer == "Taylor Swift":
            total += 1
            print("Correct!")
            print("Your score is now: ", total)
            count += 1
        else:
            print("Incorrect")     
            count += 1

def Sports():
    global total
    global count
    if genre_choice == "Sports":
        print("You chose Sports")
        print("Your question is: What team won the World Series last year?) (2023 season)")
        answer = input("Was it the Philadelphia Phillies, the Texas Rangers, the Atlanta Braves, or the Seattle Mariners? ")
        if answer == "Taylor Swift":
            total += 1
            print("Correct!")
            print("Your score is now: ", total)
            count += 1
        else:
            print("Incorrect")     
            count += 1


total = 0
count = 0
#print("The categories are: Science, History, Pop Culture, and Sports")
genre_choice = ""
game()
