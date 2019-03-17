string = "E<>"

for i in range(3):
    for j in range(3):
        if not (i == 0 and j == 0):
            for k in range(4):
                string += "visited[%s][%s][%s] <= 1 && " % (i, j, k)
        else:
            for k in range(4):
                string += "visited[%s][%s][%s] <= 2 && " % (i, j, k)

for i in range(3):
    for j in range(3):
        string += '('
        for k in range(4):
            string += "visited[%s][%s][%s] + " % (i, j, k)
        string = string[:-3] + ") > 0 && "
string += "locX == 0 && locY == 0"
print(string)
