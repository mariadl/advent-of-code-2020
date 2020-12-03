def desafio():
    arrDesafio = []
    with open("input.txt", "r") as file:
        cnt_part_one=0
        cnt_part_two=0
        for line in file:
            split1 = line.split('-')
            min_val = int (split1[0])
            split2 = split1[1].split(' ')
            max_val = int (split2[0])
            split3 = split2[1].split(':')
            letter = split3[0]
            password = split2[2].strip('\n')

            # obj = {
            #     'letter': letter,
            #     'password': password,
            #     'min_val': min_val,
            #     'max_val': max_val 
            # }
            # obj = (letter, password, min_val, max_val)

            # arrDesafio += [obj]
            
            if (pass_check_part_one (min_val, max_val, letter, password)):
                cnt_part_one+=1

            if (pass_check_part_two (min_val, max_val, letter, password)):
                cnt_part_two+=1

            
    # cnt_part_one = 0 
    # for (letter, password, min_val, max_val) in arrDesafio:
    #     occurrences = password.count(letter)
    #     if occurrences<=max_val and occurrences>=min_val:
    #         cnt_part_one += 1


    #result1 = sum([ pass_check_part_one(min_val, max_val, letter, password) for (letter, password, min_val, max_val) in arrDesafio])
    #result2= sum([ pass_check_part_two(min_val, max_val, letter, password) for (letter, password, min_val, max_val) in arrDesafio])

    print('Number of Correct Passwords in Part One:', cnt_part_one)
    print('Number of Correct Passwords in Part Two:', cnt_part_two)


def pass_check_part_one(min_val, max_val, letter, password): 
    occurrences=password.count(letter)
    return occurrences<=max_val and occurrences>=min_val



def pass_check_part_two(pos_one, pos_two, letter, password):
    count_oc=0
    if password[pos_one-1] == letter:
        count_oc+=1
    if password[pos_two-1] == letter:
        count_oc+=1
    if count_oc != 1:
        return False
    else:
        return True


    
if __name__ == "__main__":
    desafio()
