number = int(input())
power = 1
temp = number ** power #the number that is saved if it is right, start from 2
finished = False

while(not finished): #not finished = True to run
    for i in [1,2,3,4,5,6,7,8,9,0]:
        if str(i) in str(temp) and count == 9:
            finished = True
            print(power)

        elif str(i) in str(temp) and count != 9:
            count += 1
        
        elif str(i) not in str(temp):
            power += 1
            temp = number**power
            print(temp)
            count = 0 
            continue

