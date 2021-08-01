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



print("\nsentiment dictionary using default seed words")
docs = ["张市筹设兴华实业公司外区资本家踊跃投资晋察冀边区兴华实业公司，自筹备成立以来，解放区内外企业界人士及一般商民，均踊跃认股投资",
        "打倒万恶的资本家",
        "该公司原定资本总额为二十五万万元，现已由各界分认达二十万万元，所属各厂、各公司亦募得股金一万万余元",
        "连日来解放区以外各工商人士，投函向该公司询问经营性质与范围以及股东权限等问题者甚多，络绎抵此的许多资本家，于参观该公司所属各厂经营状况后，对民主政府扶助与奖励私营企业发展的政策，均极表赞同，有些资本家因款项未能即刻汇来，多向筹备处预认投资的额数。由平津来张的林明棋先生，一次即以现款入股六十余万元"
        ]
# scale: 将所有词语的情感值范围调整到[-1,1]
# 省略pos_seeds, neg_seeds,将采用默认的情感词典 get_qh_sent_dict()

print("scale=\"+-1\", 在正负区间内分别伸缩，保留0作为中性的语义")
sent_dict = ht.build_sent_dict(docs, min_times=1, scale="+-1")
print("%s:%f" % ("赞同", sent_dict["赞同"]))
print("%s:%f" % ("二十万", sent_dict["二十万"]))
print("%s:%f" % ("万恶", sent_dict["万恶"]))
print("%f:%s" % (ht.analyse_sent(docs[0]), docs[0]))
print("%f:%s" % (ht.analyse_sent(docs[3]), docs[3]))
