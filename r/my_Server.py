import socketserver

class MyHandler(socketserver.BaseRequestHandler):
    users = {}
    userResv = {}
    userId = 0
    
    def send_all_reserves(self, seat):
        for sock, _ in self.users.values():
            sock.send(seat.encode())
    
    def handle(self):
        print(self.client_address) #baserequest에 속한애
        userId += 1
        
        while True:
            msg = self.request.recv(1024)
            self.userResv[userId] = (msg.decode())
            self.send_all_reserves(msg.decode())
            
class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server = ChatServer(("",12000), MyHandler)
server.serve_forever()
server.shutdown()
server.server_close()
