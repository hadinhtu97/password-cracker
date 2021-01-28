import hashlib


def crack_sha1_hash(hash, use_salts=False):

    top_passwords = open('./data/top-10000-passwords.txt', 'r')

    for p in top_passwords:
        if use_salts == False:
            if hash == hashlib.sha1(p.strip().encode()).hexdigest():
                return p.strip()
        else:
            know_salts = open('./data/know-salts.txt', 'r')
            for s in know_salts:
                if hashlib.sha1((s.strip()+p.strip()).encode()).hexdigest() == hash:
                    return p.strip()
            know_salts.close()

    top_passwords.close()
    return 'PASSWORD NOT IN DATABASE'
