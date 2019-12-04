import random
file = open("allPossibleSymbols.txt","r") #Opens file
sylList = file.read().split("\n")
sylList.pop(0) #Encoding error right now
print("Syllables loaded!",sylList)
end = 'Thank you for using this program. You will be returned to the main menu.'
def checker():
    repeatCheck = True  
    while True:
        fullError = False
        found = False
        count = 0
        sylTrue = []
        sylFalse = []
        syl = []
        slash = False



        chosenWord = str(input("[- to cancel] Please enter your word, with . for syllable spaces in the romanised form: ").strip())
        if chosenWord == '-':
            print(end)
            break
        syl = chosenWord.split(".")
        

        
        for letter in chosenWord:
            if letter in ['/','[',']']:
                slash = True
        if chosenWord not in sylList:
            for letter in chosenWord:
                if letter == '.':
                    count += 1
            if count < 1 and chosenWord not in sylList:
                fullError = True
        for item in syl:
            if item in sylList:
                sylTrue.append(item)
            else:
                sylFalse.append(item)
        if sylFalse != []:
            found = False
        if sylFalse == []:
            found = True
        
        
        
        if slash:
            print("You included IPA symbols such as /, [, or ]. Please try again.")
            continue
        if fullError:
            print("You forgot to include a syllable break. Please try again.")
            continue
        if (not fullError) and (not slash):
            print("Word:",chosenWord,"\nSyllables split into",syl,"\nAll syllables found:",sylTrue,"\nAll syllables not found:",sylFalse)
            if found:
                print("The word works!")
            if not found:
                print("The word doesn't work.")
        
        if repeatCheck:
                repeat = input("Press Y to repeat, or I to iterate. ").strip().upper()
                try:
                    repeat = repeat[0]
                    if repeat not in ['Y','I']:
                        print(end)
                        break
                except:
                    print(end)
                    break
                if repeat == 'I':
                    print("This program will now iterate. You will not see this again.")
                    repeatCheck = False
                    continue 
                elif repeat == "Y":
                    continue
def shuffle():
    moreCheck = True
    repeatCheck = True
    while True:
        sylRand = sylList
        random.shuffle(sylRand)
        print("Shuffling all syllables...")
        print("Here are the first 20 syllables:\n",sylRand[0:19])
        if moreCheck:
            more = input("Press Y to see the rest, and A to iterate (or nothing to return to the main menu): ").upper().strip()
            try:
                    more = more[0]
                    if more not in ['Y','A']:
                        print(end)
                        break
            except:
                print(end)
                break
            if more == 'A':
                print("For now, this will always show the full list of",len(sylList),"syllables.")
                moreCheck = False
                print("Here is the full list:\n",sylRand) 
            elif more == "Y":
                print("Here is the full list:\n",sylRand) 
        if repeatCheck:
                repeat = input("Press Y to repeat, or I to iterate. ").strip().upper()
                try:
                    repeat = repeat[0]
                    if repeat not in ['Y','I']:
                        print(end)
                        break
                except:
                    print(end)
                    break
                if repeat == 'I':
                    print("This program will now iterate. You will not see this again.")
                    repeatCheck = False
                    continue 
                elif repeat == "Y":
                    continue
        
while True:
    print("Welcome to the Sinkebwnya syllable program v2.0.0! Here are the options:\n\n[0] Check if words work\n[1] Shuffle syllable list \n[2] Show syllables\n[3] Exit")        
    option = input("Which one shall you choose? Please select the number: ").strip()
    try:
        option = int(option)
    except:
        print("Sorry, that wasn't found. Please try again.")
        continue
    if option not in [0,1,2,3]:
        print("Sorry, that wasn't found. Please try again.")
        continue
    elif option == 0:
        checker()
    elif option == 1:
        shuffle()
    elif option == 2:
        print("Here are all syllables:\n",sylList)
    elif option == 3:
        print("Thank you for using this program. It will now terminate.")
        break

                    
file.close()