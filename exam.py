
with open('2.txt', 'r') as f:
    list_text = f.readlines()
    # print(list_text)
for i in range(51, 101):
    ran = str(i)
    quest_ran = 'quest' + ran
    right_ran = 'r' + ran + 'right'
    ans_ran = 'a' + ran + 'ans'
    for w in list_text:
        a = ''
        b = ''
        if quest_ran in w:
            try:
                a, b, c = w.split('=')
                quest = b
                # print(quest)
            except ValueError:
                print(w)
                print('!!!!!!!!!!!!!!!!!!!!!!!!')
        elif right_ran in w:
            try:
                a, b, c = w.split('=')
                right = b
                # print(right)
            except ValueError:
                print(w)
                print('!!!!!!!!!!!!!!!!!!!!!!!!')
        elif ans_ran in w:
            try:
                a, b, c = w.split('=')
            except ValueError:
                print(ans_ran)
                print(w)
                print('!!!!!!!!!!!!!!!!!!!!!!!!')
            # print(b)
