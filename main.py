import rsa

# generate a key pair
public_key, private_key = rsa.newkeys(512)

# write the keys to file
with open("public.pem", "wb") as f:
    f.write(public_key.save_pkcs1())

with open("private.pem", "wb") as f:
    f.write(private_key.save_pkcs1())

message = "Hello i'm a software engineering student!"

encrypted_message = rsa.encrypt(message.encode(), public_key)
print(encrypted_message)

with open("encrypted.message", "wb") as f:
    f.write(encrypted_message)

encrypted_message = open("encrypted.message", "rb").read()

clear_message = rsa.decrypt(encrypted_message, private_key)
print(clear_message.decode())

msg = "hello darkness my old friend i've come to talk with you again"
signature = rsa.sign(msg.encode(), private_key, "SHA-256")
with open("signature", "wb") as f:
    f.write(signature)

with open("signature", "rb") as f:
    signature = f.read()
print(rsa.verify(msg.encode(), signature, public_key))
