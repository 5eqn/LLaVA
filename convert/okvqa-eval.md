You are a experienced programmer using Linux. Please write a Python script according to given environment and task.

## Environment

Content of `./playground/data/eval/okvqa/OpenEnded_mscoco_val2014_questions.json`:

```json
{"license": {"url": "http://creativecommons.org/licenses/by/4.0/", "name": "Creative Commons Attribution 4.0 International License"}, "data_subtype": "train2014", "task_type": "Open-Ended", "questions": [{"image_id": 51606, "question": "What is the hairstyle of the blond called?", "question_id": 516065}, {"image_id": 81721, "question": "How old do you have to be in canada to do this?", "question_id": 817215}, {"image_id": 480208, "question": "Can you guess the place where the man is playing?", "question_id": 4802085}]}
```

## Task

Your Python script should convert the above JSON to `./playground/data/eval/okvqa/test.jsonl` with format below:

```json
{"question_id": 516065, "image": "COCO_val2014_000000051606.jpg", "text": "What is the hairstyle of the blond called?\nAnswer the question using a single word or phrase."}
{"question_id": 4802085, "image": "COCO_val2014_000000081721.jpg", "text": "How old do you have to be in canada to do this?\nAnswer the question using a single word or phrase."}
```

You should change the example usage according to actual requirements.

You should read all paths from command line arguments.
