from knock30 import sentences
#NP 名詞句
consec_N = set()
for sen in sentences:
    cn = []
    for word in sen:
        
        if word['pos'] == '名詞':
            cn.append(word['surface'])
        else:
            if len(cn) >= 2:
                consec_N.add(''.join(cn))
            cn = []
    
if __name__ == '__main__':
    print(consec_N)
    print(len(consec_N))
