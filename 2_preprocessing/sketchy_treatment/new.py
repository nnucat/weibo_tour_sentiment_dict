from harvesttext import HarvestText

ht = HarvestText()
path2 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/txt/美龄宫输出.txt'
path3 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/predict/stop_words.txt'
path4 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/txt/美龄宫输出2.txt'
f = open(path2, 'r', encoding='utf-8', errors='ignore')
data = f.read()
f2 = open(path3, 'r', encoding='utf-8', errors='ignore')
stopwords = f2.read()
ht0 = HarvestText()
fw = open(path4, 'w', encoding='utf-8', errors='ignore')
fw.write(str(ht.seg(data, stopwords=stopwords,
                    return_sent=False)))
words = ht.seg(data, stopwords=stopwords,
               return_sent=False)


counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
print(items)

file = open('D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/美龄宫带权值.txt', 'a+', encoding='utf-8')
for i in range(2000):
    file.write(str(items[i]) + '\n')
file.close()
'''
print(ht.seg(data, stopwords=stopwords,
             return_sent=True))  # return_sent=False时，则返回词语列表
'''
