#  -- coding: utf-8 --
def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
#试着执行 help(ex25) 和 help(ex25.break_words) 。这是你得到模组帮助文档的方式。 所谓帮助文档就是你定义函数时放在 """ 之间的东西，它们也被称作 documentation comments （文档注解），后面你还会看到更多类似的东西。 
def sort_words(words):
    """Sorts the words."""
    return sorted(words)
    
def print_first_word(words):
    """Prints the first word after poping it off."""
    word = words.pop(0)        
    print word
    
def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
    
def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
     
def print_first_and_last(sentence):
    """Prints the firs and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)
    
def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one ."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)    
         
    
            
