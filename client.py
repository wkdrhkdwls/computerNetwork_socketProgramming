import socket

print("1. 소켓 생성")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("3. 접속 시도")
sock.connect(("127.0.0.1", 12000))

print("5. 데이터 송/수신")
sock.sendall("Hello socket programming".encode())

print("6. 접속종료")
sock.close()
# HOST = "127.0.0.1"
# PORT = 12346

# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((HOST, PORT))
# s.sendall(b"")
# data = s.recv(1024)
# print("Response: {}".format(data))
