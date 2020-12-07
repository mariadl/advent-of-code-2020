import re 


def return_multiply(obj):
    return obj['multiply']

def desafio():
    ticket_list = []
    new_tickets=[]
    
    with open("input.txt", "r") as file:
        ticket_list = file.read().split('\n')

    for ticket in ticket_list:
        t_row=int(ticket[0:7].replace("F", "0").replace("B", "1"),2)
        t_column=int(ticket[7:10].replace("L", "0").replace("R", "1"),2)
        multiply= t_row*8+t_column
        obj = {
                 'row': t_row,
                 'column': t_column,
                 'multiply': multiply
             }
        new_tickets+=[obj]
        print(ticket, '--->', t_row,' + ', t_column, '*', multiply)
   
   
#    seq = [x['multiply'] for x in new_tickets]
#    res = max(seq)
#    print(res)

    print(max(new_tickets, key = lambda obj: obj['multiply'])['multiply'])


    ##Part II
    new_tickets.sort(reverse=False, key = lambda obj: obj['multiply'])
    seq = [x['multiply'] for x in new_tickets]
    print("My seat is:" , find_missing_seat(seq))
    
    
def find_missing_seat(lista): 
    return [x for x in range(lista[0], lista[-1]+1)  
            if x not in lista] 

#def find_missing(lst): 
 #   start = lst[0] 
  #  end = lst[-1] 
   # return sorted(set(range(start, end + 1)).difference(lst)) 
    
if __name__ == "__main__":
    desafio()
