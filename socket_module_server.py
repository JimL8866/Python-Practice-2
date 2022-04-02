import socket

#creat obj
sk = socket.socket()
#set up ip
sk.bind(("127.0.0.1", 9000))
sk.listen()

conn,addr= sk.accept()
print(conn,addr)
conn.send(b"hello")
msg = conn.recv(1024)  # 收多少个字节
print(msg)
conn.close()
sk.close()