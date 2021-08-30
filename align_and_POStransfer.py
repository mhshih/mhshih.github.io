from nltk.metrics.distance import edit_distance
from nltk.metrics.distance import edit_distance_align

def check_POS(j, tagged_words):
    i = 0
    for word, tag in tagged_words:
        i += len(word)
        if i == j:
            return tag

def align_and_tag(min, tagged_words, substitution_cost):
    s1 = min
    words = [word for word, tag in tagged_words]
    s2 = "".join(words)

    X = ['#']
    Y = ['#']

    alignment = edit_distance_align(s1=s1, s2=s2, substitution_cost=substitution_cost)
    i_1, j_1 = alignment[0]
    X[i_1] = '#'
    Y[j_1] = '#'

    for i,j in alignment[1:]: 
        if i == i_1 + 1 and j == j_1:   # delete operation
            tag = check_POS(j, tagged_words)
            if tag:
                X.append(s1[i-1]+"("+tag)
            else:
                X.append(s1[i-1])
            Y.append('＊')#*')
        elif i == i_1 and j == j_1 + 1: # insert operation
            tag = check_POS(j, tagged_words)
            if tag:
                X.append('＊' + "(" + tag)
            else:
                X.append('＊')
            Y.append(s2[j-1])
        elif i == i_1 + 1 and j == j_1 + 1:
            tag = check_POS(j, tagged_words)
            if tag:
                X.append(s1[i-1]+"("+tag)
            else:
                X.append(s1[i-1])
            Y.append(s2[j-1])
        i_1 = i
        j_1 = j
    return X, Y

from sys import argv
if __name__ == '__main__':
    min = argv[1]
    tagged_words = argv[2].split("　")
    print(tagged_words)
    tagged_words = [(tagged_word.split("(")[0], tagged_word.split("(")[1]) for tagged_word in tagged_words]
    substitution_cost = int(argv[3])

    print(check_POS(2, tagged_words))

    X, Y = align_and_tag(min=min, tagged_words=tagged_words, substitution_cost=substitution_cost)
    print(X)
    print(Y)
