import os

# Module for reading CSV files
import csv
csvpath = os.path.join(os.path.dirname(__file__),'raw_data', 'paragraph_1.txt')
csvpath1 = os.path.join(os.path.dirname(__file__),'raw_data', 'paragraph_2.txt')

#read txt file
with open(csvpath, 'r') as f:
    data  = f.read()
    p1word = data.split()
    p1word_count = len(data.split())
    p1sentence_count = data.count(".")
    print("sentences in Paragraph1: "+ str(p1sentence_count))
    print(f"words in Paragraph1: {p1word_count}")
    c = {}
    for word in p1word:
        c.update({word: len(word)})
    totalletter= sum(c.values())
    print(c.items())

with open(csvpath1, 'r') as f:
    # CSV reader specifies delimiter and variable that holds contents
    data1  = f.read()
    p2word = data1.split()
    p2sentence_count = data1.count(".")
    print("sentences in Paragraph2: " + str(p2sentence_count-1))
    p2word_count = len(data1.split())
    print(f"words in Paragraph2: {p2word_count}")
    d={word:len(word) for word in p2word}
    print(d.items())
    totalletter1=sum(d.values())
    print("\n")


total_word_count=p1word_count+p2word_count
total_sentence = p2sentence_count+p1sentence_count
totallettercount=totalletter+totalletter1

print("Paragraph Analysis\n---------------------------")
print(f"Approximate Word Count: {total_word_count}")
print(f"Approximate Sentence Count: {total_sentence}")
print(f"Average Letter Count: {round(totallettercount/total_word_count,1)}")
print(f"Average Sentence Length: {round(total_word_count/total_sentence,1)}")

output_file = os.path.join(os.path.dirname(__file__), "final_output_pyparagraph.txt")

with open(output_file, 'w') as the_file:
    the_file.write(f"Paragraph Analysis\n---------------------------\nApproximate Word Count: {total_word_count}\nApproximate Sentence Count: {total_sentence}")
    the_file.write(f"\nAverage Letter Count: {round(totallettercount/total_word_count,1)}")
    the_file.write(f"\nAverage Sentence Length: {round(total_word_count/total_sentence,1)}")