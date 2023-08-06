def encode(string):
    ans = ""
    for s in string:
        ans += str(len(s)) + ";" + s
    return ans

# print(encode(["arshia", "izadyar"]))


def decode(string):
    i = 0
    ans = []
    while i < len(string):
        j = i
        while string[j] != ";":
            j += 1
        c = int(string[j - 1])
        s = string[j + 1: j + 1 + c]
        ans.append(s)
        i += j + 1 + c
    return ans
        
print(decode("6;arshia7;izadyar"))