from cryptography.fernet import Fernet

# add key variable
# password variable
def encrypt(data, key):
  fernet = Fernet(key)
  encryptedString = fernet.encrypt(data)
  return encryptedString

def encryptFile(file, key):
  fernet = Fernet(key)
  with open(file, 'rb') as f:
    original = f.read()
  encrypted = fernet.encrypt(original)
  with open(file, 'wb') as f:
    f.write(encrypted)

'''
# Generate a key
key = Fernet.generate_key()

# Save the key into a file
with open('filekey.key', 'wb') as f:
  f.write(key)

# Load the key from the .key file
with open('filekey.key', 'rb') as f:
  key = f.read()

# Create a fernet object using the key
fernet = Fernet(key)

# Open the file to be encrypted in binary read mode
with open('file.txt', 'rb') as f:
  original = f.read()

# Encrypt the file content
encrypted = fernet.encrypt(original)

# Overwrite the original file with the encrypted data
with open('file.txt', 'wb') as f:
  f.write(encrypted)
'''