def SetLiteral(formula,lit):
    newlit=[]
    for i in formula:
        litlit=[]
        for j in i:
            if j==lit:
                litlit=[]
                break
            if j==-lit:
                continue
            litlit.append(j)
        if len(litlit)!=0:
            newlit.append(litlit)
    return newlit


def IsSatisfiable(formula):
    if len(formula)==0:
        return True
    if len(formula)>1:
        c=0
        for i in formula:
            if len(i)==1 and c==0:
                c=i[0]
            if len(i)==1 and i[0]==-c:
                return False
    lit=formula[0][0]
    for i in formula:
        if len(i)==1:
            lit=i[0]
            break
    return IsSatisfiable(SetLiteral(formula,lit))
    return IsSatisfiable(SetLiteral(formula,-lit))

def BuildModel(formula):
    if not IsSatisfiable(formula):
        return (False ,{})
    else:
        literales=[]
        while len(formula)>=1:
            lit=formula[0][0]
            if IsSatisfiable(SetLiteral(formula, lit)):
                literales.append([lit,True])
                formula = SetLiteral(formula, lit)
            else:
                literales.append([-lit,True])
                formula = SetLiteral(formula, -lit)
        for i in literales:
            if i[0]<0:
                i[0]=-i[0]
                i[1]=not i[1]
        return (True,literales)




print(BuildModel([[1],[2],[-3]]))
