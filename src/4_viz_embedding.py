from utils.ollama_model import get_embedding_model
import matplotlib.pyplot as plt
import mplcursors
from sklearn.decomposition import PCA
import numpy as np

def visualize_embeddings_2D(embeddings, texts, labels):
    pca = PCA(n_components=2)
    reduced_embeddings = pca.fit_transform(embeddings)

    plt.figure(figsize=(10, 7))
    scatter = plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], c=labels, cmap='viridis')
    plt.colorbar(scatter)
    plt.title('2D Visualization of Embeddings')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    cursor = mplcursors.cursor(scatter, hover=True)

    @cursor.connect("add")
    def on_add(sel):
        sel.annotation.set_text(f'Label: {labels[sel.index]}\nSentence: {texts[sel.index]}')
    plt.show()

def visualize_embeddings_3D(embeddings, texts, labels):
    pca = PCA(n_components=3)
    reduced_embeddings = pca.fit_transform(embeddings)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], reduced_embeddings[:, 2], c=labels, cmap='viridis')
    plt.colorbar(scatter)
    ax.set_title('3D Visualization of Embeddings')
    ax.set_xlabel('Principal Component 1')
    ax.set_ylabel('Principal Component 2')
    ax.set_zlabel('Principal Component 3')

    cursor = mplcursors.cursor(scatter, hover=True)
    
    @cursor.connect("add")
    def on_add(sel):
        sel.annotation.set_text(f'Label: {labels[sel.index]}\nSentence: {texts[sel.index]}')
    plt.show()

def visualize_embeddings(embeddings, texts, labels, method='2D'):
    if method == '2D':
        visualize_embeddings_2D(embeddings, texts, labels)
    elif method == '3D':
        visualize_embeddings_3D(embeddings, texts, labels)
    else:
        raise ValueError("Method must be '2D' or '3D'")
    
def main():
    ollama = get_embedding_model(model_name="nomic-embed-text-v2-moe:latest", port=8085)
    texts = ["This is a sample sentence.", 
             "Another example of text.", 
             "More text data for embedding.", 
             "Yet another text example.",
             "natural language processing is fun!",
             "embedding visualization is useful for understanding data.",
             "PCA helps reduce dimensionality while preserving variance.",
             "3D visualization can reveal complex relationships in data.",
             "Clustering can help identify groups in the data.",
             "Data science combines statistics and programming.",
             "Machine learning models can learn from data.",
             "Deep learning is a subset of machine learning.",
             "Neural networks are inspired by the human brain.",
             "Supervised learning uses labeled data.",
             "Unsupervised learning finds patterns in unlabeled data.",
             "Reinforcement learning learns through rewards and penalties.",
             "Natural language processing enables computers to understand human language.",
             "Computer vision allows machines to interpret visual data.",
             "Data visualization helps communicate insights effectively.",
             "Big data refers to large and complex datasets that require advanced tools for analysis.",
             "Artificial intelligence is transforming various industries.",
             "The future of technology is exciting and full of possibilities."]
    
    labels = [i for i in range(len(texts))]
    embeddings = np.array([ollama.embed_query(text) for text in texts])
    
    visualize_embeddings(embeddings, texts, labels, method='3D')

if __name__ == "__main__":
    main()