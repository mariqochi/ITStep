#დავალება 14

#1. დაწერე კოდი რომელიც article.txt _დოკუმენტში იპოვის რიგით მეორე ყველაზე ხშირად განმეორებად სიტყვას.




def remove_specific_punctuation(text):
    for char in ['.', ',', '"', '(', ')']:
        text = text.replace(char, ' ')
    return text

def count_words(filename):
    word_count  = {}

    with open(filename, 'r') as file:
        text = file.read().lower()
        text = remove_specific_punctuation(text)
        words = text.split()

        unique_words = set(words)

        for word in unique_words:
            word_count[word] = words.count(word)

    return word_count


filename = 'article.txt'
word_count = count_words(filename)

print(f"Word count: {word_count}")
most_common_word = max(word_count, key=word_count.get)
print(f"The most common word is: '{most_common_word}'") 




#2. names.csv ფაილში არსებული ინფორმაცია გადმოაკოპირე names.txt ფაილში.

import csv

with open("names.csv", "r") as file:
    csv_reader = csv.reader(file, delimiter=",")
    with open("names.txt", "w", newline="") as new_file:
        txt_writer = csv.writer(new_file)  
        for line in csv_reader:
            txt_writer.writerow(line)