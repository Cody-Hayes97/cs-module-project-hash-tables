# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.
alphabet = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L', 'W', 'U',
            'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']
# Your code here


def decrypt():
    dict = {}
    cipher_dict = {}
    result = ""
    with open("ciphertext.txt") as f:
        words = f.read()
    for letter in words:
        if letter not in dict:
            dict[letter] = 1
        else:
            dict[letter] += 1

    sorted_letters = list(dict.items())
    sorted_letters.sort(reverse=True, key=lambda item: item[1])

    for idx, letter in enumerate(alphabet):
        cipher_dict[sorted_letters[idx][0]] = alphabet[idx]
    for letter in words:
        if letter.isalpha():
            print(cipher_dict[letter])
            result += cipher_dict[letter]
        else:
            result += letter
    print(result)


decrypt()
