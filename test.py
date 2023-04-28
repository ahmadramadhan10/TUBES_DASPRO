def CekSize(users):
    cnt = 0
    for i in range(102):
        if users[i] == ["","",""]:
            return cnt
        else:   
            cnt = cnt + 1
    return cnt


users = [["t","t","t"],
         ["t","t","t"],
         ["t","t","t"]]