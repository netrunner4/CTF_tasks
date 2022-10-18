import socket
import time


def wtf(b, d):
    test = d
    max_col = len(test[0])
    max_row = len(test)
    cols = [[] for _ in range(max_col)]
    rows = [[] for _ in range(max_row)]
    fdiag = [[] for _ in range(max_row + max_col - 1)]
    bdiag = [[] for _ in range(len(fdiag))]
    min_bdiag = -max_row + 1

    for x in range(max_col):
        for y in range(max_row):
            cols[x].append(test[y][x])
            rows[y].append(test[y][x])
            fdiag[x + y].append(test[y][x])
            bdiag[x - y - min_bdiag].append(test[y][x])
    end_list = []
    for i in range(len(cols)):
        if b in "".join(cols[i]):
            for k in range(len(cols) - 2):
                if b[0] == cols[i][k] and b[1] == cols[i][k + 1] and b[2] == cols[i][k + 2]:
                    for j in range(len(b)):
                        end_list += [(i, k + j)]

    for i in range(len(rows)):
        if b in "".join(rows[i]):
            for k in range(len(rows) - 2):
                if b[0] == rows[i][k] and b[1] == rows[i][k + 1] and b[2] == rows[i][k + 2]:
                    for j in range(len(b)):
                        end_list += [(k + j, i)]

    for i in range(len(bdiag)):
        if b in "".join(bdiag[i]):
            start_x_y = (16 - len(bdiag[i]))
            for k in range(len(bdiag[i]) - 2):
                if b[0] == rows[start_x_y + k][k] and b[1] == rows[start_x_y + k + 1][k + 1] and b[2] == \
                        rows[start_x_y + k + 2][k + 2]:
                    for j in range(len(b)):
                        end_list += [(k + j, start_x_y + k + j)]
            for k in range(len(bdiag[i]) - 2):
                if b[0] == rows[k][start_x_y + k] and b[1] == rows[k + 1][start_x_y + k + 1] and b[2] == rows[k + 2][
                    start_x_y + k + 2]:
                    for j in range(len(b)):
                        end_list += [(start_x_y + k + j, k + j)]
    b = b[::-1]
    for i in range(len(fdiag)):
        if b in "".join(fdiag[i]):
            start_x_y = (len(fdiag[i]) - 1)
            for k in range(len(fdiag[i]) - 2):
                if b[0] == d[start_x_y - k][k] and b[1] == d[start_x_y - k - 1][k + 1] and b[2] == d[start_x_y - k - 2][
                    k + 2]:
                    for j in range(len(b)):
                        end_list += [(k + j, start_x_y - k - j)]
                    end_list = end_list[::-1]
            for k in range(len(fdiag[i]) - 2):
                if b[-1] == d[15 - (start_x_y - k)][15 - k] and b[-2] == d[15 - (start_x_y - k - 1)][15 - (k + 1)] and \
                        b[-3] == d[15 - (start_x_y - k - 2)][15 - (k + 2)]:
                    for j in range(len(b)):
                        end_list += [(15 - (k + j), 15 - (start_x_y - k - j))]
    end_list_final = []
    for i in end_list:
        if i not in end_list_final:
            end_list_final.append(i)

    if end_list_final == []:
        a = input("right/down/leftbot/rightbot")
        x = int(input("x start"))
        y = int(input("y start"))
        leng = int(input("length"))
        if a == "right":
            for i in range(leng):
                end_list_final += [(x + i, y)]
        if a == "down":
            for i in range(leng):
                end_list_final += [(x, y + i)]
        if a == "leftbot":
            for i in range(leng):
                end_list_final += [(x - i, y + i)]
        if a == "rightbot":
            for i in range(leng):
                end_list_final += [(x + i, y + i)]
    return (end_list_final)


host = "challenge.ctf.games"
port = 31940
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
    data = s.recv(2048)
    print(data)
    if data == b"\nLet's play a game of wordsearch! We will display the grid\nand offer you words to find. Please submit the locations of\neach word in the format [(X, Y), (X, Y), (X, Y), ...] for each letter.\n\nPlease enter 'example' if you would like to see an \nexample, or 'play' if you would like to get started.\n> ":
        s.send(b"play")
        break

time.sleep(2)
for i in range(1):
    data = s.recv(2048).decode()
    print(data, i)
    data = data.splitlines()
d = []
for i in range(19):
    d += [(data[i].split())]
del d[0]
del d[0]
del d[0]
for i in range(len(d)):
    del d[i][0]
    del d[i][0]
print(data[-1])
b = (data[-1][0:(data[-1].find(":"))])
s.send(str((wtf(b, d))).encode())
print("sent data", wtf(b, d))

while True:
    data = s.recv(2048).decode()
    if data == "Congratulations! You finished that word search!\n":
        break
    if data == "> ":
        continue
    print(data)
    b = (data[0:(data.find(":"))])
    s.send(str(wtf(b, d)).encode())
    print("sent data", wtf(b, d))

for i in range(30):
    time.sleep(2)
    for i in range(1):
        data = s.recv(2048).decode()
        print(data)
        data = data.splitlines()
    d = []
    for i in range(21):
        d += [(data[i].split())]
    del d[0]
    del d[0]
    del d[0]
    del d[0]
    del d[0]
    for i in range(len(d)):
        del d[i][0]
        del d[i][0]

    b = (data[-1][0:(data[-1].find(":"))])
    s.send(str((wtf(b, d))).encode())
    print("sent data", wtf(b, d))

    while True:
        data = s.recv(2048).decode()
        if data == "Congratulations! You finished that word search!\n":
            break
        if data == "> ":
            continue
        print(data)
        b = (data[0:(data.find(":"))])
        s.send(str((wtf(b, d))).encode())
        print("sent data", wtf(b, d))
print("end")
