def Search(txt,pat):
    m=len(pat)
    n=len(txt)
    for i in range(0,n-m+1):
        j=0
        while j<m:
            if txt[i+j]!=pat[j]:
                j=j+1
            if (j==m):
                print("the match is found at index:",i)
txt="ababc"
pat="abc"
Search(txt,pat)
