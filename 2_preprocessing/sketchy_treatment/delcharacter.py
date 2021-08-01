path1 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/美龄宫积极词带权值.txt'
path2 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/美龄宫积极词.txt'
f = open(path1, 'r', encoding='utf-8', errors='ignore')
fw = open(path2, 'w', encoding='utf-8', errors='ignore')

for line in f:
    constr = ''
    for uchar in line:
        if u'\u4e00' <= uchar <= u'\u9fa5':
            if uchar != ' ':
                constr += uchar
    fw.write(constr + '\n')