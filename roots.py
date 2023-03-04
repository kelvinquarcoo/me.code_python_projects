a = int(input('enter the value for a'))
b = int(input('enter the value for b'))
c = int(input('enter the value for c'))
disc = float((b*b)-(4*a*c))
if disc == 0:
    root1 = root2 = b/(2*a)
    print(f'the roots are real and equal and are {root1}')
elif disc > 0:
    root1 = (-b + (disc**1/2)) / (2 * a)
    root2 = (-b - (disc**1/2)) / (2 * a)
    print(f'roots are unequal and are {root1} and {root2}')
else:
    print('roots are imaginary')