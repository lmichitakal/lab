import numpy as np
import dill
from collections import *




def forward_nn(network, phi_zero):
    phi_all = [phi_zero]
    for i in range(len(network)):
        w, b = network[i]
        #前の層の値に基づいて値を計算
        phi_all.append(np.tanh(np.dot(w, phi[i]) + b))
    return phi_all

def backward_nn(network, phi, y):
    J = len(network)
    delta = np.array([0] for _ in range(len(J)) + np.array(y - phi_all[J]))
    d_delta = [0 for _ in range(len(J))]
    for i in range(reversed(j)):
        d_delta[i+1] = delta[i+1] * (1- (phi_all[i+1])**2)
        w, b = network[i]
        delta[i] = np.dot(d_delta[i+1], w)

    return d_delta

def update_weights(network, phi, d_delta, Lamda):
    for i in range(len(network)):
        w, b = network[i]
        w += Lamda * np.outer(d_delta[i+1], phi_all[i])
        b += Lamda * d_delta[i+1]
    return 0

def init_net(ids):
    net = []
    w_0 = (np.random.rand(len(ids)) – 0.5)
    b_0 = (np.random.rand(len(ids)) – 0.5)
def create_features(sen, ids):
    phi = defaultdict(int)
    words = sen.split()
    for word in words:
        phi[ids['UNI:{word}']] += 1
    return phi

def learn_nn():
    ids = defaultdict(lambda: len(ids))
    feat_lab = []
    # 素性を作り、ネットワークをランダムな値で初期化
    with open(train_data) as f:
            for line in f:
                #print(line.strip().split('\t'))
                y, sen = line.strip().split('\t')
                y = int(y)
                for word in sen.split(' '):
                    ids[f'UNI:{word}']
                feat_lab.append((create_features(sen), y))
    network = init_net(ids)      


