import bcrypt
import time

username = ["aa", "ab", "bb", "aaa", "aab", "aba", "baa", "bab", "bba"]
passwords = ["xstv", "pomme", "poire", "peche", "fruit", "fuite", "fraise", "banane", "lemon"]

hashes1 = []
salts = []
for password in passwords:
    print('first password')
    """ Salt rounds to increase the time it takes to generate a hash"""
    salt = bcrypt.gensalt(rounds=4)
    # salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password.encode('utf8'), salt)
    hashes1.append(hash)
    salts.append(salt)


file = open("hash_bcrypt.txt", "w")
for index in range(len(username)):
    file.write(str(username[index]) + ":" + str(hashes1[index]) + ":" + salts[index].decode('utf8') + "\n")
file.close()

username = input("Enter username: ")
pwd = input("Enter password: ")

f = open("hash_bcrypt.txt", "r")

user_name = None
hash_user = None
salt_user = None
for line in f:
    user = line.split(":")
    if username == user[0]:
        user_name = username
        hash_user = user[1]
        salt_user = user[2]

if user_name is not None:
    new_hash = bcrypt.hashpw(pwd.encode(), salt_user.encode('utf8'))
    if str(new_hash) == hash_user:
        result = True
    else:
        result = False
    try:
        """Not working"""
        bcrypt.checkpw(str(pwd).encode('utf8'), salt_user.encode('utf8'))
        result1 = True
    except e as Exception :
        print(e)
        result1 = False
    print("Bcrypt verify (correct password):", result)
    print("Bcrypt verify (correct password):", result1)
