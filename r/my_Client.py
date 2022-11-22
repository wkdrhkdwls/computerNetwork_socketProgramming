from tkinter import *
import tkinter
import tkinter.messagebox as msg


window = Tk()

window_width = 720
window_height = 800
window_x = 700
window_y = 100

window.geometry('{}x{}+{}+{}'.format(window_width, window_height, window_x, window_y))

window.resizable(False, False)
window.title("클라이언트")

seatFrame = Frame(window, width = 350, height = 700, relief = "sunken", bd = 1, bg = "white")
rsvFrame = Frame(window, width = 330, height = 700, relief = "sunken", bd = 1)

seatFrame.grid(column=0, row=0, padx = 10, pady = 25)
rsvFrame.grid(column=1, row=0, padx = 10, pady = 25)

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

seat_col = 0
seat_row = 0



def onClick():
    MsgBox=msg.askquestion("매매","예약하시겠습니까",icon="info")
    if MsgBox == "yes":
        pass
    # button = tkinter.Radiobutton(rsvFrame, text="예약")
    # button.pack()

#좌석 배치
for seat in seat_list:
    
    if seat_row == 8:
        #중간에 레이블 없이
        Button(seatFrame,text=seat, width=8, height=3).grid(row = seat_row, column = seat_col, padx = 5, pady = 10)
        seat_col += 1
    else:
        if seat_col == 2:
            Label(seatFrame, text = seat, width=8, height=3, bg = "white").grid(row = seat_row, column = seat_col, padx = 5, pady = 10)
        else:
            tkinter.Button(seatFrame, text=seat, width=8, height=3,command=onClick).grid(row = seat_row, column = seat_col, padx = 5, pady = 10)
        seat_col += 1
        if seat_col > 3:
            seat_row += 1
            seat_col = 0
    
#라디오버튼 배치
#예약리스트가 있는지 확인
#리스트에 맞춰 동적 생성
            
window.mainloop()
