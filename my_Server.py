import socketserver
from time import sleep


class MyHandler(socketserver.BaseRequestHandler):
    users = {}
    resvList = []
    
    def send_all_msg(self, seat):
        for sock, _ in self.users.values():
            sock.send(seat.encode())
    
    def handle(self):
        print(self.client_address)
        self.users[self.client_address[1]] = (self.request, self.client_address)

        if len(self.resvList) !=0:
            sock, _ = self.users[self.client_address[1]]
            for i in self.resvList:
                msg = "0"+str(i)
                sock.send(msg.encode())
                sleep(0.03)
              
        while True:
            data = self.request.recv(1024)
            msg = data.decode()

            if msg[:1] == "0":   #header
                self.resvList.append(msg[1:]) #index
            elif msg[:1] == "1":
                self.resvList.remove(msg[1:])  
            self.send_all_msg(msg)
            print(self.resvList)           
            
class ChatServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

IP = "192.168.55.67"
PORT = 12000

server = ChatServer((IP,PORT), MyHandler)
server.serve_forever()
server.shutdown()
server.server_close()
