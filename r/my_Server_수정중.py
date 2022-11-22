import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    users = {}
    userResv = {}
    userId = 0
    
    def send_all_reserves(self, seat):
        for sock, a in self.users.values(): #key: value , value:socket, _
            sock.send(seat.encode())# 여기서 메시지를 보내는 것임.
    
    def handle(self):
        print(self.client_address)
        # userId += 1
        
        while True: #userId 늘려서 decode로 문자열으로 출력
            self.request.send("닉네임을 입력하세요 : ".encode())
            nickname = self.request.recv(1024).decode()
            
            self.users[nickname] = (self.request, self.client_address)
            self.send_all_message("{}번사람 예약".format(nickname)) #메시지를 여기서 보낸다.(send_all_reserve 불러와서)
            break
        
        while True:
            msg = self.request.recv(1024)
            # self.userResv[userId] = (msg.decode())
            self.send_all_reserves(msg.decode())
            
class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server = ChatServer(("",12000), MyHandler)
server.serve_forever()
server.shutdown()
server.server_close()
