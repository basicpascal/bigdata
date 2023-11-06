import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE
import umap
import time

# Загрузка набора данных MNIST
mnist = fetch_openml("mnist_784")
data, labels = mnist.data / 255.0, mnist.target.astype(int)

# Выберите подмножество данных для ускорения вычислений (например, первые 1000 образцов)
n_samples = 1000
data = data[:n_samples]
labels = labels[:n_samples]

# Параметры для t-SNE
tsne_perplexity = 30
tsne_random_state = 0

# Параметры для UMAP
umap_n_neighbors = [5, 30, 50]  # Разные значения n_neighbors для UMAP
umap_min_dist = [0.1, 0.5, 0.9]  # Разные значения min_dist для UMAP

# Время выполнения t-SNE
start_time_tsne = time.time()
tsne = TSNE(n_components=2, perplexity=tsne_perplexity, random_state=tsne_random_state)
tsne_embedding = tsne.fit_transform(data)
tsne_time = time.time() - start_time_tsne

# Визуализация t-SNE
plt.figure(figsize=(15, 5))
plt.subplot(1, 4, 1)
plt.scatter(tsne_embedding[:, 0], tsne_embedding[:, 1], c=labels, cmap="jet", s=10)
plt.title(f"t-SNE (Perplexity={tsne_perplexity})")
plt.xticks([])
plt.yticks([])

# Время выполнения UMAP и визуализация
umap_embeddings = []

for n_neighbors in umap_n_neighbors:
    for min_dist in umap_min_dist:
        start_time_umap = time.time()
        umap_model = umap.UMAP(n_neighbors=n_neighbors, min_dist=min_dist)
        umap_embedding = umap_model.fit_transform(data)
        umap_time = time.time() - start_time_umap
        umap_embeddings.append(umap_embedding)

# Визуализация UMAP с разными параметрами
for i, (n_neighbors, min_dist) in enumerate(zip(umap_n_neighbors, umap_min_dist)):
    plt.subplot(1, 4, i + 2)
    plt.scatter(umap_embeddings[i][:, 0], umap_embeddings[i][:, 1], c=labels, cmap="jet", s=10)
    plt.title(f"UMAP (n_neighbors={n_neighbors}, min_dist={min_dist})")
    plt.xticks([])
    plt.yticks([])

# Отобразить графики
plt.show()

# Вывод времени выполнения
print(f"Время выполнения t-SNE: {tsne_time:.2f} секунд")
for i, (n_neighbors, min_dist) in enumerate(zip(umap_n_neighbors, umap_min_dist)):
    print(f"Время выполнения UMAP (n_neighbors={n_neighbors}, min_dist={min_dist}): {umap_time:.2f} секунд")
