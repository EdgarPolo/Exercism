def is_isogram(string):    

    string = string.lower()
    for x in range(len(string)):
        for i in range(len(string)):
            if x != i and string[x] == string[i] and string[x].isalpha():
                return False

    return True
