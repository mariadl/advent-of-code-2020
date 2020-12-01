def jose(arg1='antonio', arg2='maria'):

    # args
    print(arg1)
    print(arg2)

    # print
    print('ola')

    # boleans
    maria = True
    antonio = False

    # arrays
    arr = ['a','b','c','d','e']
    arr2 = ['f','g','h','i','j']
    arr3 = [arr,arr2]
    
    # for loops
    # for val in arr3:
    #     print(val)

    # for loops enumados
    # for (key, val) in enumerate(arr):
    #     print('key', key, ' - val', val)

    # for x in enumerate(arr):
    #     print('key', x)

    n = 100
    arr = []
    for i in range(0,n):
        arr.append(i)
    print(arr)
    
    arr = [i*50 for i in range(0,100)]
    print(arr)

    
def desafio():
    arrDesafio = []
    with open("input1to.txt", "r") as file:
        for line in file:
            stripped_line = int(line.strip())
            arrDesafio.append(stripped_line)

            # alternative
            # arrDesafio += [stripped_line]
    
    print('length', len(arrDesafio))


    for i, val1 in enumerate(arrDesafio):
        for i2, val2 in enumerate(arrDesafio[i:]):
            for val3 in arrDesafio[i2:]:
                soma=val1 + val2 + val3
                #print('soma:', soma)
                if soma==2020:
                    print('valores:', val1, val2, val3)
                    print('multiply', val1*val2*val3)
                    break
        
    
    


    
if __name__ == "__main__":
    desafio()


