# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.hackerrank.com/challenges/designer-pdf-viewer
#
# Designer PDF Viewer

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
IDX_OF_CHAR = {char: idx for idx, char in enumerate(ALPHABET)}


def designer_pdf_viewer(h, word):
    return max(h[IDX_OF_CHAR[char]] for char in word) * len(word)


if __name__ == '__main__':
    print(designer_pdf_viewer(
        [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 5], 'abc'))  # 9
    print(designer_pdf_viewer(
        [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
         5, 5, 7], 'zaba'))  # 28
