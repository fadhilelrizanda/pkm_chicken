import os

with open('chicken/data/chicken/training.txt', 'w') as out:
    for img in [f for f in os.listdir("chicken/data/chicken" + '/train') if f.endswith('jpg')]:
        out.write('chicken/data/chicken/train' + img + '\n')


with open('chicken/data/chicken/valid.txt', 'w') as out:
    for img in [f for f in os.listdir('chicken/data/chicken' + '/valid') if f.endswith('jpg')]:
        out.write('chicken/data/chicken/valid' + img + '\n')
