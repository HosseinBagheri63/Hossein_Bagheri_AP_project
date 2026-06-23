def compress_string_recur(s: str) -> str:
    res=''
    if not s:
        return res
    i=0
    n=1
    while i+1 < len(s) and s[i]==s[i+1]:
        n+=1
        i+=1
    res+= f'{s[i]}{n}'
    return res+compress_string_recur(s[i+1:])