import sys
import json
import csv
from collections import defaultdict
from cider import CiderScorer


def read_csv(file_path):
    image_comments = defaultdict(list)
    with open(file_path, 'r') as f:
        reader = csv.reader(f, delimiter='|')
        for row in reader:
            image_name = row[0].strip()
            comment = row[2].strip()
            image_comments[image_name].append(comment)
    return image_comments


def read_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)


def read_jsonl(file_path):
    data = []
    with open(file_path, 'r') as f:
        for line in f:
            data.append(json.loads(line))
    return data


def main(ground_truth_path, question_path, answer_path):
    image_comments = read_csv(ground_truth_path)
    questions = read_json(question_path)
    answers = read_jsonl(answer_path)

    question_to_image = {q['question_id']: q['image'] for q in questions}

    cider_scorer = CiderScorer(n=4, sigma=6.0)

    for answer in answers:
        question_id = answer['question_id']
        image_name = question_to_image[question_id]
        gt_answers = image_comments[image_name]
        cider_scorer.append((answer['text'], gt_answers))

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
