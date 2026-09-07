from datasets import load_dataset
import gzip

wikija_dataset = load_dataset(
    path="singletongue/wikipedia-utils",
    name="passages-c400-jawiki-20230403",
    split="train",
)

ibaraki=""
tstr = '茨城'
for data in wikija_dataset:
    if ((tstr in data['title']) or (tstr in data['text'])):
        ibaraki += (data['text'] + "\n\n")

with gzip.open('ibaraki.txt.gz', 'wb') as f:
    f.write(ibaraki.encode('utf-8'))