## Convert csv to JSON for 3D force-direcetd graph



import pandas as pd

data = pd.read_csv('notebooks/corr_graph.csv')
data.copy()
data_filt = data[data['Weight']>0]

nodes = []
group_number = []

count = 1

for i in range(len(data_filt)):
    
    if data_filt['Source'].iloc[i] not in nodes:
        nodes.append(data_filt['Source'].iloc[i])
        group_number.append(count)
        count+=1
    if data_filt['Target'].iloc[i] not in nodes:
        nodes.append(data_filt['Target'].iloc[i])
        group_number.append(count)
        count+=1




node_data = pd.DataFrame()
node_data['id'] = nodes
node_data['group'] = group_number

edge_source = []
edge_target = []
edge_value = []

for i in range(len(data_filt)):
    edge_source.append(data_filt['Source'].iloc[i])
    edge_target.append(data_filt['Target'].iloc[i])
    edge_value.append(data_filt['Weight'].iloc[i])
    
    


edge_data = pd.DataFrame()
edge_data['source'] = edge_source
edge_data['target'] = edge_target
edge_data['value'] = edge_value


edge_data.to_json('data_corr.json', orient='records')


# print(edge_data)





# data_comb = data_filt['Source']


# print(len(data_filt))

