# First draws of code

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

code = 2

# Create a new alphabet based on defined code
# In this case, the lis behavior is like circular. Whe i get next to end of alphabet
# the i is update from begining
new_alphabet = [alphabet[i+code] if (i+code) < len(alphabet) else alphabet[(i- len(alphabet))+code] for i in range(0, len(alphabet), 1)]

dict_encrypt = {}
dict_decrypt = {}

# Create two dictionaries, onde to encrypt message and another to decrypt
for i in range(0, len(alphabet), 1):
    dict_encrypt[alphabet[i]] = new_alphabet[i]
    dict_decrypt[new_alphabet[i]] = alphabet[i]

# Examples of how the code will funciton with capital letters from alphabet
message = "MY NAME IS CAESER"
encrypt_message = ""
decrypt_message = ""

for m in message:
    if m in alphabet:
        encrypt_message += dict_encrypt[m]
    else:
        encrypt_message += m     

for m in encrypt_message:
    if m in alphabet:
        decrypt_message += dict_decrypt[m]
    else:
        decrypt_message += m

print(encrypt_message)
print(decrypt_message)
