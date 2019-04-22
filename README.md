# vocabulator
A tool for estimating the vocabulary of a given set of texts via dictionary analysis.

**Usage:**
1. Generate a `dictionary.txt` with makedict and place it in the root folder.
2. Create `/input` and place texts to be analysed within.
3. Run `py vocabulator.py`
4. Results will be found in `vocabulary.txt`

**Notes:**

Make a coffee while you wait! The program can take quite a while depending on the number of input files. 

For example: calculating Dicken's vocabulary via his extant corpus takes upwards of fifteen minutes on a reasonably decent computer (the result? ~19,000 words).

Accuracy is around ~90%.

**To-do:**
1. Allow logging of statistics to file.
2. Improve accuracy.