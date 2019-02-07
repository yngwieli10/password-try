password = 'a123456'
n = 3
while n>0:
    psd = input('請輸入密碼:')
    if psd == password:
        print('登入成功')
        break
    else:
        n = n-1
        print('密碼錯誤你還有', n,'次機會')