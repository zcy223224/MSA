import csv
from math import exp, sqrt
from random import randint
import random
import numpy as np
from module.functions_mod import F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell, overlimit

'''结果文件'''
filerow=[]
'''种族个体数'''
maxnumber=100
'''维度'''
dimension=30
'''发现者比例'''
ratep=0.2
'''警戒者比例'''
ratea=0.1
'''安全阈值和危险值'''
ST=0.8
R2=0
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
        '''初始化种群'''
        '''均匀分布:list(((np.random.rand(dimension)*2-1)*idomain))'''
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
        iteration=500
        n=0
        before=[]
        while(n<iteration):
            '''发现者更新中'''
            i=0
            while(i<int(maxnumber*ratep)):
                before=[]
                for var in specie[i]:
                    before.append(var)
                j=0
                R2=np.random.rand()
                if(R2<ST):
                    while(j<dimension):           
                        specie[i][j]*=exp((-1)*i/(iteration*0.5))
                        specie[i][j]=overlimit(domain,specie[i][j])
                        j+=1
                else:
                    while(j<dimension):           
                        specie[i][j]+=np.random.randn()
                        specie[i][j]=overlimit(domain,specie[i][j])
                        j+=1
                specie[i][dimension]=functions[functionorder](specie[i])
                if(float(before[dimension])<float(specie[i][dimension])):
                    specie[i]=before
                i+=1

            specie.sort(key=fitness)

            '''跟随者更新中'''
            while(i<maxnumber):
                before=[]
                for var in specie[i]:
                    before.append(var)
                j=0
                if(i>(maxnumber/2)):
                    while(j<dimension):
                        specie[i][j]=exp((specie[maxnumber-1][j]-specie[i][j])/(i*i))*np.random.randn()
                        specie[i][j]=overlimit(domain,specie[i][j])
                        j+=1
                else:
                    while(j<dimension):
                        k=0
                        temp0=0
                        while(k<dimension):
                            temp0+=OOZ()*(specie[i][k]-specie[0][k])
                            k+=1
                        specie[i][j]=specie[0][j]+temp0/dimension
                        specie[i][j]=overlimit(domain,specie[i][j])
                        j+=1
                specie[i][dimension]=functions[functionorder](specie[i])
                if(float(before[dimension])<float(specie[i][dimension])):
                    specie[i]=before
                i+=1

            specie.sort(key=fitness)

            '''警戒者更新中'''
            for i in range(randint(0,5), maxnumber, int(1.0/ratea)):
                before=[]
                for var in specie[i]:
                    before.append(var)
                j=0
                if(specie[i][dimension]!=specie[0][dimension]):
                    while(j<dimension):
                        specie[i][j]=specie[0][j]+(specie[0][j]-specie[i][j])*np.random.randn()
                        specie[i][j]=overlimit(domain,specie[i][j])
                        j+=1
                else:
                    while(j<dimension):
                        specie[i][j]+=random.uniform(-1, 1)*(specie[i][j]-specie[maxnumber-1][j])/(specie[i][dimension]-specie[maxnumber-1][dimension]+0.00000001)
                        specie[i][j]=overlimit(domain,specie[i][j])
                        j+=1
                specie[i][dimension]=functions[functionorder](specie[i])
                if(float(before[dimension])<float(specie[i][dimension])):
                    specie[i]=before

            n+=1
            specie.sort(key=fitness)

        '''第numOfExp次实验结束，更新最优值'''
        numOfExp+=1
        fitnessvalue.append(specie[0][dimension])
        print('第{}次计算完成,最优值为:{}'.format(numOfExp,specie[0][dimension]))
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

with open('result_origin.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for r in filerow:
        writer.writerow(r)