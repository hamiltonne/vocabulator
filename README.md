# vocabulator
A tool for estimating the vocabulary of a given set of texts.

Vocabulator is designed to read in plaintext files encoded in [any format supported by Python](https://docs.python.org/3/library/codecs.html#standard-encodings).

**Usage:**
1. Generate a `dictionary` with `makedict` ([available here](https://github.com/hamiltonne/makedict)).
2. Preapre your text files to be read in. Two requirements:
   - They must be a plaintext file.
   - They must stored in a subdirectory in the program's root
3. Run `py vocabulator.py` with two positional commands: input directory & encoding format (usually either `ascii` or `utf8`)

**Notes:**
The program can take a while depending on the size of the input.
Accuracy is ~90% - it may miss certain conjugated verbs and nouns but in most cases those words will appear in other recognizable tenses.
Considering the accuracy, this tool is best used for comparative analyses rather than estimating the vocabulary demonstrated by a single work or author. 

**To-do:**
1. Allow logging of statistics to file.
2. Improve accuracy.
   - Implement function to check unknown word against common suffixes & plural endings
   - Implement dump function to check rejected strings
3. Implement GUI
4. Merge `makedict` script
