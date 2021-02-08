# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/554e4a2f232cdd87d9000038
#
# Complementary DNA

def dna_strand(dna):
    return dna.translate({ord('A'): 'T', ord('T'): 'A', ord('C'): 'G',
                          ord('G'): 'C'})


if __name__ == '__main__':
    print(dna_strand('AAAA'))  # TTTT
    print(dna_strand('ATTGC'))  # TAACG
    print(dna_strand('GTAT'))  # CATA
