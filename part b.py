all_numbers = [0,1,2,3,4,5,6,7,8,9]
def find_power(no, a_list): 
    finished = False
    count = 0
    number = int(no)
    power = 1
    temp = number ** power
    while(not finished): #not finished = True to run
        for i in a_list:
            if str(i) in str(temp) and count == 9:
                finished = True
                return power 

            elif str(i) in str(temp) and count != 9:
                count += 1
            
            elif str(i) not in str(temp):
                power += 1
                temp = number**power
                count = 0 
                continue
            
def minus_list(small_list): #for j--
    big_list = [0,1,2,3,4,5,6,7,8,9]
    for element in small_list:
        if element in big_list:
            big_list.remove(element)
    return big_list

x = int(input("first number: "))
y = int(input("second number: "))

test_one = find_power(x, all_numbers)
test_two = find_power(y, all_numbers)

list_of_shit = []

for power_of_x in range(test_one-1, -1, -1): #from test_one -1 to 0
    total = 0
    new_x = x**power_of_x
    list_x = [int(number) for number in str(new_x)]
    second_list = minus_list(list_x)
    second_power = find_power(y, list_x)
    total = test_one + second_power
    list_of_shit.append(total)

print(list_of_shit)
print(find_power(x, all_numbers))
print(find_power(y, all_numbers))





