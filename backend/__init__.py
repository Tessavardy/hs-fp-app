
def process_user_query(query_string): ## query_string stores what the user enters on heruku
    list1 = query_string.split() ##creating it into a list of names
    names = []
    for word in set(list1):
        if word[0].isupper():
            names.append(f' Hi {word}')
    return(names)
 
