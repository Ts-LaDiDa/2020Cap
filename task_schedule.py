import numpy as nmp
# beverage name data field
b1 = 'vodka'
b2 = 'wiskey'
b3 = 'gin'
b4 = 'brandy'
b5 = 'rum'
s1 = 'orange'
s2 = 'strawbeerr'
s3 = 'lemonade'
s4 = 'apple'
s5 = 'coffee'
s6 = 'milk'

storage =[
    [b1,b2,s6,s5],
    [b1,s1,s3,b3],
    [b4,s2,s4,b4],
    [b5,s3,b5,b2]
]
numberOfRobot = 4
numberOfDrink = 5

drinkInd = {}
drinkInd['drink']=[]
drinkInd['drink'].append(
    {
        'drink-id':1,
        'drink-form': [b1,b3,s2,s3,s4]
    }
)
drinkInd['drink'].append(
    {
        'drink-id':2,
        'drink-form': [b1,b2,s1,s3,s3]
    }
)
drinkInd['drink'].append(
    {
        'drink-id':3,
        'drink-form': [b5,s5,s6]
    }
)
drinkInd['drink'].append(
    {
        'drink-id':4,
        'drink-form': [b4,b1,s2,s4]
    }
)
drinkInd['drink'].append(
    {
        'drink-id':5,
        'drink-form': [s5,s6]
    }
)
#print(drinkInd)

record = nmp.zeros(shape=(numberOfDrink,numberOfRobot))
order = [[1,1],[2,1],[4,2],[5,1]]

l = len(drinkInd['drink'])

#for e in drinkInd['drink']:
result = {}
for e in range(l):
    result['d'+str(e)] = drinkInd['drink'][e]

print(result['d0'])