# Your code here

def histo():
    dict = {}
    remove_characters = ["\"", ":", ";", ",", ".", "-", "+", "=", "/", "\\",
                         "|", "[", "]", "{", "}", "(", ")", "*", "^", "&", '', "!", "?"]
    with open("robin.txt") as f:
        words = f.read()
    for word in words.split():
        if word in remove_characters:
            continue

        if word not in dict:
            dict[word] = "#"
        else:
            dict[word] += "#"
    alphabetized_word_tally = sorted(
        dict.items(), reverse=True, key=lambda item: item[0])
    sorted_word_tally = sorted(
        alphabetized_word_tally, key=lambda item: item[1])
    sorted_word_tally = sorted_word_tally[::-1]

    print(sorted_word_tally)


histo()
