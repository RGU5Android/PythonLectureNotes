#!/usr/bin/python

def count_word_in_sentence(sentence,word):
    list_sentence = sentence.split(" ")
    count = 0
    for tmp_word in list_sentence:
        if tmp_word.lower().__contains__(word.lower()):
            count += 1
    return count

if __name__=='__main__':
    sentence = raw_input("Enter the sentence: ")
    word = raw_input("Enter the word: ")
    print ("Sentence contains the word : " +str(count_word_in_sentence(sentence, word)) +" times")
