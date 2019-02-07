n=2
while True:
    psssword = input('請輸入密碼:')
    if psssword == 'a123456':
        print('密碼正確')
        break
    else:
        if n >0:
            print(f'你還有{n}次機會')
            n -=1
        else:
            break