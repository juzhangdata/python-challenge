#import dependencies:
import os
import csv
import re

#join path
path1 = os.path.join('.', 'raw_data', 'paragraph_1.txt')
path2 = os.path.join('.', 'raw_data', 'paragraph_2.txt')

#open file and get info
with open(path1, 'r') as myfile:
    paragraph = myfile.read().replace('\n', '')

    #count words
    words = paragraph.split(" ")
    word_count = len(words)

    #count sentences
    sentences = re.split(r"\(?&lt;=\[.!?\]\)+", paragraph)
    sentence_count = 0
    for i in sentences:
        sentence_count += 1

    #count letters
    letters = 0
    for word in words:
        letters += len(word)
    
    #count average letter in each word
    average_letter_count = letters / word_count

    #count average sentences length
    average_sentence_length = letters/ sentence_count

#print out results
print(
f"""```
Paragraph Analysis
-----------------
Approximate Word Count: {word_count}
Approximate Sentence Count: {sentence_count}
Average Letter Count: {average_letter_count}
Average Sentence Length: {average_sentence_length}
```
""")