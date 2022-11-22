import socketserver
from time import sleep


class MyHandler(socketserver.BaseRequestHandler):
    users = {}
    resvList = []
    
    def send_all_reserves(self, seat):
        for sock, _ in self.users.values():
            sock.send(seat.encode())
    
    def handle(self):
        print(self.client_address)
        self.users[self.client_address[1]] = (self.request, self.client_address)
        if len(self.resvList) !=0:
            sock, _ = self.users[self.client_address[1]]
            for i in self.resvList:
                sock.send(i.encode())
                sleep(0.01)
              
        while True:
            msg = self.request.recv(1024)
            self.send_all_reserves(msg.decode())
            self.resvList.append(msg.decode())
            
class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

server = ChatServer(("",12000), MyHandler)
server.serve_forever()
server.shutdown()
server.server_close()
