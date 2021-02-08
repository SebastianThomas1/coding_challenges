# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/520b9d2ad5c005041100000f
#
# Simple Pig Latin

def pig_it(text):
    return ' '.join([word[1:] + word[:1] + 'ay' if word.isalpha() else word
                     for word in text.split()])


if __name__ == '__main__':
    print(pig_it('Pig latin is cool'))  # igPay atinlay siay oolcay
    print(pig_it('Hello world !'))  # elloHay orldway !
