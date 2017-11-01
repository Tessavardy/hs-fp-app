def process_user_query(query_string):
    names = query_string.split()
    list1 = []
    counter = 0
    for word in names:
             if word == 'google':
                 counter += 1
    list1.append(f' You have searched in google {counter} times')
    if counter < 5:
        list1.append(f'Not too shabby')
    else:
        list1.append(f'You need to read more books')
    return(list1)


print(process_user_query("hello google google google "))


# new_list=["Aaberg","Aalst","Aara","Aaren","Aarika","Aaron","Aaronson","Ab","Aba","Abad","Abagael","Abagail","Abana","Abate","Abba","Abbate","Abbe","Abbey","Abbi","Abbie","Abbot","Abbotsen","Abbotson","Abbotsun","Abbott","Abbottson","Abby","Abbye","Abdel","Abdella","Abdu","Abdul","Abdulla","Abe","Abebi","Abel","Abelard","Abell","Abercromby","Abernathy","Abernon","Abert","Abeu","Abey","Abie","Abigael","Abigail","Abigale","Abijah","Abisha","Abisia","Abixah","Abner","Aborn","Abott","Abra","Abraham","Abrahams","Abrahamsen","Abrahan","Abram","Abramo","Abrams","Abramson","Abran","Abroms","Absa","Absalom","Abshier","Acacia","Acalia","Accalia","Ace","Acey","Acherman","Achilles","Achorn","Acie","Acima","Acker","Ackerley","Ackerman","Ackler","Ackley","Acquah","Acus","Ad","Ada","Adabel","Adabelle","Adachi","Adah","Adaha","Adai","Adaiha","Adair","Adal","Adala","Adalai","Adalard","Adalbert","Adalheid","Adali","Adalia","Adaliah","Adalie","Adaline","Adall","Adallard","Adam","Adama","Adamec","Adamek"]
#
# def process_user_query(query_string): ## query_string stores what the user enters on heruku
#     list1 = query_string.split() ##creating it into a list of names
#     names = []
#     for word in set(list1):
#         if word in list1:
#             names.append(f' Hi {word}')
#     return(names)
#
# print(process_user_query("Tessa Waxman"))
