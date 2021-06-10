from harvesttext import HarvestText

ht = HarvestText()
path2 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/txt/秦淮河输出.txt'
path3 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/predict/stop_words.txt'
path4 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/txt/秦淮河输出2.txt'
f = open(path2, 'r', encoding='utf-8', errors='ignore')
data = f.read()
f2 = open(path3, 'r', encoding='utf-8', errors='ignore')
stopwords = f2.read()
ht0 = HarvestText()
fw = open(path4, 'w', encoding='utf-8', errors='ignore')
fw.write(str(ht.seg(data, stopwords=stopwords,
                    return_sent=False)))
'''
print(ht.seg(data, stopwords=stopwords,
             return_sent=True))  # return_sent=False时，则返回词语列表
'''
