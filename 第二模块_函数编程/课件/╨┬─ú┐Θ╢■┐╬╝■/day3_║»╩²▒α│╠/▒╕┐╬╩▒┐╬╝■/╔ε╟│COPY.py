

import copy


data = {
    "name":"alex",
    "age":18,
    "scores":{
        "语文":130,
        "数学":60,
        "英语":98,
    }
}
d2 = data.copy()

d3 = copy.deepcopy(data)

d3["scores"]["语文"] = 149

print(d3)
print(data)