from mk_base_text_data import ibaraki
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)
import pickle

splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=100,
    length_function=len,
    separators=["\n\n", "\n", "。", "、", ""],
)

# ibarakiはテキストデータ文字列
chunks = splitter.split_text(ibaraki)

with open("chunks.pkl", "wb") as f:
    pickle.dump(chunks, f)

    print('中身',chunks)