import os
import re

# Functions
def process(add):
    if add not in unique:
        unique.append(add)
    if add not in total:
        total.append(add)
    words.append(add)

# Variables
text = []
inputs = []
total = []
hyphen = []
vocabulary = []
counter = 0

# Pre-processing
print("Encoding:", end = " ")
encoding = input()
for file in os.listdir("input"):
    try:
        text.append(open("input/" + file, encoding=encoding))
        inputs.append(file)
    except IOError:
        print(file, "is unreadable.")
dictionary = open("dictionary.txt").read().split("\n")
for word in dictionary:
    if "-" in word:
        hyphen.append(word)

# Parsing
print("Program may appear frozen while processing!")
for file in text:
    words = []
    unique = []
    for word in file.read().split():
        temp = word.lower()
        temp = re.sub('[?:,!.;\'_()‘’]', '', temp)
        position = temp.find("-")
        if position == -1:
            position = temp.find("—")
        if position > 1:
            if temp not in hyphen:
                temporary = temp[position + 1:]
                temporary = re.sub('[-]', '', temporary)
                process(temporary)
                temp = temp[:position]
                temp = re.sub('[-—]', '', temp)
        process(temp)
    print("Total number of words used for", inputs[counter], ":", len(unique))
    counter = counter+1
total.sort()

# Dictionary Analysis
for word in total:
    if word in dictionary:
        vocabulary.append(word)

# export
print("Total vocabulary:", len(vocabulary))
print("Export? [y/n]:", end = " ")
if input() == "Y" or "y" or "yes" or "Yes":
    out = open("vocabulary.txt", "w", encoding=encoding)
    for word in vocabulary:
        out.write(word+"\n")
    out.close()
    print("Exported to vocabulary.txt", end = " ")
    quit()
else:
    quit()
