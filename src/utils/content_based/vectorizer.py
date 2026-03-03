from sklearn.feature_extraction.text import TfidfVectorizer

def create_tfidf_matrix(text_series, max_features = 5000):
    vectorizer = TfidfVectorizer(max_features = max_features, stop_words = "english")
    tfidf_matrix = vectorizer.fit_transform(text_series)
    return tfidf_matrix,vectorizer
