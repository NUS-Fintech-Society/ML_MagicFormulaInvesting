import pandas as pd
table_a = pd.read_csv("Data_A.csv")
table_b = pd.read_csv("Data_B_new.csv")
table_c = table_a
market_2014 = table_b['p_2019'][0]/table_b['p_2014'][0]
market_2015 = table_b['p_2020'][0]/table_b['p_2015'][0]
market_2016 = table_b['p_2021'][0]/table_b['p_2016'][0]
market_2017 = table_b['p_2022'][0]/table_b['p_2017'][0]
label = []
count1 = 0
for i in table_a.index:
    code = table_a['stockcode'][i]+'.SI'
    temp = table_b[table_b['Name']==code].index.values
    if len(temp)==0:
        label.append('NaN')
        continue
    j = table_b[table_b['Name']==code].index.values[0]
    if table_a['year'][i]=='2014':
        if table_b['p_2019'][j]/table_b['p_2014'][j] > market_2014:
            label.append(1)
            count1+=1
        else:
            label.append(0)
    elif table_a['year'][i]=='2015':
        if table_b['p_2020'][j]/table_b['p_2015'][j] > market_2015:
            label.append(1)
            count1+=1
        else:
            label.append(0)
    elif table_a['year'][i]=='2016':
        if table_b['p_2021'][j]/table_b['p_2016'][j] > market_2016:
            label.append(1)
            count1+=1
        else:
            label.append(0)
    elif table_a['year'][i]=='2017':
        if table_b['p_2022'][j]/table_b['p_2017'][j] > market_2017:
            label.append(1)
            count1+=1
        else:
            label.append(0)
    else:
        label.append('NaN')
table_c['label'] = label
table_c = table_c.drop(table_c[table_c.label == 'NaN'].index)
table_c = table_c.drop(table_c[table_c.ey == float('inf')].index)
table_c = table_c.drop(table_c[table_c.roc == 0].index)
print(count1)
table_c.to_csv('Data_C.csv',index=False)
