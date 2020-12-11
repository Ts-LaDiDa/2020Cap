import json

#<json order list>
drinks = dict()
drinks['order']=[]
drinks['order'].append(
    {
        'order-id':1,
        'order-drink': 'white russian',
        'order-num': 5
    }
)
drinks['order'].append(
    {
        'order-id':2,
        'order-drink': 'Bloody Marry',
        'order-num': 1
    }
)
drinks['order'].append(
    {
        'order-id':3,
        'order-drink': 'Strawberry stuff',
        'order-num': 2
    }
)


#</json order list>

#<json object display>
# print(json.dumps(drinks,indent=4))
#</json object display>
f = open('order.json','w')
json.dump(drinks,f)
f.close()

