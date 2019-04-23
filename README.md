# vocabulator
A tool for estimating the vocabulary of a given set of texts via dictionary analysis.

**Usage:**
1. Generate `dictionary.txt` with makedict and place it in the root folder.
2. Create `/input` and place texts to be analysed within.
3. Run `py vocabulator.py`
4. When prompted, input the single encoding format all of your input files are in.
5. Results will be found in `vocabulary.txt`

**Notes:**

Make a coffee while you wait! The program can take a while depending on the size of the input.

For example: calculating Dicken's vocabulary via his extant corpus takes upwards of fifteen minutes to compute on a reasonably fast computer (the result? ~20,100 words).

Accuracy is >=90% - it may miss certain conjugated verbs and nouns but in most cases those words will appear in other recognizable forms.

Considering the accuracy, this tool is best used for comparative analyses rather than estimating the vocabulary demonstrated of a single work or author. 

**To-do:**
1. Allow logging of statistics to file.
2. Improve accuracy.
3. Implement internal UTF-8 conversion for mitigating encoding errors.