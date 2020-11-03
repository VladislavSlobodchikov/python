file = open('file_5_6.txt')

text = file.read().split('\n')
for elem in text:
    buffer = elem.split(':')
    labs = buffer[1].split('-')
    sum =0;
    for item in labs:
           buffer2 = item.split('(')
           print(buffer2[0])