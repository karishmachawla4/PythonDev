try:
    my_file = open('doc.txt',"r")
    data = my_file.readlines()
    evenlist = []
    for line1 in data:
        word = line1.strip(" ")
        word = word.split(" ")
        for w in word:
            if len(w)%2 == 0:
                evenlist.append(w)
    print(evenlist)
except:
    print("Error case")