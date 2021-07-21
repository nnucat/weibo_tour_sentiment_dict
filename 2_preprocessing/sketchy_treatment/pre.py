from re import sub, compile, UNICODE, IGNORECASE


def clean_text(text):
    zh_puncts1 = "，；、。！？（）《》【】"  # 清除符号
    URL_REGEX = compile(
        r'(?i)((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>' + zh_puncts1 + ']+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:\'".,<>?«»“”‘’' + zh_puncts1 + ']))',
        IGNORECASE)
    text = sub(URL_REGEX, "", text)

    EMAIL_REGEX = compile(r"[-a-z0-9_.]+@(?:[-a-z0-9]+\.)+[a-z]{2,6}", IGNORECASE)
    text = sub(EMAIL_REGEX, "", text)
    text = sub(r"(回复)?(//)?\s*@\S*?\s*(:|：| |$)", " ", text)  # 去除正文中的@和回复/转发中的用户名
    lb, rb = 1, 6
    text = sub(r"\[\S{" + str(lb) + r"," + str(rb) + r"}?\]", "", text)
    emoji_pattern = compile("["u"\U0001F600-\U0001F64F"
                            u"\U0001F300-\U0001F5FF"
                            u"\U0001F680-\U0001F6FF"
                            u"\U0001F1E0-\U0001F1FF"
                            u"\U00002702-\U000027B0" "]+", flags=UNICODE)
    text = emoji_pattern.sub(r'', text)
    text = sub(r"#\S+#", "", text)
    pic_num = compile(r"[p]+[0-9]", IGNORECASE)
    text = sub(pic_num, "", text)
    text = sub(r"L\S+的微博视频", " ", text)
    '''
    text = text.replace("\n", " ")
    '''
    text = sub(r"(\s)+", r"\1", text)
    stop_terms = ['展开', '全文', '展开全文', '一个', '网页', '链接', '?【', 'ue627', 'c【', '10', '一下', '一直', 'u3000', '24', '12',
                  '30', '?我', '15', '11', '17', '?\\', '显示地图', '原图', '☀', '丨', '抽奖详情', '→']
    for x in stop_terms:
        text = text.replace(x, "")
    allpuncs = compile(
        r"[，\_《。》、？；：‘’＂“”【「】」·！@￥…（）—\,\<\.\>\/\?\;\:\'\"\[\]\{\}\~\`\!\@\#\$\%\^\&\*\(\)\-\=\+]")
    text = sub(allpuncs, "", text)

    return text.strip()


path1 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/txt/美龄宫.txt'
path2 = 'D:/nnu/大创/weibo_tour_sentiment_dict/2_PreProcessing/data/南京/txt/美龄宫输出.txt'
f = open(path1, 'r', encoding='utf-8', errors='ignore')
fw = open(path2, 'w', encoding='utf-8', errors='ignore')
data = f.read()
fw.write(clean_text(data))
'''
for line in f:
    constr = ''
    for uchar in line:
        clean_text(uchar)
        if uchar != ' ':
            constr += uchar
    fw.write(constr + '\n')
'''
