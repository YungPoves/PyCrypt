from cryptography.fernet import Fernet

def decrypt(data, key):
  try:
    fernet = Fernet(key)
    decryptedString = fernet.decrypt(data)
  except Exception as err:
    print(f"Unexpected {err=}, {type(err)=}")
  return decryptedString

def decryptFile(file, key):
  fernet = Fernet(key)
  with open(file, 'rb') as f:
    encrypted = f.read()
  decrypted = fernet.decrypt(encrypted)
  with open(file, 'wb') as f:
    f.write(decrypted)

'''
# Load the key
with open('filekey.key', 'rb') as f:
  key = f.read()

# Create a fernet object from the key
fernet = Fernet(key)

# Read the encrypted data from the file
with open('file.txt', 'rb') as f:
  encrypted = f.read()

# Decrypt the file content
decrypted = fernet.decrypt(encrypted)

# Write the decrypted data back to the file
with open('file.txt', 'wb') as f:
  f.write(decrypted)
'''