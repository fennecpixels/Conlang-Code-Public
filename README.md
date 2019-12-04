# Conlang Code Public
 
## What is this?

This is a collection of the programs I made for conlanging. 

### Why Conlang Code **Public**?

I chose this because I already have a GitHub repo in the works for this project, but it has information not needed here. Instead of publishing that, I chose this.

## Contents

### `SyllableFunctions.py`

This program is able to randomise a list of syllables (see allPossibleSyllables.txt); check that a word works within the syllable structure of a conlang; and also show the full syllable list. I had some issues with encoding, so it does delete the first line. To fix this, you may need an empty line as the first. The program splits the syllables at new lines:
```python
file = open("allPossibleSymbols.txt","r") #Opens file
sylList = file.read().split("\n")
sylList.pop(0) #Encoding error right now
print("Syllables loaded!",sylList)
```

### allPossibleSymbols.txt

This text file has all the syllables within the conlang. If you download this, feel free to change them to suit your needs. As I mentioned previously: 

> I had some issues with encoding, so it does delete the first line. To fix this, you may need an empty line as the first.

When changing it, make sure you:

* Keep the first line blank (for encoding issues)
* Separate each syllable by a line break
    
    Note: this doesn't mean
    ```
    a
    [line break]
    b
    [line break]
    c
    ```
    It means
    ```
    a
    b
    c
    ```
* Use **ASCII / UTF-8 only** characters.
