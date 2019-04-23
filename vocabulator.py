import os
import re


def process(add):
    if add not in unique:
        unique.append(add)
    if add not in total:
        total.append(add)
    words.append(add)


# variables
text = []
inputs = []
total = []
hyphen = []
exception = []
counter = 0

# pre-processing
print("Encoding:")
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

# parsing
print("Program may appear frozen while processing.")

for file in text:
    words = []
    unique = []

    for word in file.read().split():
        process(word)
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

    print("Statistics for", inputs[counter])
    print("\tTotal words used: ", len(words))
    print("\tUnique words: ", len(unique))
    print("\tPercentage of unique words in text:", round((len(unique) / len(words)) * 100), "%")
    counter = counter+1

total.sort()
vocabulary = []

# dictionary analysis
dictionary = open("dictionary.txt").read().split("\n")
for word in total:
    if word in dictionary:
        vocabulary.append(word)

# export
print("Total vocabulary:", len(vocabulary))
print("Export vocabulary to file? Y/N")

if input() == "Y":
    out = open("vocabulary.txt", "w", encoding=encoding)
    for word in vocabulary:
        out.write(word)
        out.write("\n")
    out.close()
    print("Exported to vocabulary.txt")
    quit()
else:
    quit()
