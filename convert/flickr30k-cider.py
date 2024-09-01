import json
import sys
from collections import defaultdict
from cider import CiderScorer


def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def load_jsonl(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data


def main(ground_truth_path, question_path, answer_path):
    # Load data
    ground_truth = load_json(ground_truth_path)
    questions = load_jsonl(question_path)
    answers = load_jsonl(answer_path)

    # Create a mapping from image name to ground truth captions
    image_to_captions = {item['image']: item['caption']
                         for item in ground_truth}

    # Create a mapping from question_id to image name
    question_id_to_image = {q['question_id']: q['image'] for q in questions}

    # Initialize CIDEr scorer
    cider_scorer = CiderScorer(n=4, sigma=6.0)

    # Process each answer
    for answer in answers:
        question_id = answer['question_id']
        image = question_id_to_image.get(question_id)
        if image:
            gt_answers = image_to_captions.get(image)
            if gt_answers:
                cider_scorer += (answer['text'], gt_answers)

    # Compute CIDEr score
    (score, scores) = cider_scorer.compute_score()
    print(f"CIDEr Score: {score}")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <ground_truth_path> <question_path> <answer_path>")
        sys.exit(1)

    ground_truth_path = sys.argv[1]
    question_path = sys.argv[2]
    answer_path = sys.argv[3]

    main(ground_truth_path, question_path, answer_path)
