import string

def avg_word_len(text):
    words = text.replace('.', ' ').replace(',', ' ').split()  
    word_lengths = [len(word) for word in words]  
    avg_length = sum(word_lengths) / len(word_lengths) if word_lengths else 0  
    
    return avg_length
    

text = "Hi all, my name is Tom... I am originally from Australia."
print(f"Average word length: {avg_word_len(text):.2f}")  
