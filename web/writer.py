import csv

def write_to_csv(filename, data, headers):    
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=headers)
        
        writer.writeheader()
        
        writer.writerows(data)