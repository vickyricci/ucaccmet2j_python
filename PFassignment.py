import json
seattle_month= [0]*12
total_monthly_precipitation= []
total_relative_percipitation= []
with open('precipitation.json', encoding='utf8') as file: 
    precipitation= json.load(file)
    for item in precipitation:
       if item ['station'] == 'GHCND:US1WAKG0038':
            month = int(item['date'].split('-')[1])
            seattle_month[month-1] +=  item['value']
           # total_monthly_precipitation.append(item["value"])
            #total_relative_percipitation= 

total_precipitation= int(sum(seattle_month))
#print('The total over the whole year is:' +str(total_precipitation)) #part1
total_relative_percipitation = [i/total_precipitation*100 for i in seattle_month] #shorthand loop
print(total_relative_percipitation) 
with open ('seattle_precipitation.json', 'w') as file:
    	json.dump(total_relative_percipitation,file,indent=4)


#print(seattle_month)    
#print(f'The average rainfall per month is {total_precipitation/len(seattle_month)}')
'''
toatal_monthly_precipitation [1]
'''
#print(total_monthly_precipitation)        

