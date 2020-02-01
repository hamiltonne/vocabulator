import os
import re
import argparse

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

# Argument parsing
parser = argparse.ArgumentParser(prog='vocabulator',
                                 description='Estimate the vocabularly of a given set of texts',
                                 epilog='Note: vocabulator requires a dictionary.txt')
parser.add_argument("directory",
                    help='specifies a directory to read texts from, required option')
parser.add_argument("encoding",
                    help='specifies an encoding format to read and save with')
parser.add_argument('-v', '--verbose',
                    help='enables verbose output',
                    dest='verbose',
                    action='store_true')
parser.add_argument('-o', '--output',
                    help='specifices a file to export the vocabulary list to',
                    dest='output')
args = parser.parse_args()

# Pre-processing
for file in os.listdir(args.directory):
    try:
        text.append(open(args.directory + '/' + file, encoding=args.encoding))
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
    if args.verbose is True:
        print("Total number of words in ", inputs[counter], ":", len(unique))
    counter = counter+1
total.sort()

# Dictionary Analysis
for word in total:
    if word in dictionary:
        vocabulary.append(word)
print("Total vocabulary:", len(vocabulary))

# Export
if args.output is not None:
    out = open(args.output, "w", encoding=args.encoding)
    for word in vocabulary:
      out.write(word+"\n")
    out.close()
    print("Exported to", args.output)
    quit()  
else:
    quit() 
