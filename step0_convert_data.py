import argparse
import json
import os
from tqdm import tqdm


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset","-d",
                         type=str, required=True, help='dataset name', choices=['hotpotqa','musique', '2wikimultihopqa'])
    args = parser.parse_args()

    corpus = json.load(open(f'data/{args.dataset}_corpus.json'))
    os.makedirs(f'data/{args.dataset}/input', exist_ok=True)
    
    for idx, passage in tqdm(enumerate(corpus), total=len(corpus)):
        text = passage['text']
        title = passage['title']

        content = title + '\n\n' + text
        idx = str(idx) if 'idx' not in passage else passage['idx']

        with open(f'data/{args.dataset}/input/{idx}.txt', 'w') as f:
            f.write(content)