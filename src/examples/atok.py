def reversePhrase(word):
    """
    Takes a string of words and returns them in reverse order

    Arguments:
    phrase(str): phrase to be reversed

    Returns:
    str: phrase in reverse order
    """
    i = len(word)-1
    start = end = i+1
    result = ''
    while i>=0:
        if word[i] == ' ':
            start = i+1
    while start!= end:
        result += word[start]
    start+=1
    result+=' '
    end = i
    i-=1
    start = 0
    while start!=end:
        result+=word[start]
    start+=1
    return result
print(reversePhrase('A man, a plan, a canal, Panama!'))
