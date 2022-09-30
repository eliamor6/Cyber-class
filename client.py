import socket
import keyboard
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
soc.connect(('127.0.0.1', port))

def move(direction, soc):
    soc.send(('MOVE ' + side).encode())
    print(soc.recv(128).decode())

def status(soc):
    soc.send('STATUS'.encode())
    print(soc.recv(128).decode())

keyboard.add_hotkey('up', move, args=('UP', soc))
keyboard.add_hotkey('down', move, args=('DOWN', soc))
keyboard.add_hotkey('right', move, args=('RIGHT', soc))
keyboard.add_hotkey('left', move, args=('LEFT', soc))
keyboard.add_hotkey('s', args=[soc])
keyboard.wait('esc')