#!/usr/bin/env python

# Usage: ./icectf.py SILENT

from pwn import *
from base64 import b64encode, b64decode

def discover_block_size(encryption_oracle):
  """ 
  Discover the block size of the cipher given by the oracle (with the size of maximum 128)
  """
  block_size = None
  length = len(encryption_oracle(''))
  for i in range(128):
    prefix = 'a' * i
    new_length = len(encryption_oracle(prefix))
    if new_length > length:
      block_size = new_length - length
      break
  return block_size

def discover_number_of_blocks(encryption_oracle):
  """ 
  Return the number of blocks given by the oracle
  """
  return len(encryption_oracle('')) / discover_block_size(encryption_oracle)

def pkcs7_remove_padding(msg, block_size):
  padding = ord(msg[-1])
  if padding < block_size:
    return msg[:-padding]
  else:
    return msg

def split_to_chucks(s, length):
  """
  Return the array of chucks containing at most 'length' characters
  """
  return [ s[0+i:length+i] for i in range(0, len(s), length) ]

def detect_aes_ecb(msg, block_size = 16):
  """
  Because ECB is is stateless and deterministic, the same 16 byte plaintext block
  will always produce the same 16 byte ciphertext
  """
  blocks = split_to_chucks(msg, block_size)
  total = len(blocks)
  unique = len(set(blocks))
  
  if (total != unique):
    print("[+] Found anomaly, unique blocks:", total, ' total:', unique)
  
  return (total != unique)

def detect_cipher_mode(ciphertext, block_size = 16):
  """
  Detect if the encryption mode was ECB or CBC, for AES-128 
  """
  if detect_aes_ecb(ciphertext, block_size):
    return 'ECB'
  else:
    # print("[+] Detected CBC or not enough blocks provided")
    return 'CBC'

def decrypt_unknown_string(encryption_oracle):
  """
  Iterate through each block and recover the unknown string byte by byte for 
  AES ECB mode
  """
  block_size = discover_block_size(encryption_oracle)
  if (block_size): 
    print("[+] Discovered the block size:", block_size)
  else:
    return False

  # Detect if the function is using ECB
  if (detect_cipher_mode(encryption_oracle('a' * block_size*3), block_size) == "ECB"):
    print("[+] Detected ECB")
  else:
    return False

  num_blocks = discover_number_of_blocks(encryption_oracle)
  print 'num_blocks: ', num_blocks
  known_bytes = ''

  # We skip the first two blocks, after we already know the blocksize!
  for n in range(2, num_blocks):
    # Iterate from 15 to 0 for each block
    for b in range(block_size - 1, -1, -1):
      ciphertext = encryption_oracle('a' * b)
      # Get the currently decrypting block
      block_to_attack = split_to_chucks(ciphertext, block_size)[n]

      for x in range(256):
        ciphertext = encryption_oracle('a' * b + known_bytes + chr(x))
        print('a' * b + known_bytes + chr(x))
        block = split_to_chucks(ciphertext, block_size)[n]
        if block == block_to_attack:
          known_bytes += chr(x)
          break

  decrypted = pkcs7_remove_padding(known_bytes, block_size)
  return decrypted


def encryption_oracle_with_unknown_string(prefix):
  r = remote('l33tcrypt.vuln.icec.tf', 6001)
  # r = remote('0', 6001)

  r.recvuntil("Send me something to encrypt:\n")

  # First 2 blocks which we skip later
  magic = 'l33tserver please'
  data = magic + "X" * (32-len(magic)) + prefix

  r.sendline(b64encode(data))
  
  r.recvuntil('Your l33tcrypted data:\n')
  ciphertext = r.recv(1024)
  ciphertext = b64decode(ciphertext)
  r.close()

  return ciphertext

print(decrypt_unknown_string(encryption_oracle_with_unknown_string))
