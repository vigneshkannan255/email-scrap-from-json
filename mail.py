import json

ans=set()

f=open('csvjson.json',)
data=json.load(f)
for j in range(len(data)):
	for i in data:
		ans.add(data[j]['email'])
		
print(ans)
print(len(ans))
f.close()

