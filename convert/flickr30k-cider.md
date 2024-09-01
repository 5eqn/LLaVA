You are a experienced programmer using Linux. Please write a Python script according to given environment and task.

## Environment

Content of ground truth `../.cache/lavis/flickr30k/images/flickr30k-images/results.csv`:

```csv
image_name| comment_number| comment
1000092795.jpg| 0| Two young guys with shaggy hair look at their hands while hanging out
in the yard .
1000092795.jpg| 1| Two young , White males are outside near many bushes .
1000092795.jpg| 2| Two men in green shirts are standing in a yard .
1000092795.jpg| 3| A man in a blue shirt standing in a garden .
1000092795.jpg| 4| Two friends enjoy time spent together .
10002456.jpg| 0| Several men in hard hats are operating a giant pulley system .
10002456.jpg| 1| Workers look down from up above on a piece of equipment .
10002456.jpg| 2| Two men working on a machine wearing hard hats .
10002456.jpg| 3| Four men on top of a tall structure .
10002456.jpg| 4| Three men on a large rig .
1000268201.jpg| 0| A child in a pink dress is climbing up a set of stairs in an entry way
 .
1000268201.jpg| 1| A little girl in a pink dress going into a wooden cabin .
1000268201.jpg| 2| A little girl climbing the stairs to her playhouse .
1000268201.jpg| 3| A little girl climbing into a wooden playhouse
1000268201.jpg| 4| A girl going into a wooden building .
```

Content of question `./playground/data/eval/flickr30k/test.jsonl`:

```
{"question_id": 262144005, "image": "COCO_test2015_000000262144.jpg", "text": "What credi
t card company is on the banner in the background?\nAnswer the question using a single wo
rd or phrase.", "category": "default"}
{"question_id": 262144003, "image": "COCO_test2015_000000262144.jpg", "text": "Is the pit
cher wearing a hat?\nAnswer the question using a single word or phrase.", "category": "de
fault"}
{"question_id": 262144000, "image": "COCO_test2015_000000262144.jpg", "text": "Is the bal
l flying towards the batter?\nAnswer the question using a single word or phrase.", "categ
ory": "default"}
```

Content of answer `./playground/data/eval/flickr30k/answers/flickr30k/llava-v1.5-7b/merge.jsonl`:

```
{"question_id": 262144005, "prompt": "What credit card company is on the banner in the ba
ckground?\nAnswer the question using a single word or phrase.", "text": "Mastercard", "an
swer_id": "Nkgs9ckMfp3aPdrR8pf7DQ", "model_id": "llava-v1.5-7b", "metadata": {}}
{"question_id": 262144003, "prompt": "Is the pitcher wearing a hat?\nAnswer the question
using a single word or phrase.", "text": "Yes", "answer_id": "h3vKaP2DUhkFZEArPuAaUc", "m
odel_id": "llava-v1.5-7b", "metadata": {}}
{"question_id": 262144000, "prompt": "Is the ball flying towards the batter?\nAnswer the
question using a single word or phrase.", "text": "No", "answer_id": "dzLSh7hu4C2dbgUa6gk
c7V", "model_id": "llava-v1.5-7b", "metadata": {}}
```

## Task

Your Python script should calculate CIDEr score with answer and grount truth. An example of using CIDEr is:

```py
from .cider import CiderScorer
with open(answer_path, 'r') as f:
    dict = json.load(f)
    cider_scorer = CiderScorer(n=4, sigma=6.0)
    for i in range(len(dict)):
        gt_answers = dict[i]['gt_answers']
        answer = dict[i]['answer']
        cider_scorer += (answer, gt_answers)
    (score, scores) = cider_scorer.compute_score()
```

You should change the example usage according to actual requirements.

Note that `gt_answers` has multiple entries. You should get `gt_answers` by getting `question_id` in answer file, then get `image` from question file, then get all 5 comments from grount truth CSV.

You should read all paths from command line arguments.
