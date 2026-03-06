import pandas as pd

def recommender(title, similarity_matrix,df, top_k = 5):
    idx = df[df["title"] == title].index[0]
    sim_scores = list(enumerate(similarity_matrix(idx)))
    sim_scores = sorted(sim_scores, key=lambda x:x[1], reverse=True)
    sim_scores = sim_scores(1, top_k+1)
    results = []

    for i,scores in sim_scores:
        results.append(df["title"].iloc[i],scores)
    return results