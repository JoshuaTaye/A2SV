def gradingStudents(ng):
    assert 1<=ng<=60
    g=0
    lst=[]
    while len(lst)<ng:
        nu=input()
        lst.append(nu)
    for i in lst: 
        i=int(i)
        if i>=38:
            s=((i//5+1)*5)
            if s-i<3:
                print(s)    
            elif s-i>=3:
                print(i) 
        else:
            print(i)
ng=int(input()) 
gradingStudents(ng)   
