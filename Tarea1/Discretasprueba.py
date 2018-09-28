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
    v=True
    f=False
    if len(formula)==0:
        print(v)
        return v
    if len(formula)>1 and formula[0][0]==-formula[1][0]:
        if len(formula[0])==1 and len(formula[1])==1:
            print(f)
            return f
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




print(BuildModel([[-2, 4], [1], [-4,-1]]))