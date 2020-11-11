'''
Descripttion: 
version: 
Author: @***
Date: 2020-11-11 10:42:13
LastEditors: @***
LastEditTime: 2020-11-11 15:46:44
'''
from socket import *
import base64
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"
# Choose a mail server (e.g. Google mail server) and call it mailserver 
mailserver = "smtp.qq.com"#Fill in start   #Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
fromaddress = "*****@qq.com"
toaddress = "*****@qq.com"
user = base64.b64encode(b'*****@qq.com').decode() + '\r\n'
password = base64.b64encode(b'*****').decode() + '\r\n'
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((mailserver,25))

#Fill in end
recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print ('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print ('250 reply not received from server.')
#请求登录
clientSocket.sendall(("AUTH LOGIN\r\n").encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '334'):
	print('334 reply not received from server')
#输入用户名和密码
clientSocket.send(user.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '334'):
	print('334 reply not received from server')
    
clientSocket.send(password.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '235'):
	print('235reply not received from server')
# Send MAIL FROM command and print server response.
# Fill in start
header ="MAIL FROM:<"+fromaddress+">\r\n"
clientSocket.send(header.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '250'):
    	print('250 reply not received from server')
# Fill in end


# Send RCPT TO command and print server response.
# Fill in start
foot = "RCPT TO:<"+toaddress+">\r\n"
clientSocket.send(foot.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '250'):
    	print('250 reply not received from server')
# Fill in end

# Send DATA command and print server response.
# Fill in start
foot = "DATA\r\n"
clientSocket.send(foot.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '354'):
    	print('354 reply not received from server')
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end 

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '250'):
    	print('250 reply not received from server')
# Fill in end

# Send QUIT command and get server response.
# Fill in start
foot = "QUIT\r\n"
clientSocket.send(foot.encode())
recv = clientSocket.recv(1024).decode()
print(recv)
if (recv[:3] != '221'):
    	print('221 reply not received from server')
# Fill in end
 