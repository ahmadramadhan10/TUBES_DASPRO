def login(users, len_users, current_login, can_access):
    found = False
    new_login = -1
    user_name = input("Username: ")
    password = input("Password: ")
    print("")
    for i in range(len_users):
        if users[i][0] == user_name and not found:
            if users[i][1] != password:
                print("Password salah")
                return current_login
            else:
                new_login = i
                found = True
                
    if not found:
        print("Username tidak terdaftar!")
    else:
        return new_login
    