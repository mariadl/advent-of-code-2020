from functools import reduce
import re 

min_campos = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

def desafio():
    pass_list = []
    nr_validos = 0
    
    with open("input.txt", "r") as file:
        pass_list = file.read().split('\n\n')

    for passaporte in pass_list:
        passaporte_temp=passaporte.split('\n')

        #print('antes', passaporte_temp)
        if len(passaporte_temp) > 1:
            passaporte = reduce(lambda a,b: a+' '+b,  passaporte_temp)
        #print('depois', passaporte)
            
        passaporte_campos = {}

        pares = passaporte.split(' ')
        for par in pares:
            [key,val] = par.split(':') 
            passaporte_campos[key] = val

        if validate(passaporte_campos):
            nr_validos += 1

        



    print ('Passaportes Validos:', nr_validos)



   
def validate(passp):
    campos=set(passp.keys())
    x = min_campos-campos
    if len(x) > 0:
        return False
    by = int(passp['byr'])
    if by < 1920 or by > 2020:
        return False
    iy = int(passp['iyr'])
    if iy < 2010 or iy > 2020:
        return False
    ey = int(passp['eyr'])
    if ey < 2020 or ey > 2030:
        return False

    hgt = passp['hgt']
    p = re.compile(r"^(1[5-8]\d|19[0-3])cm|(59|6\d|7[0-6])in$")
    m = p.match(hgt)
    if not m:
        return False

    hcl = passp['hcl'] 
    p = re.compile(r"^#[a-f0-9]{6}$")
    m = p.match(hcl)
    if not m:
        return False

    ecl = passp['ecl']
    p = re.compile(r"^(amb|blu|brn|gry|grn|hzl|oth)$")
    m = p.match(ecl)
    print ('ecl', ecl)
    if not m:
        print('false')
        return False

    pid = passp['pid'].strip()
    p = re.compile(r"^[0-9]{9}$")
    m = p.match(pid)
    if not m:
        return False


    return True



    
if __name__ == "__main__":
    desafio()
