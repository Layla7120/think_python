import string
from random import choice


def process_file(filename):
    w_list = list()
    fp = open(filename, encoding= 'utf-8')
    for line in fp:
        process_line(line, w_list)
    return w_list


def process_line(line,w_list):
    line = line.replace('-',' ')
    for word in line.split():
        word = word.strip('[,],(,), ')
        word = word.lower()
        w_list.append(word) 


def markov(w_list, length):
    w_markov = {}

    for n in range(length - 1, len(w_list) - length):
        key_w = ' '.join(w_list[n - length:n])
        value_w = w_list[n]
        if key_w in w_markov:
            if value_w != w_markov[key_w]:
                w_markov[key_w] +=':' + value_w
        else:
            w_markov[key_w] = value_w
    
    return w_markov

count = 0
ran_w = []

def make_random_words(w_markov, count, key_index):
    # print(count)
    if count == 0:
        key_index = choice(list(w_markov.keys()))
        options = w_markov[key_index].split(':')
        # print(options)
        next_word = choice(options)
        ran_w.append(next_word)
        count += 1
        key_index = (key_index.split())[1] + " " + next_word
        # print(key_index)
        make_random_words(w_markov, count, key_index)

    elif key_index in w_markov and count < 30:
        options = w_markov[key_index].split(':')
        # print(options, "in")
        next_word = choice(options)
        ran_w.append(next_word)
        key_index = (key_index.split())[1] + " " + next_word
        count += 1
        make_random_words(w_markov, count, key_index)
    


def main():
    novel = process_file('emma.txt')
    markov_list = markov(novel, 2)
    make_random_words(markov_list, 0, '')
    print(' '.join(ran_w))


if __name__ == "__main__":
    main()