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
with open(output_file_path, 'w') as file:
    for item in data:
        image = item['image']
        captions = item['caption']
        line = json.dumps({
            "question_id": str(uuid.uuid4()),
            "image": image,
            "text": "A short image caption.",
        }) + "\n"
        file.write(line)

print(f"Processed data has been written to {output_file_path}")
