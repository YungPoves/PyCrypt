from cryptography.fernet import Fernet

def loadKey(keyfile):
  with open(keyfile, 'rb') as f:
    key = f.read()
    return key

def generateKey():
  key = Fernet.generate_key()
  print("Generated new key:", key)
  return key

def saveKey(keyfile, key):
  with open(keyfile, 'wb') as f:
    f.write(key)