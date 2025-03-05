from flask import Flask, request, jsonify
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Sample Dataset
data = {'Video': ['Python Basics', 'Data Science', 'AI Introduction', 'Machine Learning', 'Deep Learning'],
        'Description': ['Learn Python for beginners', 'Data Science full course', 
                        'Introduction to AI', 'Machine Learning concepts', 'Deep Learning with TensorFlow']}

df = pd.DataFrame(data)

# Text Vectorization
cv = CountVectorizer(stop_words='english')
vectors = cv.fit_transform(df['Description'])
cosine_sim = cosine_similarity(vectors)

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.json['query']
    input_vector = cv.transform([user_input])
    similarities = cosine_similarity(input_vector, vectors)
    recommendations = df.iloc[similarities.argsort()[0][-3:][::-1]]
    return jsonify(recommendations['Video'].tolist())

if __name__ == '__main__':
    app.run(debug=True)
