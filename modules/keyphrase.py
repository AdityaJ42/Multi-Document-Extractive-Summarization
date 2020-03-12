import pke
from nltk.corpus import stopwords

# 1. create a YAKE extractor.
extractor = pke.unsupervised.YAKE()

# 2. load the content of the document.
extractor.load_document(input='input2pr.txt', language='en', normalization=None)

# 3. select {1-3}-grams not containing punctuation marks and not
#    beginning/ending with a stopword as candidates.
stoplist = stopwords.words('english')
extractor.candidate_selection(n=2, stoplist=stoplist)

# 4. weight the candidates using YAKE weighting scheme, a window (in
#    words) for computing left/right contexts can be specified.
window = 1#2
use_stems = False # use stems instead of words for weighting
extractor.candidate_weighting(window=window, stoplist=stoplist, use_stems=use_stems)
 
# 5. get the 10-highest scored candidates as keyphrases.
#    redundant keyphrases are removed from the output using levenshtein
#    distance and a threshold.
threshold = 1 #1
keyphrases = extractor.get_n_best(n=10, threshold=threshold)
print(keyphrases)

# for i in range(0,10):
# print(extractor.is_redundant(keyphrases[4][0],keyphrases,0.8) )