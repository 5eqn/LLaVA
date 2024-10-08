import json
import uuid
import os

import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Process JSON data.')
parser.add_argument('input_file', type=str, help='Path to the input JSON file')
parser.add_argument('output_file', type=str,
                    help='Path to the output JSON file')
args = parser.parse_args()

# Define the input and output file paths from command line arguments
input_file_path = os.path.expanduser(args.input_file)
output_file_path = os.path.expanduser(args.output_file)
print(f"Convert {input_file_path} to {output_file_path}")

# Read the input JSON file
with open(input_file_path, 'r') as file:
    data = json.load(file)

# Process the data
output_data = []
for item in data:
    image = item['image']
    caption = item['caption']
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
                "value": caption
            }
        ]
    }
    output_data.append(conversation)

# Write the output JSON file
with open(output_file_path, 'w') as file:
    json.dump(output_data, file, indent=4)

print(f"Processed data has been written to {output_file_path}")
