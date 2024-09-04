You are a experienced programmer using Linux. Please write a Python script according to given environment and task.

## Environment

Content of `./playground/data/eval/okvqa/OpenEnded_mscoco_train2014_questions.json`:

```json
{"license": {"url": "http://creativecommons.org/licenses/by/4.0/", "name": "Creative Commons Attribution 4.0 International License"}, "data_subtype": "train2014", "task_type": "Open-Ended", "questions": [{"image_id": 51606, "question": "What is the hairstyle of the blond called?", "question_id": 516065}, {"image_id": 81721, "question": "How old do you have to be in canada to do this?", "question_id": 817215}, {"image_id": 480208, "question": "Can you guess the place where the man is playing?", "question_id": 4802085}]}
```

Content of `./playground/data/eval/okvqa/mscoco_train2014_annotations.json`:

```json
{
  "license": {
    "url": "http://creativecommons.org/licenses/by/4.0/",
    "name": "Creative Commons Attribution 4.0 International License"
  },
  "data_subtype": "train2014",
  "question_types": {
    "eight": "Plants and Animals",
    "nine": "Science and Technology",
    "four": "Sports and Recreation",
    "six": "Geography, History, Language and Culture",
    "two": "Brands, Companies and Products",
    "other": "Other",
    "one": "Vehicles and Transportation",
    "five": "Cooking and Food",
    "ten": "Weather and Climate",
    "seven": "People and Everyday life",
    "three": "Objects, Material and Clothing"
  },
  "annotations": [
    {
      "image_id": 51606,
      "answer_type": "other",
      "question_type": "four",
      "question_id": 516065,
      "answers": [
        {
          "answer_id": 1,
          "raw_answer": "pony tail",
          "answer_confidence": "yes",
          "answer": "pony tail"
        },
        {
          "answer_id": 2,
          "raw_answer": "pony tail",
          "answer_confidence": "yes",
          "answer": "another answer"
        }
      ]
    }
  ]
}
```

## Task

Your Python script should convert the above JSON to `./playground/data/train/okvqa/train.json` with format below:

```json
[
    {
        "id": "0f0d362d-1b75-4104-9aff-c2d4f457cc0e",
        "image": "COCO_train2014_000000051606.jpg",
        "conversations": [
            {
                "from": "human",
                "value": "<image>\nWhat is the hairstyle of the blond called?\nAnswer the question using a single word or phrase."
            },
            {
                "from": "gpt",
                "value": "pony tail"
            }
        ]
    },
    {
        "id": "b6608a4b-66b4-4818-8efb-8f9928cba13c",
        "image": "COCO_train2014_000000051606.jpg",
        "conversations": [
            {
                "from": "human",
                "value": "<image>\nWhat is the hairstyle of the blond called?\nAnswer the question using a single word or phrase."
            },
            {
                "from": "gpt",
                "value": "another answer"
            }
        ]
    }
]
```

You should change the example usage according to actual requirements.

You should read all paths from command line arguments.

You should generate a conversation for each answer.
