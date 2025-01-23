from roman_number import to_arabic_number
from roman_number import to_roman_numeral
import pytest

@pytest.mark.parametrize("rom, result", [('I',1), ('MMVIII',2008), ('IV',4), ('XC',90), ('MMMCMXCIX',3999)])
def test_to_arabic_number(rom,result):
   assert to_arabic_number(rom) == result

@pytest.mark.parametrize("num, result", [(1,'I'), (2008,'MMVIII'), (4,'IV'), (90,'XC'), (3999,'MMMCMXCIX')]) 
def test_to_roman_numeral(num, result):
    assert to_roman_numeral(num) == result


