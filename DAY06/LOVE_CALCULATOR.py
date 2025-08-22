N1 = input("Enter the first name: ")
N2 = input("Enter the second name: ")
def calculate_love_score(name1, name2):
    name = name1 + name2
    #combined = list(name.lower())
    total = 0
    total1 = 0
    #for i in combined:
    for i in name:
        #if i=="t" or i=="r" or i=="u" or i=="e" :
        if i in "true":
            total +=1
        #for i in combined:
    for i in name:
        if i in "love":
            total1 +=1
    print("LOVE Calculated:",str(total) + str(total1))
calculate_love_score(N1,N2)
