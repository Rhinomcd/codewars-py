import codewars_test as test
from main import VigenereCipher

abc = "abcdefghijklmnopqrstuvwxyz"
key = "password"
c = VigenereCipher(key, abc)

test.assert_equals(c.encode('codewars'), 'rovwsoiv')
test.assert_equals(c.decode('rovwsoiv'), 'codewars')

test.assert_equals(c.encode('waffles'), 'laxxhsj')
test.assert_equals(c.decode('laxxhsj'), 'waffles')

test.assert_equals(c.encode('CODEWARS'), 'CODEWARS')
test.assert_equals(c.decode('CODEWARS'), 'CODEWARS')