# Movie data (Pure Python)
movies = {
    "Avatar": ["Action", "Adventure", "SciFi"],
    "Titanic": ["Romance", "Drama"],
    "Avengers": ["Action", "Superhero"],
    "Iron Man": ["Action", "SciFi", "Superhero"],
    "Interstellar": ["SciFi", "Space", "Drama"]
}

def recommend(movie_name):
    if movie_name not in movies:
        print("Movie not found!")
        return

    target_genres = movies[movie_name]
    scores = {}

    for movie, genres in movies.items():
        if movie == movie_name:
            continue
        common = len(set(target_genres) & set(genres))
        scores[movie] = common

    # Sort by similarity
    recommended = sorted(scores.items(), key=lambda x: x[1], reverse=True)

    print(f"Because you liked '{movie_name}', you may also like:")
    for movie, score in recommended[:3]:
        if score > 0:
            print("👉", movie)

# Run
recommend("Avatar")
