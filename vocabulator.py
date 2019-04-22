import string
import os

text = []
inputs = []
total = []
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
        temp.translate(str.maketrans("", "", string.whitespace + "!.,'"))
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
    out = open("vocabulary.txt", "w")
    for word in btotal:
        out.write(word)
        out.write("\n")
    out.close()
    print("Exported to vocabulary.txt")
    quit()
else:
    quit()
