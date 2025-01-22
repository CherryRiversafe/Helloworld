from roman_number import to_arabic_number
from roman_number import to_roman_numeral

#def test_to_arabic_number(rom,result):
 #   assert to_arabic_number(rom) == result
@pytest.fixture
def num():
    num = 
def test_to_roman_numeral(num, result):
    assert to_roman_numeral(num) == result

to_test = {1:'I', 2008:'MMVIII', 4:'IV', 90:'XC', 3999:'MMMCMXCIX'}
for item in to_test.keys():
    print(item, to_test[item])
    test_to_roman_numeral(item, to_test[item])

'''
to_test2 = {'I':1, 'MMVIII':2008, 'IV':4, 'XC':90, 'MMMCMXCIX':3999}
for item in to_test2.keys():
    rom = item
    result = to_test2[rom]
    test_to_arabic_number(rom, result)
'''