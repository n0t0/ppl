# f = open('schedule.txt', 'r')
# # print(f)

# # data = f.read()
# # print(data)

# for line in f:
#     print(line)

# # f.close()

# # with open('schedule.txt', 'r') as f:
# #     data = f.read()

# total = 0.0 

with open('data.csv', 'r') as f:
    headers = next(f)       # Skip a single line of input 
    for line in f: 
        line = line.strip()
        parts = line.split(',')
        # parts[0] = parts[0].strip('"')
        # parts[1] = parts[1].strip('"')
        total += parts[4]*parts[5]
        # print(parts)
        
        
print('Total cost:', total)