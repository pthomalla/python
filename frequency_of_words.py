lines = int(input(""))
dict = {}
while lines > 0:
    lines = lines - 1
    word = input("")
    dict[word] = dict.get(word,0) + 1
print_word = int(input(""))

def bisect_left(a, x):
    hi = len(a)
    lo = 0
    while lo < hi:
        mid = (lo+hi)//2
        if a[mid][0] > x[0] or (a[mid][0] == x[0] and a[mid][1] < x[1]):
            lo = mid+1
        else: hi = mid
    return lo
most_frequent = []
for word, frequent in dict.items():
    wpis = (frequent,word)
    pos = bisect_left(most_frequent,wpis)
    most_frequent.insert(pos,wpis)
    if len(most_frequent) > print_word : 
        most_frequent.pop()
for word in most_frequent:
    print(word[1])
