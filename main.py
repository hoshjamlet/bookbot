def main():
    path = 'books/frankenstein.txt'
    text=book_text(path)
    print(f'Beginning report of {path}')
    print(f'{len(words(text))} words found in the document')
    for item in dict_to_list(letter_count(text)):
        if not item["char"].isalpha():
            continue
        print(f'The {item["char"]} character was found {item["num"]} times')
    
    
    
              
def book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def words(text):
    words = text.split()
    return words

def letter_count(word_list):
    word_dict={}
    for word in word_list:
        l_word=word.lower()
        for letter in l_word:
            if letter in word_dict:
                word_dict[letter]+=1
            else: 
                word_dict[letter]=1
    return word_dict

def sort_on(dict):
    return dict["num"]

def dict_to_list(word_dict):
    sorted_list=[]
    for k,v in word_dict.items():
        sorted_list.append({"char":k,"num":v})
    sorted_list.sort(reverse=True,key=sort_on)
    return(sorted_list)
        


    
main()

