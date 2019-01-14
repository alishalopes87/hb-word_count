# put your code here.
def  count_words(file_name):

    test_file = open(file_name)
    
    word_count = {}

    for line in test_file:
        line = line.rstrip()
        words_in_lst = line.split(" ")

        for word in words_in_lst:
            word_count[word] = word_count.get(word, 0) + 1
            for word, cnt in word_count.items():
                print(word, cnt)

    

