#login program and indentation

#concept
#email -> (dineshbhatt0707@gamail.com)
#password -> (12345)


email = input('enter email')
password = input('enter password')

if email == 'dineshbhatt0707@gmail.com' and password == '12345':

    print('welcome')
elif email == 'dineshbhatt0707@gmail.com' and password != '12345':

    print('incorrect password')

    password = input('enter password again')

    if password=='1234':
        print('welcome , finally')


    else:
        print('beta tumse na ho payaga')
else:
    print('not correct')


