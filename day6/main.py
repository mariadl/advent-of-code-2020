from functools import reduce
import re 


def return_multiply(obj):
    return obj['multiply']

def desafio():
    answer_list = []
    group_sum=0
    group_sum_pt_2=0

    with open("input.txt", "r") as file:
        answer_list = file.read().split('\n\n')
        
    #part 1
    for a in answer_list:
        print(a)
        ind_answers = a.split('\n')
        #print (ind_answers)
        group_set = set()
        for answer in ind_answers:
            for question_letter in answer:
                group_set.add(question_letter)

        set1 = set([c for c in ind_answers[0]])
        for answer in ind_answers:
            set1=set1.intersection(set([c for c in answer])) 

        group_sum += len(group_set)
        group_sum_pt_2 += len (set1)

    print (group_sum)
    print (group_sum_pt_2)
   


#def find_missing(lst): 
 #   start = lst[0] 
  #  end = lst[-1] 
   # return sorted(set(range(start, end + 1)).difference(lst)) 
    
if __name__ == "__main__":
    desafio()
