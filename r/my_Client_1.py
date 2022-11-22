from tkinter import *
import socket
from threading import Thread
import tkinter
    
IP = ""
PORT = 0

resvSeats = []
seatButtons = []
resvRadioButtons = []

seat_list = [
    '1A','1B','','1C', #0
    '2A','2B','','2C', #1
    '3A','3B','','3C', #2
    '4A','4B','','4C', #3
    '5A','5B','','5C', #4
    '6A','6B','','6C', #5
    '7A','7B','','7C', #6
    '8A','8B','','8C', #7
    '9A','9B','9C','9D' ] #8

def connect(event=None):
    global IP,PORT
    connect_string = input_string.get()
    addr = connect_string.split(":")
    IP = addr[0]
    PORT = int(addr[1])
    w_connect.destroy()
    
def send_user(event = None):
    msg = input_user.get()
    sock.send(msg.encode())
    pass

def recv_permission(sock):
    while True:
        msg = sock.recv(1024)
        if msg.decode() == "Enter":
            u_connect.destroy()            

def recv_reservation(sock):
    while True:
        msg = sock.recv(1024)
        seatButtons[i].configure(bg = "blue")
    
def send_reservation(i):
    sock.send(i.encode())
    seatButtons[i].configure(bg = "blue")
    
    #이 리스트는 내 클라이언트에서 예약된 좌석을 의미
    resvSeats.append(seatButtons[i])

def send_cancel():
    pass
    #예약을 취소하는 함수

#서버 연결 부분
w_connect = Tk()
w_connect.title("접속 대상")
tkinter.Label(w_connect, text="접속 대상").grid(row=0, column=0)
input_string = tkinter.StringVar(value="127.0.0.1:12000")
input_addr = tkinter.Entry(w_connect, textvariable=input_string, width=20)
input_addr.grid(row=0, column=1, padx=5, pady=5)
c_button = tkinter.Button(w_connect, text="접속하기", command=connect)
c_button.grid(row=0, column=2, padx=5, pady=5)

width = 330
height = 45

screen_width = w_connect.winfo_screenwidth()
screen_height = w_connect.winfo_screenheight()

x = int((screen_width / 2) - (width/2))
y = int((screen_height / 2) - (height/2))

w_connect.geometry('{}x{}+{}+{}'.format(width, height, x, y))
w_connect.mainloop()

#유저 확인 부분


#예약부분
window = Tk()

window_width = 720
window_height = 800
window_x = 700
window_y = 100

window.geometry('{}x{}+{}+{}'.format(window_width, window_height, window_x, window_y))

window.resizable(False, False)
window.title("버스 좌석 예매")

seatFrame = Frame(window, width = 0, height = 0, relief = "sunken", bd = 1, bg = "white")
rsvFrame = Frame(window, width = 0, height = 0, relief = "sunken", bd = 1)
seatFrame.grid(column=0, row=0, padx = 10, pady = 25)
rsvFrame.grid(column=1, row=0, padx = 10, pady = 25)

seat_col = 0
seat_row = 0

#좌석 배치
for i in range(len(seat_list)):
    def action(t = i):
        send_reservation(t)
        
    if seat_row == 8:
        #중간에 레이블 없이
        seat_button = Button(seatFrame, text = seat_list[i], width=8, height=3, command = action)
        seat_button.grid(row = seat_row, column = seat_col, padx = 5, pady = 10)
        seat_col += 1
    else:
        if seat_col == 2:
            seat_button = Label(seatFrame, text = seat_list[i], width=8, height=3, bg = "white")
            seat_button.grid(row = seat_row, column = seat_col, padx = 5, pady = 10)
        else:              
            seat_button = Button(seatFrame, text = seat_list[i], width=8, height=3, command = action)
            seat_button.grid(row = seat_row, column = seat_col, padx = 5, pady = 10)
        seat_col += 1
        
        if seat_col > 3:
            seat_row += 1
            seat_col = 0
    seatButtons.append(seat_button)



sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((IP,PORT))

th = Thread(target=recv_message, args=(sock, ))
th.daemon = True
th.start()
            
window.mainloop()
