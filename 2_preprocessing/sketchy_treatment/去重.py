import shutil

readDir = "D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/消极种子词.txt"  # old 最后一行要补换行符
writeDir = "D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/消极种子词去重.txt"  # new
a = 0
lines_seen = set()
outfile = open(writeDir, "w", encoding='utf-8', errors='ignore')
f = open(readDir, "r", encoding='utf-8', errors='ignore')
for line in f:
    if line not in lines_seen:
        a += 1
        outfile.write(line)
        lines_seen.add(line)
        print(a)
        print('\n')
outfile.close()
print("success")


