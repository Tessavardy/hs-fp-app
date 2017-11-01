
def isearched(input1):
    names = input1.split()
    list1 = []
    counter = 0
    for word in names:
             if word == 'bob':
                 counter += 1
    list1.append(f' You have searched {word} {counter} times')
    if counter < 5:
        print('Not too shabby')
    else:
        print('You need to read more books')


    return(list1)


print(isearched('bob bob cat john bob bob bob'))


# new_list=["Aaberg","Aalst","Aara","Aaren","Aarika","Aaron","Aaronson","Ab","Aba","Abad","Abagael","Abagail","Abana","Abate","Abba","Abbate","Abbe","Abbey","Abbi","Abbie","Abbot","Abbotsen","Abbotson","Abbotsun","Abbott","Abbottson","Abby","Abbye","Abdel","Abdella","Abdu","Abdul","Abdulla","Abe","Abebi","Abel","Abelard","Abell","Abercromby","Abernathy","Abernon","Abert","Abeu","Abey","Abie","Abigael","Abigail","Abigale","Abijah","Abisha","Abisia","Abixah","Abner","Aborn","Abott","Abra","Abraham","Abrahams","Abrahamsen","Abrahan","Abram","Abramo","Abrams","Abramson","Abran","Abroms","Absa","Absalom","Abshier","Acacia","Acalia","Accalia","Ace","Acey","Acherman","Achilles","Achorn","Acie","Acima","Acker","Ackerley","Ackerman","Ackler","Ackley","Acquah","Acus","Ad","Ada","Adabel","Adabelle","Adachi","Adah","Adaha","Adai","Adaiha","Adair","Adal","Adala","Adalai","Adalard","Adalbert","Adalheid","Adali","Adalia","Adaliah","Adalie","Adaline","Adall","Adallard","Adam","Adama","Adamec","Adamek","Adamik","Adamina","Adaminah","Adamis","Adamo","Adamok","Adams","Adamsen","Adamski","Adamson","Adamsun","Adan","Adao","Adar","Adara","Adaurd","Aday","Adda","Addam","Addi","Addia","Addie","Addiego","Addiel","Addis","Addison","Addy","Ade","Adebayo","Adel","Adela","Adelaida","Adelaide","Adelaja","Adelbert","Adele","Adelheid","Adelia","Adelice","Adelina","Adelind","Adeline","Adella","Adelle","Adelpho","Adelric","Adena","Ader","Adest","Adey","Adham","Adhamh","Adhern","Adi","Adiana","Adiel","Adiell","Adigun","Adila","Adim","Adin","Adina","Adine","Adis","Adkins","Adlai","Adlar","Adlare","Adlay","Adlee","Adlei","Adler","Adley","Adna","Adnah","Adne","Adnopoz","Ado","Adolf","Adolfo","Adolph","Adolphe","Adolpho","Adolphus","Adon","Adonis","Adora","Adore","Adoree","Adorl","Adorne","Adrea","Adrell","Adria","Adriaens","Adrial","Adrian","Adriana","Adriane","Adrianna","Adrianne","Adriano","Adriel","Adriell","Adrien","Adriena","Adriene","Adrienne","Adur","Aekerly","Aelber","Aenea","Aeneas","Aeneus","Aeniah","Aenneea","Aeriel","Aeriela","Aeriell","Affer","Affra","Affrica","Afra","Africa","Africah","Afrika","Afrikah","Afton","Ag","Agace","Agamemnon","Agan","Agata","Agate","Agatha","Agathe","Agathy","Agbogla","Agee","Aggappe","Aggappera","Aggappora","Aggarwal","Aggi","Aggie","Aggri","Aggy","Agle","Agler","Agna","Agnella","Agnes","Agnese","Agnesse","Agneta","Agnew","Agnola","Agostino","Agosto","Agretha","Agripina","Agrippina","Aguayo","Agueda","Aguie","Aguste","Agustin","Ahab","Aharon","Ahasuerus","Ahders","Ahearn","Ahern","Ahl","Ahlgren","Ahmad","Ahmar","Ahmed","Ahola","Aholah","Aholla","Ahoufe","Ahouh","Ahrendt","Ahrens","Ahron","Aia","Aida","Aidan","Aiden","Aiello","Aigneis","Aiken","Aila","Ailbert","Aile","Ailee","Aileen","Ailene","Ailey","Aili","Ailin","Ailina","Ailis","Ailsa","Ailssa","Ailsun","Ailyn","Aime","Aimee","Aimil","Aimo","Aindrea","Ainslee","Ainsley","Ainslie","Ainsworth","Airel","Aires","Airla","Airlee","Airlia","Airliah","Airlie","Aisha","Ajani","Ajax","Ajay","Ajit","Akanke","Akel","Akela","Aker","Akerboom","Akerley","Akers","Akeyla","Akeylah","Akili","Akim","Akin","Akins","Akira","Aklog","Aksel","Aksoyn","Al","Alabaster","Alage","Alain","Alaine","Alair","Alake","Alameda","Alan","Alana","Alanah","Aland","Alane","Alanna","Alano","Alansen","Alanson","Alard","Alaric","Alarice","Alarick","Alarise","Alasdair","Alastair","Alasteir","Alaster","Alatea","Alathia","Alayne","Alba","Alban","Albarran","Albemarle","Alben","Alber","Alberic","Alberik","Albers","Albert","Alberta","Albertina","Albertine","Alberto","Albertson","Albie","Albin","Albina","Albion","Alboran","Albrecht","Albric","Albright","Albur","Alburg","Alburga","Alby","Alcina","Alcine","Alcinia","Alcock","Alcot","Alcott","Alcus","Alda","Aldarcie","Aldarcy","Aldas","Alded","Alden","Aldercy","Alderman","Alderson","Aldin","Aldis","Aldo","Aldon","Aldora","Aldos","Aldous","Aldred","Aldredge","Aldric","Aldrich","Aldridge","Alduino","Aldus","Aldwin","Aldwon","Alec","Alecia","Aleck","Aleda","Aleece","Aleedis","Aleen","Aleetha","Alegre",Zosima","Zoubek","Zrike","Zsa","Zsa Zsa","Zsazsa","Zsolway","Zubkoff","Zucker","Zuckerman","Zug","Zulch","Zuleika","Zulema","Zullo","Zumstein","Zumwalt","Zurek","Zurheide","Zurkow","Zurn","Zusman","Zuzana","Zwart","Zweig","Zwick","Zwiebel","Zysk"]
#
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
