import json

def read_write_json_files(input, output):
    # load the input json file
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    #change the size field in every record to the value 35
    for record in data:
        record['size'] = 35
        
    #write back the result in reverse order to a file
    with open(output_file, 'w') as file:
        json.dump(data[::-1], file, indent=4)



if __name__ == "__main__":
    input_file = "large-file.json"
    output_file = "output.2.3.json"
    read_write_json_files(input_file, output_file)