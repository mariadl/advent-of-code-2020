def desafio():
    arrDesafio = []
    with open("input.txt", "r") as file:
        cnt_part_one=0
        cnt_part_two=0
        cnt_lines=0
        print(file)
        for line in file:
            cnt_lines+=1
            split1 = line.split('-')
            min_val = int (split1[0])
            split2 = split1[1].split(' ')
            max_val = int (split2[0])
            split3 = split2[1].split(':')
            letter = split3[0]
            password = split2[2].strip('\n')
            
            if (pass_check_part_one (min_val, max_val, letter, password)):
                cnt_part_one+=1

            if (pass_check_part_two (min_val, max_val, letter, password)):
                cnt_part_two+=1

            
    print('Input Lines:', cnt_lines)
    print('Number of Correct Passwords in Part One:', cnt_part_one)
    print('Number of Correct Passwords in Part Two:', cnt_part_two)


def pass_check_part_one(min_val, max_val, letter, password): 
    occurrences=password.count(letter)
    if occurrences>max_val:
        return False
    if occurrences<min_val:
        return False
    else:
        return True



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
