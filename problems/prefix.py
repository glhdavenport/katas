from typing import List
# JAVA types :: Type variableName
# Python types :: variable_name: Type

def words(sentence: str) -> List[str]:
    return sentence.split()

def is_prefix(word: str, prefix: str) -> bool:
    return word.startswith(prefix)

def is_prefix_of_word(sentence: str, prefix: str) -> int:
    word_list = words(sentence)

    # numbers = [1, 2, 3, 4, 5, 600, 3, 2, 42]
    # even_nums = []
    # for n in numbers:
    #     if n % 2 == 0:
    #         even_nums.append(n)
    
    # even_nums = [n for n in numbers if n % 2 == 0]
    # square_of_evens = [n ** 2 for n in numbers if n % 2 == 0]
    # index_of_evens = [i for i, n in enumerate(numbers) if n % 2 == 0]

    index_of_match: List[int] = [i+1 for i, word in enumerate(word_list) if is_prefix(word, prefix) == True]
    return index_of_match[0] if index_of_match else -1
    # for i, word in enumerate(word_list):
    #     if is_prefix(word, prefix) == True:
    #         return i + 1    
    # return -1
        
