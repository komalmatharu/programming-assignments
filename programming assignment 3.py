def gibberish():
    result = ""
    #defining uppercase and lowercase vowels
    v_lower = "aeiou"
    v_upper = "AEIOU"
    #opening and reading the txt file
    file=open("english_text.txt", "r")
    text=file.read()
    #for loop to change vowels from the txt file
    for i in text:
        #first rule adds "egg" to the beginning of each lowercase vowel
        if i in v_lower:
            result = result + "egg" + i
        #second rule adds "ldig" before uppercase vowels and lowercases them
        elif i in v_upper:
            result = result + "ldig" + i.lower()
        #third rule does not make any changes if the character is not a vowel
        else:
            result = result + i
    print(result)
gibberish()
