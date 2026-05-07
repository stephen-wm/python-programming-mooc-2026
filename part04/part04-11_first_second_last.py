def first_word(sentence):
    return sentence.split(" ")[0]
 
def second_word(sentence):
    return sentence.split(" ")[1]
 
def last_word(sentence):
    return sentence.split(" ")[-1]
 
# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "once upon a time there was a programmer"
    print(first_word(sentence)) # once
    print(second_word(sentence)) # upon
    print(last_word(sentence)) # programmer