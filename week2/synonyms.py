import fasttext

TOP_WORDS_PATH = '/workspace/datasets/fasttext/top_words.txt'
MODEL_PATH = '/workspace/datasets/fasttext/title_model.bin'


def create_synonyms(f, threshold=0.75):
    
    model = fasttext.load_model(MODEL_PATH)
    for word in f.readlines():
        word = word.replace('\n', '')
        neighbors = [x[1] for x in filter(lambda x: x[0] >= threshold, model.get_nearest_neighbors(word))]
        if neighbors:
            result = [word] + neighbors
            print(', '.join(result))


if __name__ == '__main__':
    with open(words_file_path,'r') as f
        create_synonyms(f)