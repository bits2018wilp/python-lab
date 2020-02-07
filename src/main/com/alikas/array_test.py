from sklearn.datasets import load_digits
from sklearn.naive_bayes import BernoulliNB, GaussianNB, MultinomialNB
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn import datasets

datasets.load_digits()

cpath = 'D:\\kaggle\\basicshapes\\shapes\\'+ 'circles'

datasets.load_files(cpath)
a = [1, 2, 3, 4, 5]
print(len(a))
print(a[1])
a[2] = 8
print(a.append(88), a)

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5, 6]

print( a == b)
print( 5 in b)
