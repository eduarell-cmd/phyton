jose = [10,10,9,10,8];
maria = [10,10,9,8,10];

def mean(numbers):
    return sum(numbers) / len(numbers)
jose=mean(jose)
maria=mean(maria)
print (f'Media de jose: {jose:.1f}')
print (f'Media de maria: {maria:.1f}')