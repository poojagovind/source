For a given string, find whether or not a permutation of this string is a palindrome. You should return TRUE if such a permutation is possible and FALSE if it isn’t possible.


def permute_palindrome(st):
    frequencies = {}
    index = 0
    for i in st:
        index += 1
        if i in frequencies:
            frequencies[i] += 1
        else:
            frequencies[i] = 1
    count = 0
    for ch in frequencies.keys():
        if frequencies[ch] % 2:
            count += 1

    if count <= 1:
        return True
    else:
        return False