import sys
import random

filler = map(lambda x: x.strip(), open('filler.txt').readlines())
censorship = map(lambda x: x.strip(), open('censorship.txt').readlines())

def make_sentence():
    sentence = random.choice(filler + censorship).capitalize()
    length = random.randint(4, 15)
    for i in range(length):
        if random.random() > 0.8:
            sentence += ', '
        else:
            sentence += ' '
        if random.random() > 0.5:
            sentence += random.choice(filler)
        else:
            sentence += random.choice(censorship)

    sentence += '. '
    return sentence

def main(argv):
    sentence_count = 5
    if len(sys.argv) > 1:
        sentence_count = int(sys.argv[1])

    ipsum = ''
    for i in range(sentence_count):
        ipsum += make_sentence()
    print(ipsum)

if __name__ == '__main__':
    main(sys.argv)
