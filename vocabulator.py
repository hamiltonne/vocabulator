import os
import re
import codecs

text = []
inputs = []
total = []
exception = []
counter = 0

print("Encoding:")
encoding = input()

for file in os.listdir("input"):
    try:
        text.append(open("input/" + file, encoding=encoding))
        inputs.append(file)
    except IOError:
        print(file, "is unreadable.")

print("Program may appear frozen while processing.")

for c in text:
    words = []
    unique = []
    for word in c.read().split():
        temp = word.lower()
        temp = re.sub('[?:,!.;\'_()‘’]', '', temp)
        position = temp.find("-")
        if position == -1:
            position = temp.find("—")
        if position > 1:
            temporary = temp[position+1:]
            temporary = re.sub('[-]', '', temporary)
            if temporary not in unique:
                unique.append(temporary)
            if temporary not in total:
                total.append(temporary)
            words.append(temporary)
            temp = temp[:position]
        temp = re.sub('[-]', '', temp)
        if temp not in unique:
            unique.append(temp)
        if temp not in total:
            total.append(temp)
        words.append(temp)
    print("Statistics for", inputs[counter])
    print("\tTotal words used: ", len(words))
    print("\tVocabulary: ", len(unique))
    print("\tPercentage of unique words in text:", round((len(unique) / len(words)) * 100), "%")
    counter = counter+1

total.sort()
btotal = []

dictionary = open("dictionary.txt").read().split("\n")
for word in total:
    if word in dictionary:
        btotal.append(word)

print("Total vocabulary:", len(btotal))
print("Export vocabulary to file? Y/N")

if input() == "Y":
    out = open("vocabulary.txt", "w", encoding=encoding)
    for word in btotal:
        out.write(word)
        out.write("\n")
    out.close()
    print("Exported to vocabulary.txt")
    quit()
else:
    quit()
