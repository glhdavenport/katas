


def get_sentence_score(sentence):
    print("Given sentence:", sentence)
    return sum([get_score(letter) for word in sentence.split() for letter in word])

    # https://www.python.org/dev/peps/pep-0289/
    
def get_score(letter):
    values = {
        "A": 1481,
        "a": 1481,
        "B": 271,
        "b": 271,
        "C": 494,
        "c": 494,
        "D": 787,
        "d": 787,
        "E": 2191,
        "e": 2191,
        "F": 420,
        "f": 420,
        "G": 369,
        "g": 369,
        "H": 1079,
        "h": 1079,
        "I": 1331,
        "i": 1331,
        "J": 18,
        "j": 18,
        "K": 125,
        "k": 125,
        "L": 725,
        "l": 725,
        "M": 476,
        "m": 476,
        "N": 1266,
        "n": 1266,
        "O": 1400,
        "o": 1400,
        "P": 331,
        "p": 331,
        "Q": 20,
        "q": 20,
        "R": 1097,
        "r": 1097,
        "S": 1145,
        "s": 1145,
        "T": 1658,
        "t": 1658,
        "U": 524,
        "u": 524,
        "V": 201,
        "v": 201,
        "W": 381,
        "w": 381,
        "X": 31,
        "x": 31,
        "Y": 385,
        "y": 385,
        "Z": 12,
        "z": 12
    }  
    # The quick brown fox jumps over the lazy dog.
    # 4928+2494+4415+1851+2494+4889+4928+2603+2556 = 31158
    # Uif rvjdl cspxo gpy kvnqt pwfs uif mbaz eph.
    # 2275+2828+3401+1085+3270+2277+1275+2240+3601 = 22252


    # letter = letter.upper()
    return values[chr(letter)] if chr(letter) in values else 0
