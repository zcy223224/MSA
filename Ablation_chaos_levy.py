import csv
from math import exp, sqrt
from random import randint
import numpy as np
from module.chaotic import PWLCM
from module.functions import F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell, overlimit
from module.levy import fly

'''结果文件'''
filerow=[]
'''种族个体数'''
maxnumber=100
'''维度'''
dimension=30
'''发现者比例'''
ratep=0.1
'''loser者比例'''
ratea=0.1
'''函数名列表，各函数最大边界和初始边界'''
functions=[F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell]
domainlist=[100,10,100,100,30,100,1.28,500,5.12,32,600,50,32,30,900,10,5]

def fitness(elem):
    return elem[dimension]

def OOZ():
    if(randint(0,1)):
        return 1
    else:
        return -1

functionorder=0
wholefunc=17
while(functionorder<wholefunc):
    '''最大边界与初始边界'''
    domain=domainlist[functionorder]

    print('现在测试的函数是:{}'.format(functions[functionorder].__name__))
    '''第iter_table次实验，共15次'''
    iter_table=0
    iter_tablemax=15
    fitnessvalue=[]
    while(iter_table<iter_tablemax):
        '''第iter_table次实验'''

        '''整个种族'''
        specie=[]
        '''个体'''
        Individual=[]
        '''初始化种群'''
        '''混沌映射:PWLCM(start,dimension,idomain)'''
        '''反向学习策略:生成初始混沌映射的反向解，二者混合取最优'''
        counter=0
        while(counter<maxnumber):
            start=int(np.random.rand()*10000)+500
            Individual=PWLCM(start,dimension,domain)
            Reverse=[]
            for var in Individual:
                if(var>0):
                    Reverse.append(domain-var)
                else:
                    Reverse.append(-domain-var)
            Reverse.append(0)
            Reverse[dimension]=functions[functionorder](Reverse)
            Individual.append(0)
            Individual[dimension]=functions[functionorder](Individual)
            specie.append(Individual)
            specie.append(Reverse)
            counter+=1
        specie.sort(key=fitness)
        for var in range(maxnumber):
            specie.remove(specie[maxnumber])


        '''算法,开始迭代'''       
        '''最大迭代次数'''
        iteration=500
        n=0
        before=[]
        while(n<iteration):
            '''发现者更新中'''
            i=0
            while(i<int(maxnumber*ratep)):
                j=0
                while(j<dimension):
                    beforevalueofij=specie[i][j]
                    beforevalueoffitness=specie[i][dimension]       
                    specie[i][j]+=np.random.randn()*domain*0.3*exp(-n*0.03)
                    specie[i][j]=overlimit(domain,specie[i][j])
                    specie[i][dimension]=functions[functionorder](specie[i])
                    if(beforevalueoffitness<specie[i][dimension]):
                        specie[i][j]=beforevalueofij
                        specie[i][dimension]=beforevalueoffitness
                    j+=1
                i+=1

            specie.sort(key=fitness)

            '''跟随者更新中'''
            while(i<maxnumber):
                j=0
                while(j<dimension):
                    specie[i][j]+=(specie[0][j]-specie[i][j])*0.1
                    specie[i][j]=overlimit(domain,specie[i][j])
                    j+=1
                specie[i][dimension]=functions[functionorder](specie[i])
                i+=1

            specie.sort(key=fitness)

            '''loser更新中'''
            i=int(maxnumber*(1-ratea))
            while(i<maxnumber):
                before=[]
                for var in specie[i]:
                    before.append(var)
                j=0
                while(j<dimension):
                    specie[i][j]=0
                    j+=1
                for var1 in range(20):
                    vectorofLevy=fly(domain,dimension)                                        
                    j=0
                    while(j<dimension):
                        specie[i][j]+=vectorofLevy[j]
                        specie[i][j]=overlimit(domain,specie[i][j])
                        j+=1
                    specie[i][dimension]=functions[functionorder](specie[i])
                    if(float(before[dimension])<float(specie[i][dimension])):
                        specie[i]=before
                    else:
                        before=[]
                        for var2 in specie[i]:
                            before.append(var2)
                i+=1

            n+=1
            specie.sort(key=fitness)

        '''第iter_table次实验结束，更新最优值'''
        iter_table+=1
        fitnessvalue.append(specie[0][dimension])
        print('第{}次计算完成,最优值为:{}'.format(iter_table,specie[0][dimension]))
        '''
        print(specie[0])
        print("\n\n\n\n")
        '''
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

with open('result_chaos_levy.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for r in filerow:
        writer.writerow(r)