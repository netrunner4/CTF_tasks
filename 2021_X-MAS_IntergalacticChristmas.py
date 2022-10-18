import socket

prime50000000 = []
with open("5000000prime.csv", "r") as f: #file with prime numbers up to 5000000
    lines = f.readlines()
for line in lines:
    prime50000000.append(int(line.strip()))

def isprime(num):
    for i in range(120):
        if num%(i+2) == 0:
            return False
    if num in prime50000000:
        return True
    return False


def solve(numbers, queries):
    Nicenium = []
    Naughtynium = []

    for i in numbers:
        if i == 1:
            Naughtynium.append(i)
        elif isprime(i):
            Nicenium.append(i)
        else:
            Naughtynium.append(i)
    print("prime done")
    Christmasium = []
    for i in range(len(Nicenium)):
        for j in range(len(Naughtynium)):
            Christmasium.append(Nicenium[i]+Naughtynium[j])
    print("list done")
    Christmasium1 = sorted(Christmasium)
    print(len(Christmasium1))
    globallist.append(Christmasium1)
    answer = []
    for i in queries:
        answer.append(Christmasium1[i-1])
    return answer

def Convert(string):
    li = list(string.split(", "))
    return li

def datasolve(data):
    pos1 = (data.decode().find("numbers"))
    pos2 = (data.decode().find("]"))
    numbers = (data.decode()[pos1+10:pos2+1])
    numbers = numbers[1:-1]
    pos3 = (data.decode().find("queries"))
    pos4 = (data.decode().find("answers"))
    queries = (data.decode()[pos3+10:pos4-1])
    queries = queries[1:-1]
    numbers = (Convert(numbers))
    queries = (Convert(queries))
    realnumbers = [int(i) for i in numbers]
    realqueries = [int(i) for i in queries]
    answer = solve(realnumbers, realqueries)
    s.send(str(answer).encode()+"\n".encode())

def strsolve(data):
    pos1 = (data.find("numbers"))
    pos2 = (data.find("]"))
    numbers = (data[pos1 + 10:pos2 + 1])
    numbers = numbers[1:-1]
    pos3 = (data.find("queries"))
    pos4 = (data.find("answers"))
    queries = (data[pos3 + 10:pos4 - 1])
    queries = queries[1:-1]
    numbers = (Convert(numbers))
    queries = (Convert(queries))
    realnumbers = [int(i) for i in numbers]
    realqueries = [int(i) for i in queries]
    answer = solve(realnumbers, realqueries)
    s.send(str(answer).encode() + "\n".encode())

globallist = []

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("challs.xmas.htsp.ro", 5006))

data = s.recv(2048)
print(data)
data = s.recv(2048)
print(data)
data = s.recv(2048)
print(data)
datasolve(data)

datastr = ''

while True:
    data = s.recv(50000)
    datastr += data.decode()
    print(data.decode())
    if data[-4:].decode() == "s = ":
        strsolve(datastr)
        datastr = ''