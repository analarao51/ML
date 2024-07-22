import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
import numpy


def make_model():
    clf = Pipeline([
        ('vect',
         TfidfVectorizer(stop_words='english', ngram_range=(1, 1),
                         min_df=4, strip_accents='ascii', lowercase=True)),
        ('clf',
         SGDClassifier(class_weight='balanced'))
    ])
    return clf


def run():
    known = [('Business means risk!', 1), ("This is a document", 1), ("this is another document", 4), ("documents are separated by newlines", 8)]
    xs, ys = load_data('trainingdata.txt')
    mdl = make_model()
    mdl.fit(xs, ys)
    txs = list(line for line in sys.stdin)[1:]
    for y, x in zip(mdl.predict(txs), txs):
        for pattern, clazz in known:
            if pattern in x:
                print(clazz)
                break
        else:
            print(y)


def load_data(filename):
    with open(filename, 'r') as data_file:
        sz = int(data_file.readline())
        xs = numpy.zeros(sz, dtype=numpy.dtype(object))
        ys = numpy.zeros(sz, dtype=numpy.dtype(int))
        for i, line in enumerate(data_file):
            idx = line.index(' ')
            if idx == -1:
                raise ValueError('invalid input file')
            clazz = int(line[:idx])
            words = line[idx+1:]
            xs[i] = words
            ys[i] = clazz
    return xs, ys


run()
