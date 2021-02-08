# Sebastian Thomas (coding at sebastianthomas dot de)

# https://www.codewars.com/kata/540d0fdd3b6532e5c3000b5b
#
# Binomial Expansion

def binom(n, k):
    res = 1
    for i in range(1, k + 1):
        res *= n - i + 1
        res //= i

    return res


def binomial_parameters(expr):
    # determine indeterminate and index of indeterminate
    indeterminate = None
    indeterminate_idx = -1
    for idx, char in enumerate(expr):
        if char.isalpha():
            indeterminate = char
            indeterminate_idx = idx
            break

    # determine index of carrot
    carrot_idx = -1
    for idx, char in enumerate(expr[indeterminate_idx + 1:],
                               start=indeterminate_idx + 1):
        if char == '^':
            carrot_idx = idx
            break

    coef1_rep = expr[1:indeterminate_idx]
    if coef1_rep == '':
        coef1 = 1
    elif coef1_rep == '-':
        coef1 = -1
    else:
        coef1 = int(coef1_rep)

    coef0_rep = expr[indeterminate_idx + 1:carrot_idx - 1]
    coef0 = int(coef0_rep)

    power_rep = expr[carrot_idx + 1:]
    power = int(power_rep)

    return coef0, coef1, indeterminate, power


def coef_rep(coef):
    if coef == 1:
        return ''
    elif coef == -1:
        return '-'
    else:
        return str(coef)


def expand(expr):
    coef0, coef1, indeterminate, power = binomial_parameters(expr)

    coefs = [int(binom(power, k)) * (coef0**(power - k)) * (coef1 ** k)
             for k in range(power + 1)]

    term_reps = [str(coefs[0])]
    if power > 0:
        if coefs[0] > 0:
            term_reps[0] = '+' + term_reps[0]
        elif coefs[0] == 0:
            term_reps[0] = ''
        term_reps.append(coef_rep(coefs[1]) + indeterminate)
    if power > 1:
        term_reps += [coef_rep(coefs[k]) + indeterminate + '^' + str(k)
                      for k in range(2, power + 1)]
        for k in range(1, power):
            if coefs[k] > 0:
                term_reps[k] = '+' + term_reps[k]
            elif coefs[k] == 0:
                term_reps[k] = ''

    return ''.join(term_reps[::-1])


if __name__ == '__main__':
    print(expand('(x+1)^2'))  # x^2+2x+1
    print(expand('(p-1)^3'))  # p^3-3p^2+3p-1
    print(expand('(2f+4)^6'))
    # 64f^6+768f^5+3840f^4+10240f^3+15360f^2+12288f+4096
    print(expand('(-2a-4)^0'))  # 1
    print(expand('(-12t+43)^2'))  # 144t^2-1032t+1849
    print(expand('(r+0)^203'))  # r^203
    print(expand('(-x-1)^2'))  # x^2+2x+1
