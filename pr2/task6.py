import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.manifold import TSNE

# Загрузка набора данных MNIST
mnist = fetch_openml("mnist_784")
data, labels = mnist.data / 255.0, mnist.target.astype(int)

# Выберите подмножество данных для ускорения вычислений (например, первые 1000 образцов)
n_samples = 1000
data = data[:n_samples]
labels = labels[:n_samples]

# Задайте значения перплексии, которые вы хотите исследовать
perplexities = [5, 30, 50]

# Создайте подзадачи t-SNE с разными значениями перплексии
embeddings = []
for perplexity in perplexities:
    tsne = TSNE(n_components=2, perplexity=perplexity, random_state=0)
    embeddings.append(tsne.fit_transform(data))

# Визуализация
plt.figure(figsize=(15, 5))
for i, perplexity in enumerate(perplexities):
    plt.subplot(1, len(perplexities), i + 1)
    plt.scatter(embeddings[i][:, 0], embeddings[i][:, 1], c=labels, cmap="jet", s=10)
    plt.title(f"t-SNE (Perplexity={perplexity})")
    plt.xticks([])
    plt.yticks([])

plt.show()
