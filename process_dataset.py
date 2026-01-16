import pandas as pd

# Load audio features CSV (from Kaggle)
df = pd.read_csv("features.csv")

# Clean columns
df = df[['name', 'artists', 'valence', 'energy', 'danceability']].dropna()

# Mood classification function
def classify_mood(valence, energy, danceability):
    if valence > 0.6 and energy > 0.6:
        return "happy"
    elif valence < 0.4 and energy < 0.4:
        return "sad"
    elif energy > 0.7:
        return "energetic"
    elif valence > 0.5 and energy < 0.4:
        return "calm"
    else:
        return "neutral"

# Apply mood classifier
df['mood'] = df.apply(lambda x: classify_mood(x['valence'], x['energy'], x['danceability']), axis=1)

# Save selected data
df[['name', 'artists', 'mood']].to_csv("mood_tracks.csv", index=False)
print("Mood tracks file created successfully.")
