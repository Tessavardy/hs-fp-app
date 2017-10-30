# def process_user_query(query_string): ## query_string stores what the user enters on heruki
#
#     list1 = query_string.split() ##creating it into a list of names
#     names = []
#     for name in list1:
#         names.append(f'Hi {name}!')
#     return names ## return should always be something like this
#
#
# print(process_user_query('Tessa Alex'))

def process_user_query(query_string): ## query_string stores what the user enters on heruki

list = ['Hi alex how are you']
for word in list:
    if word[0].isupper():
        list.appned(word)
