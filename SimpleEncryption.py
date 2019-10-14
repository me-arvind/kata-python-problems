def decrypt(encrypted_text, n):
    if n<=0:
        return encrypted_text
    List = list(encrypted_text)
    length = len(encrypted_text)
    if length % 2 ==0:
        split_on = length // 2
    else:
        split_on = (length-1)//2
    first = List[0:split_on]
    second = List[split_on:length]
    resultList = [ second[i//2] if i % 2 == 0 else first[(i-1)//2] for i in range(0,length) ]
    result = ''.join(resultList)
    return decrypt(result,n-1)

def encrypt(text, n):
    if n<=0:
        return text
    List = list(text)
    first = List[::2]
    second = List[1::2]
    encrypted = second + first
    result = ''.join(encrypted)
    return encrypt(result,n-1)