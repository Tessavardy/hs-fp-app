def process_user_query(query_string): ## query_string stores what the user enters on heruki

    list1 = query_string.split()

    for n in list1:
        result = f'Hi {query_string}'

    return result ## return should always be something like this


print(process_user_query('Tessa Alex'))
