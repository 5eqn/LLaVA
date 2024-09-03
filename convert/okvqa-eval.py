import json
import sys

def main(input_file, output_file):
    # Read the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Prepare the output data
    output_data = []
    for question in data['questions']:
        image_id = str(question['image_id']).zfill(12)  # Zero-padding to 12 digits
        image_name = f"COCO_val2014_{image_id}.jpg"
        output_data.append({
            "question_id": question['question_id'],
            "image": image_name,
            "text": question['question']
        })

    # Write the output data to a JSONL file
    with open(output_file, 'w') as f:
        for entry in output_data:
            f.write(json.dumps(entry) + '\n')

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <input_json_file> <output_jsonl_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    main(input_file, output_file)