from csv import DictReader
from collections import Counter

def leankloud(a):
    f1=DictReader(a)
    name=[]
    math=[]
    bio=[]
    eng=[]
    phy=[]
    chem=[]
    hin=[]

    for i in f1:
        name.append(i['Name'])
        math.append(int(i['Maths']))
        bio.append(int(i['Biology']))
        eng.append(int(i['English']))
        phy.append(int(i['Physics']))
        chem.append(int(i['Chemistry']))
        hin.append(int(i['Hindi']))

    max=math[0]
    for i,j in zip(range(len(name)),range(len(math))):
        if math[j]>max:
            max=math[j]
            k=j
    print('Topper in Maths is',name[k],'with',max,'Marks')

    max=bio[0]
    for i,j in zip(range(len(name)),range(len(bio))):
        if bio[j]>max:
            max=bio[j]
            k=j
    print('Topper in Biology is',name[k],'with',max,'Marks')

    max=eng[0]
    for i,j in zip(range(len(name)),range(len(eng))):
        if eng[j]>max:
            max=eng[j]
            k=j
    print('Topper in English is',name[k],'with',max,'Marks')

    max=phy[0]
    for i,j in zip(range(len(name)),range(len(phy))):
        if phy[j]>max:
            max=phy[j]
            k=j
    print('Topper in Physics is',name[k],'with',max,'Marks')

    max=chem[0]
    for i,j in zip(range(len(name)),range(len(chem))):
        if chem[j]>max:
            max=chem[j]
            k=j
    print('Topper in Chemistry is',name[k],'with',max,'Marks')

    max=hin[0]
    for i,j in zip(range(len(name)),range(len(hin))):
        if hin[j]>max:
            max=hin[j]
            k=j
    print('Topper in Hindi is',name[k],'with',max,'Marks'),print()

    topper_list={}
    for  a,b,c,d,e,g,f in zip(name,math,eng,bio,phy,chem,hin):
        su=int(b)+int(c)+int(d)+int(e)+int(g)+int(f)
        topper_list[a]=su
    # print(topper_list),print()


    c=Counter(topper_list)
    top_three=c.most_common(3)
    s=[]
    for i in top_three:
        s.append(i[0])
    print('Best students in the class are {}, {}, {}'.format(s[0],s[1],s[2]))
f=open('Student_marks_list.csv','r')
leankloud(f)