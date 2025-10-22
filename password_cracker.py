import hashlib

def crack_sha1_hash(hash_to_find, use_salts=False):
    hash_to_find = hash_to_find.lower().strip()

    
    with open("top-10000-passwords.txt", "r", encoding="utf-8") as f:
        passwords = [line.strip() for line in f if line.strip()]

    
    for pw in passwords:
        if hashlib.sha1(pw.encode()).hexdigest() == hash_to_find:
            return pw 

    
    if use_salts:
        with open("known-salts.txt", "r", encoding="utf-8") as sf:
            salts = [s.strip() for s in sf if s.strip()]
        for salt in salts:
            for pw in passwords:
                if (hashlib.sha1((salt + pw).encode()).hexdigest() == hash_to_find or hashlib.sha1((pw + salt).encode()).hexdigest() == hash_to_find
):
                    return pw

               
                    
    return "PASSWORD NOT IN DATABASE"

