def desafio():
    arrDesafio = []
    with open("input.txt", "r") as file:
        for line in file:
            stripped_line = (line.strip())
            arrDesafio += [stripped_line]

    print ('Nr. of Trees:', tree_search_part1(arrDesafio))
    print ('Result Part Two:', tree_search_part2(arrDesafio, 1, 1) * tree_search_part2(arrDesafio, 3, 1) * 
    tree_search_part2(arrDesafio, 5, 1) * tree_search_part2(arrDesafio, 7, 1) * tree_search_part2(arrDesafio, 1, 2))

    # alternativa 
    # tuples = [(1,1),(3,1), (5,1), (7,1), (1,2)]
    # result = 1
    # for x,y in tuples:
    #     result *= tree_search_part2(arrDesafio, x, y)
            
    # print('# trees:', result)


    # tuples = [(1,1,1),(3,1,1), (5,1,1), (7,1,1), (1,2,3)]
    # for x,y,z in tuples:
    #     print(x,y,z)

def tree_search_part1(arrDesafio):
    trees=0
    aux=0
    lenght=len(arrDesafio[0])

    for i, val in enumerate(arrDesafio):
    #for row in arrDesafio:
        if(aux>=lenght):
          aux=aux%lenght
        #if row[aux]=='#':
        if arrDesafio[i][aux]=='#':
            trees+=1
        aux=aux+3
    return trees


def tree_search_part2(arrDesafio, right, down):
    trees=0
    aux=0
    lenght=len(arrDesafio[0])

    #for i in range(0, len(arrDesafio), down):
    for i, val in enumerate(arrDesafio):
        if(aux>=lenght):
            aux=aux%lenght
        if (i*down)>=len(arrDesafio):
            return trees
        if arrDesafio[i*down][aux]=='#':
            trees+=1
        aux=aux+right
    return trees


    
if __name__ == "__main__":
    desafio()
