print()
print('WElCOME! Here I will help you to find a if a number is an armstrong for power 3 :)')
print()
print('And if not then I will tell you the next armstrong number of the entered value')
print()
n = int(input('Enter the number to you want to find te next armstrong of: '))
num = n
print()
print('Calculating... Please wait!!!')
print()

a_lst = []
x = str(n)
for i in range(len(x)):
    a = int(x[i])
    a_lst.append(a)
total_cube = 0
for i in a_lst:
    i_cube = i ** 3
    total_cube += i_cube
    
    if total_cube == n:
        if num == n:
            print('The given number {} is itself an armstrong number for the power 3.'.format(n))

        else:
            print('The next armstrong number of {} is {} for power 3'.format(num, n))
else:
    n += 1
