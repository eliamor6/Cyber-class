import socket
cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
cli.connect(('127.0.0.1', port))
for i in range(10):
    guess = ""
    while len(guess) != 4:
        guess = input("enter 4 digits: ")
    cli.send(guess.encode())
    answer = cli.recv(1024).decode()
    print(answer)
    if answer == "you got caught:(, maybe next time you'll win" or answer == "Congratulations, you won":
        cli.close()
        break
    