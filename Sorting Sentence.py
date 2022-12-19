def sortSentence(s) -> str:
    lst=[]
    for i in s:
        lst.append(i)
    for i in s:
        s[s.index(i)]=s[s.index(i)].replace('"','')
    for k in s:
        j=int(k[-1])
        s[s.index(k)],lst[j-1]=lst[j-1],s[s.index(k)]
    for j in lst:
        lst[lst.index(j)]=lst[lst.index(j)].replace(j[-1],'')
    print(*lst)
s=list((input().strip().split()))
sortSentence(s)
#"KTFkUVVrmYMSo2 wXlQraUqblfhCfDLK3 IfTuftYVualQ6 NhpQ5 HlRjClVtQrTFcwbx4 fi1"