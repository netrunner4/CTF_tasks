import socket

def countsum(word):
    answer = 0
    alphabet = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11,
                "m": 12,
                "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23,
                "y": 24, "z": 25}
    for i in word:
        answer += alphabet[i]
    return answer
host = "code.deadface.io"
port = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

data = s.recv(2048).decode()
first = data[196:].strip()
print(countsum(first), first)
s.send(str(countsum(first)).encode())
for i in range(10):
    data = s.recv(2048).decode()
    print(data)

# wtf too easy, need to solve 1 time, 275 points

