MOD = 10**16 + 61
BAS = 200

#returns true if there exists a duplicate substring of length n in s
def ok(s, n):
    if n == 0:
        return True
    if n == 1:
        if len(set(list(s))) == len(list(s)):
            return False
        else:
            return True
    cur = 0
    rem = pow(BAS, n-1, MOD) # biggest multiple
    seen = {}
    for i in range(n):
        cur = (cur * BAS) % MOD #multiply by p
        cur = (cur + ord(s[i])) % MOD #add next char
    
    seen[cur] = True
    for i in range(n, len(s) - 1):
        
        cur = (cur - ord(s[i - n]) * (rem)) % MOD #remove last character
        cur = (cur * BAS + ord(s[i])) % MOD #add new character
        
        if cur in seen:
            return True
        seen[cur] = True

    return False
