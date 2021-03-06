import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from time import time
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


# define column names

# loading training data
df = pd.read_csv('normalizedFeatures.csv')
df = df.values

X = df[0:, 1:-1]
X = np.asarray(X, 'float')

Y = np.zeros(len(X))

for i in range(len(Y)):
    if df[i, -1] == 'prog':
        Y[i] = 1
    
y = Y.ravel()


from matplotlib import offsetbox
from sklearn import (manifold, datasets, decomposition, ensemble,
                     discriminant_analysis, random_projection)


n_samples, n_features = X.shape
n_neighbors = 30

#----------------------------------------------------------------------
# Scale and visualize the embedding vectors
def plot_embedding(X, title=None):
    x_min, x_max = np.min(X, 0), np.max(X, 0)
    X = (X - x_min) / (x_max - x_min)

    plt.figure()
    ax = plt.subplot(111)
    for i in range(X.shape[0]):
        plt.scatter(X[i, 0], X[i, 1], color=plt.cm.Set1(y[i] *2))
#        plt.text(X[i, 0], X[i, 1], str(y[i]),
#                 color=plt.cm.Set1(y[i] / 1),
#                 fontdict={'weight': 'bold', 'size': 9})

#    if hasattr(offsetbox, 'AnnotationBbox'):
#        # only print thumbnails with matplotlib > 1.0
#        shown_images = np.array([[1., 1.]])  # just something big
#        for i in range(X.shape[0]):
#            dist = np.sum((X[i] - shown_images) ** 2, 1)
#            if np.min(dist) < 4e-3:
#                # don't show points that are too close
#                continue
#            shown_images = np.r_[shown_images, [X[i]]]
#            imagebox = offsetbox.AnnotationBbox(
#                offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r),
#                X[i])
#            ax.add_artist(imagebox)
#    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)

#----------------------------------------------------------------------
# Scale and visualize the embedding vectors
def plot_embedding3D(X, title=None):
#    x_min, x_max = np.min(X, 0), np.max(X, 0)
#    X = (X - x_min) / (x_max - x_min)

    fig = plt.figure()
    ax = Axes3D(fig)
    for i in range(X.shape[0]):
        ax.scatter(X[i, 0], X[i, 1], X[i, 2], color=plt.cm.Set1(y[i] / 1))
#        plt.text(X[i, 0], X[i, 1], str(y[i]),
#                 color=plt.cm.Set1(y[i] / 1),
#                 fontdict={'weight': 'bold', 'size': 9})

#    if hasattr(offsetbox, 'AnnotationBbox'):
#        # only print thumbnails with matplotlib > 1.0
#        shown_images = np.array([[1., 1.]])  # just something big
#        for i in range(X.shape[0]):
#            dist = np.sum((X[i] - shown_images) ** 2, 1)
#            if np.min(dist) < 4e-3:
#                # don't show points that are too close
#                continue
#            shown_images = np.r_[shown_images, [X[i]]]
#            imagebox = offsetbox.AnnotationBbox(
#                offsetbox.OffsetImage(digits.images[i], cmap=plt.cm.gray_r),
#                X[i])
#            ax.add_artist(imagebox)
#    plt.xticks([]), plt.yticks([])
    if title is not None:
        plt.title(title)


'''PCA'''
#print("Computing PCA projection")
#X_pca = decomposition.TruncatedSVD(n_components=3).fit_transform(X)
#plot_embedding(X_pca[:, 0:2],
#               "Principal Components projection of the digits")
# Projection on to the first 2 linear discriminant components


'''Locally linear embedding of the digits dataset'''
#n_neighbors = 12
#print("Computing LLE embedding")
#clf = manifold.LocallyLinearEmbedding(n_neighbors, n_components=5,
#                                      method='standard')
#t0 = time()
#X_lle = clf.fit_transform(X)
#print("Done. Reconstruction error: %g" % clf.reconstruction_error_)
#
###plot_embedding3D(X_lle[:, 0:3],
###               "Locally Linear Embedding of the digits (time %.2fs)" %
###               (time() - t0))
##
#plot_embedding(X_lle[:, 0:2],
#               "Locally Linear Embedding of the digits (time %.2fs)" %
#               (time() - t0))
##plot_embedding(X_lle[:, 2:4],
##               "Locally Linear Embedding of the digits (time %.2fs)" %
##               (time() - t0))
    
    
'''Isomap projection of the digits dataset'''
#print("Computing Isomap embedding")
#t0 = time()
#n_neighbors = 5
#X_iso = manifold.Isomap(n_neighbors, n_components=3).fit_transform(X)
#print("Done.")
#plot_embedding(X_iso,
#               "Isomap projection of the digits (time %.2fs)" %
#               (time() - t0))

#
'''Modified Locally linear embedding of the digits dataset'''
#n_neighbors = 31
#print("Computing modified LLE embedding")
#clf = manifold.LocallyLinearEmbedding(n_neighbors, n_components=2,
#                                      method='modified')
#t0 = time()
#X_mlle = clf.fit_transform(X)
#print("Done. Reconstruction error: %g" % clf.reconstruction_error_)
#plot_embedding(X_mlle,
#               "Modified Locally Linear Embedding of the digits (time %.2fs)" %
#               (time() - t0))

''' t-SNE embedding of the digits dataset'''
#print("Computing t-SNE embedding")
#n_neighbors = 3
#tsne = manifold.TSNE(n_components=2, init='pca', random_state=0)
#t0 = time()
#X_tsne = tsne.fit_transform(X)
#
#plot_embedding(X_tsne,
#               "t-SNE embedding of the digits (time %.2fs)" %
#               (time() - t0))
#
#plt.show()


'''MDS  embedding of the digits dataset'''
print("Computing MDS embedding")
clf = manifold.MDS(n_components=2, n_init=1, max_iter=1000)
t0 = time()
X_mds = clf.fit_transform(X)
print("Done. Stress: %f" % clf.stress_)
plot_embedding(X_mds,
               "MDS embedding of the digits (time %.2fs)" %
               (time() - t0))