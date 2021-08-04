from harvesttext import HarvestText

ht = HarvestText()
"""
import jieba

path_txt = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/txt/秦淮河输出.txt'
txt = open(path_txt, "r", encoding='utf-8', errors='ignore').read()
words = jieba.lcut(txt)
counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(15):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
"""
readDir = "D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/积极种子词去重.txt"  # 种子词
writeDir = "D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/积极词带权值.txt"
outfile = open(writeDir, "w", encoding='utf-8', errors='ignore')
f = open(readDir, "r", encoding='utf-8', errors='ignore')
sents = open('D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/txt/总输出.txt', "r", encoding='utf-8',
             errors='ignore')

processed_texts = []
with open("D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/txt/总输出.txt", encoding="utf-8") as f:
    for line in f:
        if len(line) > 0:
            processed_texts.append(line)
print("\n".join(processed_texts))
inv_index = ht.build_index(processed_texts)

'''
# 使用默认的内置资源建立情感词典，最负面为-1，最正面为+1
senti_dict = ht.build_sent_dict(processed_texts, scale="+-1")
# 假设实体出现的句子的情感都是体现了对其的情感，所有句子的情感的平均值代表了总体好评度
for entity in ht.entity_type_dict:
    entity_appeared_docs = ht.search_entity(entity, processed_texts, inv_index)
    docs_senti = [ht.analyse_sent(doc) for doc in entity_appeared_docs]
    avg_senti = sum(docs_senti) / len(docs_senti)
    print(f"{entity}的好评度为：{avg_senti}")
'''

print("\nsentiment dictionary using default seed words")

# scale: 将所有词语的情感值范围调整到[-1,1]
# 省略pos_seeds, neg_seeds,将采用默认的情感词典 get_qh_sent_dict()

print("scale=\"+-1\", 在正负区间内分别伸缩，保留0作为中性的语义")
sent_dict = ht.build_sent_dict(processed_texts, min_times=5, scale="+-1")
print("%s:%f" % ("美", sent_dict["美"]))

