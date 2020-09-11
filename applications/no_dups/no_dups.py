def no_dups(s):
    dict = {}
    # Your code here
    # split string by spaces
    if len(s) <= 0:
        return ""
    split = s.split()
    # loop through string
    for word in split:
     # add string to dict if its not there
        if word not in dict:
            dict[word] = 1
    # if word is in the string, remove it from the string
    output_string = ""
    for word in dict.keys():
        output_string += " " + word
    output_string = output_string.replace(" ", "", 1)
    return output_string


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
