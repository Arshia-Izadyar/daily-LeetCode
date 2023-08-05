def isAnagram(s, t):
    if len(s) != len(t):
        return False
    return True if sorted(s) == sorted(t) else False