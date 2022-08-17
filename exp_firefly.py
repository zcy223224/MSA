import csv
from math import exp, sqrt
from random import randint
import numpy as np
from module.functions_mod import F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley, Euclid,Perm,Trid,Zakharov,Powell, overlimit

'''结果文件'''
filerow=[]
'''种族个体数'''
maxnumber=100
'''维度'''
dimension=30
'''函数名列表，各函数最大边界和初始边界'''
functions=[F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell]
domainlist=[100,10,100,100,30,100,1.28,500,5.12,32,600,50,32,30,900,10,5]

def fitness(elem):
    return elem[dimension]

functionorder=0
wholefunc=17
while(functionorder<wholefunc):
    '''最大边界与初始边界'''
    domain=domainlist[functionorder]

    print('现在测试的函数是:{}'.format(functions[functionorder].__name__))
    '''第numOfExp次实验，共15次'''
    numOfExp=0
    numOfExpmax=15
    fitnessvalue=[]
    while(numOfExp<numOfExpmax):
        '''第numOfExp次实验'''

        '''整个种族'''
        specie=[]
        '''个体'''
        Individual=[]
        '''萤火虫参数'''
        beta0 = 1;   '''最大吸引力'''
        gamma = 0.5/domainlist[functionorder];  '''光强吸收系数'''
        alpha = 0.2;   '''步长因子'''
        '''初始化种群'''
        counter=0
        while(counter<maxnumber):
            Individual=list(((np.random.rand(dimension)*2-1)*domain))
            Individual.append(0)
            Individual[dimension]=functions[functionorder](Individual)
            specie.append(Individual)
            counter+=1
        specie.sort(key=fitness)


        '''算法,开始迭代'''       
        '''最大迭代次数'''
        iteration=200
        n=0
        while(n<iteration):
            i=1
            while(i<maxnumber):
                before=[]
                for var in specie[i]:
                    before.append(var) 
                j=0 
                while(j<i):
                    '''i向所有前方j靠近'''
                    r2=Euclid(specie[i],specie[j])
                    beta = beta0*exp(-gamma*r2)
                    k=0
                    while(k<dimension):     
                        specie[i][k]+=beta*(specie[j][k]-specie[i][k])+alpha*(np.random.rand()-0.5)
                        specie[i][k]=overlimit(domain,specie[i][k])                       
                        k+=1
                    specie[i][dimension]=functions[functionorder](specie[i])
                    if(before[dimension]<specie[i][dimension]):
                        specie[i]=before
                    else:
                        before=[]
                        for var in specie[i]:
                            before.append(var)                     
                    j+=1               
                i+=1
            before=[]
            for var in specie[0]:
                before.append(var)
            k=0
            while(k<dimension):  
                if(n&2==1):   
                    specie[0][k]*=exp((-1)*i/(iteration*0.5))
                else:
                    specie[0][k]+=np.random.randn()
                k+=1
                specie[i][k]=overlimit(domain,specie[i][k])
            specie[0][dimension]=functions[functionorder](specie[0])
            if(before[dimension]<specie[0][dimension]):
                specie[0]=before
            n+=1
            specie.sort(key=fitness)

        '''第numOfExp次实验结束，更新最优值'''
        numOfExp+=1
        fitnessvalue.append(specie[0][dimension])
        print('第{}次计算完成,最优值为:{}'.format(numOfExp,specie[0][dimension]))
    '''15次实验结束，生成3个值'''
    average=float(sum(fitnessvalue))/len(fitnessvalue)
    total = 0
    for value in fitnessvalue:
        total += (value - average) ** 2
    
    stddev = sqrt(total/len(fitnessvalue))
    fitnessvalue.sort()
    print('最优值:{}    平均值:{}    标准差:{}'.format(fitnessvalue[0],average,stddev))
    filerow.append([functions[functionorder].__name__,'min',fitnessvalue[0]])
    filerow.append(['','ave',average])
    filerow.append(['','std',stddev])
    functionorder+=1
    print("\n\n\n\n")

with open('result_firefly.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for r in filerow:
        writer.writerow(r)