import re

def count_words(file):
    with open(f"../files/{file}", "r") as input_file:
        text = input_file.read() # converts to one long string
        text_lst = re.findall(r"[\w]+", text) #matches on word chars
        
        # needs unique words not just total
        text_set = set()

        for word in text_lst:
            text_set.add(word)
        
        large_words = []
        small_words = []

        for word in text_set:
            if len(word) < 3:
                small_words.append(word)
            else:
                large_words.append(word)


    with open("large-words.txt", "w") as large_file:
        #write some text
        for word in large_words:
            large_file.write(f"{word}\n")
    
    
    with open("small-words.txt", "w") as small_file:
        #write something
        for word in small_words:
            small_file.write(f"{word}\n")
     
        
        
    return len(text_set)





def ex3():
    total_words = count_words("words.txt")
    print(f"Total words: {total_words}.")

ex3()