#!/usr/bin/env python3

################################################################
#
#   Program to write in H4CK3R C0D3 for your personnal messages
#
#   Author : oliBeau
#   Github : @OliBeaulieu
#
################################################################
#   *Aditionnal notes on the program : only fully translate text 
#       text without accents 
#   *   Take the first argument of argv as the text to translate
################################################################

## Variables

textToTranslate = ""    # string
translatedText = []     # list
finalMessage = ""       # string

# Dictionnary of translations
translationDict = { "a" : "4", "e" : "3", "i" : "1", "o" : "0" }


## Prompt the user for the text to translate in H4CK3R C0D3
# textToTranslate = sys.argv[0]

textToTranslate = input("Please enter the text to translate in H4CK3R C0D3 :")

for letter in textToTranslate:
    if (letter in translationDict) or (letter.lower() in translationDict):
        translatedText.append(translationDict[letter.lower()])
    else:
        translatedText.append(letter)

finalMessage = "".join(translatedText)

print(finalMessage)



