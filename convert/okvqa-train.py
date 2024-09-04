import json
import uuid
import sys


def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)


def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)


def main(questions_path, annotations_path, output_path):
    questions_data = read_json(questions_path)
    annotations_data = read_json(annotations_path)

    output_data = []
    suffix = "Answer the question using a single word or phrase."

    for annotation in annotations_data['annotations']:
        question_id = annotation['question_id']
        image_id = annotation['image_id']
        question = next(q['question'] for q in questions_data['questions']
                        if q['question_id'] == question_id)
        image_name = f"COCO_train2014_000000{image_id:06d}.jpg"

        for answer in annotation['answers']:
            conversation = {
                "id": str(uuid.uuid4()),
                "image": image_name,
                "conversations": [
                    {
                        "from": "human",
                        "value": f"<image>\n{question}\n" + suffix
                    },
                    {
                        "from": "gpt",
                        "value": answer['answer']
                    }
                ]
            }
            output_data.append(conversation)

    write_json(output_data, output_path)


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <questions_path> <annotations_path> <output_path>")
        sys.exit(1)

    questions_path = sys.argv[1]
    annotations_path = sys.argv[2]
    output_path = sys.argv[3]

    main(questions_path, annotations_path, output_path)
