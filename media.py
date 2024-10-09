jose = [9,10,9,10,8];
maria = [10,10,9,8,10];

def mean(numbers):
    return sum(numbers) / len(numbers)
jose=mean(jose)
maria=mean(maria)
if jose>maria:
    print (f'Media de jose: {jose:.1f}')
    print('Maria se la pela a jose')
elif jose==maria:
    print ('Nunguno de los dos vlv')
else:
    print (f'Media de maria: {maria:.1f}')
    print('jose se la pela a Maria')
