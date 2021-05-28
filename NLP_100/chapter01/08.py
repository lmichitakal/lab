def cipher(S):
    S = [chr(219 - ord(w)) if 97 <= ord(w) <= 122 else w for w in S]
    return ''.join(S)
S = "this is a message."
enc = cipher(S)
print(enc)
dec = cipher(enc)
print(dec)