# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=12345
# s.connect((HOST_NAME,PORT))


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=12345
# s.connect((HOST_NAME,PORT))
# msg=s.recv(100)
# print(msg.decode("utf-8"))


# import socket
# s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# HOST_NAME=socket.gethostname()
# PORT=12345
# s.connect((HOST_NAME,PORT))
# while (1):
#     msg=s.recv(100)
#     print("server:",msg.decode("utf=8"))
#     message_to_send=input("client:")
#     s.send(bytes(message_to_send,"utf=8"))



import socket

from tkinter import *
def send(listbox,entry):
    message=entry.get()
    listbox.insert("end","client:" +message)
    entry.delete(0,END)
    s.send(bytes(message, "utf=8"))

def recive(listbox):
    message = s.recv(100)
    listbox.insert("end","server:"+ message.decode("utf-8"))

root=Tk()
entry=Entry()
entry.pack(side=BOTTOM)
listbox=Listbox(root)
listbox.pack()
button=Button(root,text="send",command=lambda :send(listbox,entry))
button.pack(side=BOTTOM)

rbutton=Button(root,text="recive",command=lambda :recive(listbox))
rbutton.pack(side=BOTTOM)
root.title("CLIENT")

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST_NAME=socket.gethostname()
PORT=12345
s.connect((HOST_NAME,PORT))

root.mainloop()
    