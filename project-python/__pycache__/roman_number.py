

def to_roman_numeral(x:int)->str:
    rom_num =  {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV' ,1:'I' }
    roman_numeral = ''
    for key in rom_num.keys():
        while x >= key:
            roman_numeral += rom_num[key]
            x -= key
    return roman_numeral


def to_arabic_number(y:str)->int:
    arb_num = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    num_list = list(y)
    i = 1
    j = 0
    while i < len(num_list):
        current_char = arb_num[num_list[(i-1)]]
        next_char = arb_num[num_list[i]]

        if current_char >= next_char:
            j += arb_num[num_list[(i-1)]]   
        else:
            j -= arb_num[num_list[(i-1)]] 
        i += 1
    j += arb_num[num_list[(len(num_list)-1)]]
    print(j)  
    return j

to_roman_numeral(3999)
#to_arabic_number('CXLII')
