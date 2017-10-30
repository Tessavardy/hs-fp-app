
def process_user_query(query_string): ## query_string stores what the user enters on heruki

    list1 = query_string.split() ##creating it into a list of names
    names = []
for word in list1:
    if word[0].isupper():
        list1.append(word)

print(list1)
