import bcrypt

pw = b'passy12'
s = bcrypt.gensalt()
h = bcrypt.hashpw(pw, s) # Hash password
print(h)
entered_pw = (input('enter your password here: ')).encode()

if bcrypt.checkpw(entered_pw, h):
    print("Password match!")
else:
    print("Incorrect password.")