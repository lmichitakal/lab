from collections import *

def load_model(model_file):

    return 0

#素性を色々試す
def create_features(x):
    phi = defaultdict(int)
    words = x.split(' ')

    l = len(words)
    if l < 15:
        phi[f'LEN:{l}'] += 1
    
    for i in range(len(words)-1):
        lis = words[i:i+2]
        phi['BI:' + ' '.join(lis)] += 1
    
    #for word in words:
    #    phi["UNI:" + word] += 1
    
    for word in words:
        phi["UNI:" + word] += 1
        #if word == word.upper():
        #    phi['UPPER:' + word] += 1
        if word == word.lower():
            phi['LOWER:' + word] += 1
    return phi

def predict_one(weight, phi):
    score = 0
    for name, value in phi.items():
        if name in weight: score += value * weight[name]

    if score >= 0:
        return 1
    return -1

def predict_all(w, input_file, out_file):
    with open(input_file) as f, open(out_file, 'w') as out:
        for line in f:
            phi = create_features(line)
            y_pred = predict_one(w, phi)
            out.write(f'{y_pred}\t{line}')



def online_learning(iteration_number, data):
    weights = defaultdict(int)

    for _ in range(iteration_number):
        with open(data) as f:
            for line in f:
                #print(line.strip().split('\t'))
                y, x = line.strip().split('\t')
                y = int(y)
                phi = create_features(x)
                pred_y = predict_one(weights, phi)

                if pred_y != y:
                    update_weights(weights, phi, y)
    return weights

def update_weights(weight, phi, y):
    for name, value in phi.items():
        weight[name] += float(value * y)



def confirm_diff(answer, my_answer, positive_mispredicted_file, negative_mispredicted_file):

    p_cnt = 0
    n_cnt = 0
    n_words = defaultdict(lambda: 0)
    p_words = defaultdict(lambda: 0)

    with open(answer) as labels, open(my_answer) as preds:
        with open(positive_mispredicted_file, 'w') as p_mispred, open(negative_mispredicted_file, 'w') as n_mispred:
            for i, (label, pred) in enumerate(zip(labels, preds)):
                now = label.strip().split('\t')
                y = int(now[0])
                sentence = now[1].split(' ')
                y = int(y)
                pred_y = int(pred.strip().split('\t')[0])
                if pred_y != y:
                    if pred_y == 1:
                        n_cnt += 1
                        for word in sentence:
                            n_words[word] += 1
                        n_mispred.write(f'Number:{i+1} {label}')
                    else:
                        p_cnt += 1
                        for word in sentence:
                            p_words[word] += 1
                        p_mispred.write(f'Number:{i+1} {label}')
            total = p_cnt + n_cnt
            print(f'{p_cnt} + {n_cnt} = {total}')
            n_words = sorted(n_words.items(), key=lambda x: x[1])
            p_words = sorted(p_words.items(), key=lambda x: x[1])
            n_words.reverse()
            p_words.reverse()
            p_mispred.write(f'total mispred:{p_cnt}\n')
            n_mispred.write(f'total mispred:{n_cnt}\n')
            '''
            for k, v in n_words:
                n_mispred.write(f'{k} : {v}\n')
            for k, v in p_words:
                p_mispred.write(f'{k} : {v}\n')
            '''





if __name__ == '__main__':
    path =  '/Users/michitaka/lab/NLP_tutorial/nlptutorial/'

    #テスト
    input = path + 'test/03-train-input.txt'
    answer = path + 'test/03-train-answer.txt'
    #w = online_learning(5, input)
    #print(w)
    #with open('my_weights.txt','w') as f:
    #   for name, value in sorted(w.items()):
    #        f.write(f'{name}\t{value}\n')
        
    #演習
    data = path + 'data/titles-en-train.labeled'
    input = path + 'data/titles-en-test.word'
    answer = path + 'data/titles-en-test.labeled'
    iter_num = 10
    weights = online_learning(iter_num, data)
    predict_all(weights, input, 'my_answer.labeled')
    pred = '/Users/michitaka/lab/NLP_tutorial/tutorial05/my_answer.labeled'
    confirm_diff(answer, pred, 'p_mispred.labeled', 'n_mispred.labeled')

#uni
'''
Accuracy = 92.702798%
'''
#+bi
'''
Accuracy = 93.198725%
'''
#+reversed bi
'''
Accuracy = 93.907191%
'''
#len
'''
Accuracy = 94.048884%
'''
#bi + len + upper,lower
'''
Accuracy = 94.226001%
'''
#uni + bi + len + lower
'''
Accuracy = 94.367694%
'''
#ni + bi + len + lowe (len < 15)
'''
Accuracy = 94.721927%
'''