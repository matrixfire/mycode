import jieba
'''
jieba.lcut(s) # 精确模式，返回一个列表类型的分词结果
jieba.lcut(s, cut_all=True) # 全模式
jieba.lcut_for_search(s) # 搜索引擎模式
jieba.add_word(w) # 向分词词典增加新词
'''

excluded_symbols = '!"#$%&()*+,-./:;<=>?@[\\]^_‘{|}~'
excluded_words = ['the'] 

path = r"test.txt"

def get_text_en(path):
	with open(path) as f_obj:
		txt = f_obj.read().lower()
	for es in excluded_symbols:
		txt = txt.replace(es, " ")
	for num in range(10):
		txt = txt.replace(str(num), ' ')
	for word in excluded_words:
		txt = txt.replace(word,' ')
	return txt	

def get_word_freq(path):
	word_dict = {}
	txt = get_text_en(path)
	word_list = txt.split()
	for word in word_list:
		if len(word) > 2:
			word_dict[word] = word_dict.get(word, 0) + 1
	final_list = list(word_dict.items())
	final_list.sort(key=lambda x: x[1], reverse=True)		

	return final_list

# for i in get_word_freq(path):

# 	print(i)		
items = get_word_freq(path)

for i in range(min(10, len(items))):
	word, count = items[i]
	print("{0:<10}{1:>5}".format(word, count))


def get_chinese(path):
	txt = open(path, encoding="utf-8").read()
	words = jieba.lcut(txt)
	counts = {}
	for word in words:
		if len(word) == 1:
			continue
		elif word == "小猫" or word == "小狗":
			rword == "宠物" 	 
		else:
			rword = word
		counts[rword] = counts.get(rword, 0) + 1

	for word in excludes:
		del counts[word]
	items = list(counts.items())
	items.sort(key=lambda x:x[1], reverse=True)
	return items

