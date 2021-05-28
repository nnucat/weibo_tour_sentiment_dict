path1 = 'C:/Users/yan/Desktop/大创/2021-4-18微博数据.txt'
path2 = 'C:/Users/yan/Desktop/大创/path2.txt'
f = open(path1, 'r', encoding='utf-8', errors='ignore')
fw = open(path2, 'w', encoding='utf-8', errors='ignore')

for line in f:
    constr = ''
    for uchar in line:
        if u'\u4e00' <= uchar <= u'\u9fa5':
            if uchar != ' ':
                constr += uchar
    fw.write(constr + '\n')