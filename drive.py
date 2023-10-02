import gdown

url = 'https://drive.google.com/file/d/1uFTzwFc3tmS-D7azjMiJcxSfn71BPqKt/view?usp=sharing'
output_path = 'graph_ML.pk'

gdown.download(url, output_path, quiet=False, fuzzy=True)
