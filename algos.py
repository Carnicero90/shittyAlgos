def rota(l1, l2):
    if len(l1) == len(l2):
        k = l1[0]
        for i in range(len(l1)):
            if (l2[i] == k) and (l1 == l2[i:]+l2[:i]):
                return True
    return False

print(rota([1,2,3],[2,3,1]))

def rev(s):
    w, out = '',''
    for letter in s:
        if letter == ' ':
            out = letter + w + out
            w = ''
        else: w += letter
    out = w + out
    return out

print(rev('funziona se vediamo'))

def twoMax(arr):
    if len(arr) > 1:
        a, b = arr[0], arr[1]
        for i in arr[2:]:
            if b > a:
                a, b = b, a
            if i > b:
                b = i
        return (a, b)

print(twoMax([1,-12,21,32,-7,7,5]))
