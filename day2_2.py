f = open("input2.txt","r")
numbers = f.read().split(",")
integers = [int(number) for number in numbers]
savedints = integers[:]

j = 0 
while j < 100:
    k = 0
    while k < 100:
        # print j,k
        integers = savedints[:]
        # replace position 1 with value 12 
        integers[1] = k
        #replace position 2 w value 2
        integers[2] = j 

        # print(integers)

        i = 0 
        # print k,j
        while True:
            if integers[i] == 1:
                val1 = integers[i + 1]
                val2 = integers[i + 2]
                change = integers[i + 3]
                if change >= 161:
                    break
                if val1 >= 161:
                    break
                if val2 >= 161:
                    break
                integers[ change ] = integers[val1] + integers[ val2 ]
            elif integers[i] == 2:
                val1 = integers[i + 1]
                val2 = integers[i + 2]
                change = integers[i + 3]
                if change >= 161:
                    break
                if val1 >= 161:
                    break
                if val2 >= 161:
                    break
                integers[ change ] = integers[val1] * integers[ val2 ]
            elif integers[i] == 99:
                break
            i += 4
            # print integers
        # print integers[0]
        if integers[0] == 19690720:
        # if integers[0] == 19690622:
            print 100 * k + j 
        k += 1
    j += 1

