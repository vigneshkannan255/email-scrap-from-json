'''email sacrap from json'''
#importing json package  
import json
def scrap():
    '''
    this code is used for scrap data from json file
    '''
    ans=set()

    f=open('csvjson.json',)

    #this below line is used for load json file
    data=json.load(f)

    #below code for scrap data from json file
    for j in range(len(data)):
        for i in data:
	    ans.add(data[j]['email'])
		
    print(ans)
    print(len(ans))
    f.close()

scrap()

