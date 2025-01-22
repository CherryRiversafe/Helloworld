from flask import Flask, render_template, url_for, request, json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ator')
def arabic_to_roman():
    x = int(request.args.get('arab'))
    rom_num =  {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV' ,1:'I' }
    roman_numeral = ''
    for key in rom_num.keys():
        while x >= key:
            roman_numeral += rom_num[key]
            x -= key
    print(roman_numeral)
    return{'roman_numeral': roman_numeral}


    

@app.route('/rtoa')
def roman_to_arabic():
    y = request.args.get('rom')
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
    return {'Arabic_number': j}
    

if __name__ == "__main__":
    app.run(debug = True)