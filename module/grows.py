from module.functions_mod import F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell
functions=[F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12,Ackley,Perm,Trid,Zakharov,Powell]
idomainlist=[100,10,100,100,30,100,1.28,500,5.12,32,600,50,32,30,900,10,5]

def lowbest(functionorder,dimension):
    num=20   
    idomain=idomainlist[functionorder]
    result=[]
    for var in range(dimension+1):
        result.append(0)
    dorder=0
    result[dimension]=functions[functionorder](result)
    while(dorder<dimension):
        down=-idomain
        step=2*idomain/num
        best=0
        for time in range(5):       
            for i in range(num-1):
                tempd=result[dorder]
                result[dorder]=down+step*(i+1)
                tempr=functions[functionorder](result)
                if(result[dimension]>tempr):
                    best=down+step*(i+1)
                    result[dimension]=tempr
                else:
                    result[dorder]=tempd
            down=best-step          
            step=2*step/num
        result[dorder]=best
        dorder+=1

    return result

