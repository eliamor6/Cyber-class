import socket
from map_code import map
map1 = 'files/icehockey.bin'
port = 12345
soc = socket.socket()
soc.bind(('', port))
soc.listen(5)
while True:
    c, addr = soc.accept()
    current_map = map(map1)
    while True:
        order = c.recv(128).decode()
        if order == 'STATUS':
             c.send(current_map.one_step_away().encode())
        else:
            side = order[5:]
            c.send(map.move(side).encode())
            current_map.cop_random_move()
