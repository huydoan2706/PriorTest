# Given a binary string s without leading zeros,
# return true if s contains at most one contiguous segment of ones.
# Otherwise, return false.

def Check(s):
    count = 0
    limit = False
    for i in range(len(s)):
        if s[i] == "1":
            count += 1
        else:
            if count < 1:
                count = 0
                continue
            else:
                if not limit:
                    limit = True
                    count = 0
                else:
                    return False
    if count >= 1 and limit == False:
        limit = True
        count = 0
    if limit == True and count >= 1:
        return False
    if limit == False:
        return False
    return True

s = '1000011110000'
print(Check(s))



