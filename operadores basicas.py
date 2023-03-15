                # Operaciones Basicas 
 123 + 222
#  345

1.5 * 4
#6.0

2 ** 100
# 1267650600228229401496703205376

len(893)
# TypeError: object of type 'int' has no len()

len("893")
# 3
len([2, 3, 4, 5])
# 4

len(str(2 ** 1000000))
# ValueError: Exceeds the limit (4300) for integer string conversion; use sys.set_int_max_str_digits() to increase the limi

import math
#
Math.pi
# NameError: name 'Math' is not defined

random.random()
#NameError: name 'random' is not defined

random.choice([1, 2, 3, 4])
#NameError: name 'random' is not defined

st = 'Spam'
#Spam

len(st[-1]
#'m'
    
st[1:3]
#'pa
    
st[1:]
#'pam'
    
st[:]
#'Spam'
    
st + "Hola"
# 'SpamHola'
    
st * 5
#  'SpamSpamSpamSpamSpam'
    
st[0] = 'z'
# NameError: name 'st' is not defined
    
st = 'z' + st[1:]
#KeyboardInterrupt
    
print(st)
#NameError: name 'st' is not defined
    
           # Transformar string a lista:
    
S = 'shrubbery'
# SyntaxError: unmatched '}'
    
L = list(S)
#NameError: name 'S' is not defined
 L
#NameError: name 'L' is not defined
    
 L[1] = 'c'
#NameError: name 'L' is not defined
    
''.join(L)
# NameError: name 'L' is not defined
    
B = bytearray(b'spam')
 #bytearray(b'spam')
    
B.extend(b'eggs')
#bytearray(b'spameggs')
    
B
#bytearray(b'spameggs')
    
B.decode()
# NameError: name 'B' is not defined
  # Métodos especiales para strings:
S = 'Spam'
    
S.find('pa')
    
S.find('pa')
# 1
    
S
# 'Spam'
    
S.replace('pa', 'XYZ')
# 'SXYZm'

S
'Spam'
    
line = 'aaa,bbb,ccccc,dd'
    
line.split(',')
# ['aaa', 'bbb', 'ccccc', 'dd']
    

    
S.upper()
# 'SPAM'
    
S.isalpha() # Content tests: isalpha, isdigit, etc.
# True
    
line = 'aaa,bbb,ccccc,dd\n'
#   'aaa,bbb,ccccc,dd\n'
    
line.rstrip()
# 'aaa,bbb,ccccc,dd'
    
line.rstrip().split(',')
# ['aaa', 'bbb', 'ccccc', 'dd']
    
      # Plantillas para strings:
'%s, eggs, and %s' % ('spam', 'SPAM!')
# 'spam, eggs, and SPAM!'
    
'{0}, eggs, and {1}'.format('spam', 'SPAM!')'{0}, eggs, and {1}'.format('spam', 'SPAM!')
#     #SyntaxError: invalid syntax
    
'{}, eggs, and {}'.format('spam', 'SPAM!')
# 'spam, eggs, and SPAM!'
    
f'{S}, eggs, and {line}'
# 'spam, eggs, and aaa,bbb,ccccc,dd\n'
    
}

#Visualizar los métodos de un objecto:
dir(S) # S es un string
#IndentationError: unexpected indent

help(S.replace)
#IndentationError: unexpected indent

S = 'A\nB\tC'
#IndentationError: unexpected indent

len(S)
# IndentationError: unexpected indent

ord('\n')
#IndentationError: unexpected indent

S = 'A\0B\0C'

