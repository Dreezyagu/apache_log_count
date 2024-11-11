import ast

total_data = []

for i in range(0,5):
    with open(f'part-0000{i}', 'r') as file:
        data1 = file.read().strip()
        array1 = ast.literal_eval(data1)
        total_data.extend(array1)

sorted_data = sorted(total_data, key=lambda x: x[1], reverse=True)

# Open the file in write mode
with open('result.txt', 'w') as file:
    # Write each tuple in a readable format
    for word, count in sorted_data[:5]:
        file.write(f"domain: {word}\t\t\t\t\t\tCount: {count}\n")
    


