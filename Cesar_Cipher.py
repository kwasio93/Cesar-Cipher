def c_t(a):
    tab=[]
    for i in range(0,26):
        tab.append(chr(i+a))
    return tab

Duze=c_t(65)
Male=c_t(97)

def isAlpha(a):
    if (ord(a)>=65 and ord(a)<65+26) or (ord(a)>=97 and ord(a)<97+26):
        return 1
    else:
        return 0
def isUpper(a):
    if (ord(a)>=65 and ord(a)<65+26):
        return 1
    else:
        return 0
def isLower(a):
    if (ord(a)>=97 and ord(a)<97+26):
        return 1
    else:
        return 0

def szyfr(string,D,M,key,isAlpha,isUpper,isLower):
    zaszyfrowane=''
    if abs(key)>len(D):
        if key>=0:
            diff=key//len(D)
            print(diff)
            key=key-diff*len(D)
            key=key
            
        else:
            key=-key
            diff=key//len(D)
            key=key-diff*len(D)
            key=-key
    for i in range(0,len(string)):
        if isAlpha(string[i])==1:
            if isUpper(string[i])==1:
                for j in range(0,len(D)):
                    if string[i]==D[j]:
                        if j+key<len(D):
                            zaszyfrowane+=D[j+key]
                        else:
                            zaszyfrowane+=D[j+key-len(D)]
            else:
                for j in range(0,len(M)):
                    if string[i]==M[j]:
                        if j+key<len(M):
                            zaszyfrowane+=M[j+key]
                        else:
                            zaszyfrowane+=M[j+key-len(M)]
        else:
            zaszyfrowane+=string[i]
                
    return zaszyfrowane
def main():
    print(szyfr("WARSZAWA",Duze,Male,-2,isAlpha,isUpper,isLower))
    
main()