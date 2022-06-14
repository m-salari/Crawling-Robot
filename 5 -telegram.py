def found_chat_id(app, group_id):  
    try:
        app.join_chat(group_id)  # if not join to group, its join your account
    except:
        print('Error Join To Group.')
    with open('./telegram_username.txt', 'a+') as f:  # found and write id's in text file
        with open('./telegram_username.txt', 'r+') as fr:
            ids = []
            sended = []
            for i in fr.readlines():
                ids.append(i.replace('\n', ''))  # append ID with out '\n'

            for i in ids:
                sended.append(i[1:])  # append ID with out '-'
            my_username = app.get_users("me").username
            for u in app.iter_chat_members(group_id):
                if (type(u.user.username) == str) and (u.user.username[1:] not in ids) and (u.user.username not in sended):
                    if u.user.username == my_username:
                        continue
                    f.write(u.user.username + '\n')
    print('group member id\'s are found.\n')
