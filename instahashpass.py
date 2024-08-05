import bcrypt


def hash_password(password):
    salt = bcrypt.gensalt(rounds=12)
    hashed_pass = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_pass.decode('utf-8')


p = input("enter the plaintext passwrd: ")
h_pass = hash_password(f'{p}')
print(h_pass)
