import re

patron = r'^(?!.*211)[012]*(111|122)$'

count = 0

def test (prueba):
    if re.match(patron, prueba):
        return True
    else:
        return False

#Test 1
if(test('1201201020120111')) == True:
    count += 1

#Test 2
if (test('120120120102020122')) == True:
    count += 1

#Test 3
if (test('012012010201122')) == True:
    count += 1

#Test 4
if (test('012012001201201202111111')) == False:
    count += 1

#Test 5
if (test('01201201020120102012')) == False:
    count += 1

#Test 6
if (test('102012021122')) == False:
    count += 1

#Test 7
if (test('1201201020120102020201201020120120111')) == True:
    count += 1

#Test 8
if (test('111111111111111111111111111111111111111111111111111111111122')) == True:
    count += 1

#Test 9
if (test('01202012011010101010101111111102020200222222222221020120120122')) == True:
    count += 1

#Test 10
if (test('01201202011121112222012020120120120221221221112120111')) == False:
    count += 1

#Test 11
if (test('01201201020111')) == True:
    count += 1

#Test 12
if (test('120120120102020122')) == True:
    count += 1

#Test 13
if (test('0122111')) == False:
    count += 1

#Test 14
if (test('2110122')) == False:
    count += 1

#Test 15
if (test('120211122')) == False:
    count += 1

#Test 16
if (test('20120120102111')) == False:
    count += 1

#Test 17
if (test('020120120102012021120210120102122')) == False:
    count += 1

#Test 18
if (test('02012012021101222021012010212201122')) == False:
    count += 1

#Test 19
if (test('0102120210012021021010210120210210210210111')) == True:
    count += 1

#Test 20
if (test('210210210210021021021020210210121201202102102102102102122')) == True:
    count += 1

print(count, 'de 20 pruebas')