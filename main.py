import pandas as pd
import numpy as np
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_data(file_path):
    """Load dataset and preprocess text data."""
    df = pd.read_csv(file_path)
    df = df[['title', 'plot']].dropna()
    return df

def preprocess_and_vectorize(df):
    """Convert text data into TF-IDF vectors."""
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(df['plot'])
    return vectorizer, tfidf_matrix

def recommend(query, vectorizer, tfidf_matrix, df, top_n=5):
    """Recommend top N similar movies based on query."""
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, tfidf_matrix).flatten()
    top_indices = np.argsort(similarities)[-top_n:][::-1]
    return df.iloc[top_indices][['title', 'plot']]

def main():
    """Main function to handle command-line execution."""
    parser = argparse.ArgumentParser()
    parser.add_argument('query', type=str, help='User query for movie recommendation')
    args = parser.parse_args()
    
    file_path = "data/movies_initial.csv"
    df = load_data(file_path)
    vectorizer, tfidf_matrix = preprocess_and_vectorize(df)
    recommendations = recommend(args.query, vectorizer, tfidf_matrix, df)
    print(recommendations)

if __name__ == "__main__":
    main()
