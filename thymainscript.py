def medivalify(input_string):
    # Replaces instances of words with archaic ones,
    # for example the word "the" would become "thy"
    medivalifyed_string = input_string.replace("the", "thy").replace("you", "thou").replace("are", "art").replace("your", "thine").replace("have", "hast")
    return medivalifyed_string


print(medivalify(input("Enter a phrase: ")))
