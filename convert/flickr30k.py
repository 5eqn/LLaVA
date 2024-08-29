import json
import uuid

# Define the input and output file paths
input_file_path = '../.cache/lavis/flickr30k/annotations/test.json'
output_file_path = './test.json'

# Read the input JSON file
with open(input_file_path, 'r') as file:
    data = json.load(file)

# Process the data
output_data = []
for item in data:
    image = item['image']
    captions = item['caption']
    for i in range(len(captions)):
        conversation = {
            "id": str(uuid.uuid4()),
            "image": image,
            "conversations": [
                {
                    "from": "human",
                    "value": "<image>\nA short image caption."
                },
                {
                    "from": "gpt",
                    "value": captions[i]
                }
            ]
        }
        output_data.append(conversation)

# Write the output JSON file
with open(output_file_path, 'w') as file:
    json.dump(output_data, file, indent=4)

print(f"Processed data has been written to {output_file_path}")
