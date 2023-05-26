import json



# Sample JSON string
# Read and parse the JSON file
with open('GetTaskList2.json', 'r', encoding="utf-8") as file:
    json_string = json.load(file)

def extract_values(obj, key):
    """Recursively extract the values of a given key from a JSON object."""
    arr = []
    def extract(obj, arr, key):
        if isinstance(obj, dict):
            for k, v in obj.items():
                if k == key:
                    arr.append(v)
                elif isinstance(v, (dict, list)):
                    extract(v, arr, key)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    return extract(obj, arr, key)

# Parse JSON string from file
parsed_json_string = json.dumps(json_string)

# Parse JSON string
parsed_json = json.loads(parsed_json_string)
#print(parsed_json)
# Extract 'tasksetid' values
tasksetid_list = extract_values(parsed_json, 'TaskSetID')

#print(tasksetid_list)

my_list = []
redundant_list = []
count = 0

for item in tasksetid_list:
    if item not in my_list:
        my_list.append(item)
    else:
        count+=1
        redundant_list.append(item)


print(my_list)

# Join the strings in the list using the '#' separator
joined_string = '#'.join(my_list)


print(joined_string)

print("redundant:" + str(count))
print(redundant_list)