# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039
#
# Mumbling

def accum(s):
    return '-'.join(char.upper() + char.lower() * idx
                    for idx, char in enumerate(s))


if __name__ == '__main__':
    print(accum('abcd'))  # A-Bb-Ccc-Dddd
    print(accum('RqaEzty'))  # R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy
    print(accum('cwAt'))  # C-Ww-Aaa-Tttt
    print(accum(''))  #
    print(accum('ZpglnRxqenU'))
    # Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn
    # -Uuuuuuuuuuu
    print(accum('NyffsGeyylB'))
    # N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll
    # -Bbbbbbbbbbb
    print(accum('MjtkuBovqrU'))
    # M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr
    # -Uuuuuuuuuuu
    print(accum('EvidjUnokmM'))
    # E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm
    # -Mmmmmmmmmmm
    print(accum('HbideVbxncC'))
    # H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc
    # -Ccccccccccc
