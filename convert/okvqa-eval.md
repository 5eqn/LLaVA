You are a experienced programmer using Linux. Please write a Python script according to given environment and task.

## Environment

Content of `./playground/data/eval/okvqa/OpenEnded_mscoco_val2014_questions.json`:

```json
{"license": {"url": "http://creativecommons.org/licenses/by/4.0/", "name": "Creative Commons Attribution 4.0 International License"}, "data_subtype": "train2014", "task_type": "Open-Ended", "questions": [{"image_id": 51606, "question": "What is the hairstyle of the blond called?", "question_id": 516065}, {"image_id": 81721, "question": "How old do you have to be in canada to do this?", "question_id": 817215}, {"image_id": 480208, "question": "Can you guess the place where the man is playing?", "question_id": 4802085}}
```

## Task

Your Python script should convert the above JSON to `./test.json` with format below:

```json
{"question_id": "54810ef7-b174-4b59-b515-6394bd139be1", "image": "COCO_val2014_000000441814.jpg", "text": "What is the hairstyle of the blond called?"}
{"question_id": "4af03e2f-5f0a-45f5-a75b-11dc2dcf5313", "image": "COCO_val2014_000000051606.jpg", "text": "Describe this image using one or more simple sentences"}
```

You create 5 test cases for each image. For test case `i`:

- `id` is a unique UUID assigned to each test case.
- `image` should be unchanged.
- `conversations` are expected conversation for this test case.
	- The first message's content is constant over all conversations.
	- The second message's content should be `annotations[i]`.

## I/O

Input: `~/.cache/lavis/flickr30k/annotations/test.json`
Output: `./test.json`
