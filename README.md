# Video-Recommendation-System
Video Recommendation System using NLP and Cosine Similarity
This project recommends videos based on user queries using Natural Language Processing (NLP) and Cosine Similarity.

Features

Text-Based Video Recommendation
Cosine Similarity Matching
NLP Preprocessing
API Integration with FastAPI
Postman Testing

Tech Stack

Python

FastAPI

Cosine Similarity

Postman

How to Run the Project

1. Clone the repository:

git clone https://github.com/swapnaGyabgonda/Video-Recommendation-System.git


2. Install dependencies:
pip install -r requirements.txt


3. Run the API:

uvicorn src.app:app --reload


4. Test with Postman using:

Endpoint: /recommend

Method: POST

Input:


{
  "query": "python tutorials"
}

Postman Collection

👉 Download collection from postman_collection.json
pip install -r requirements.txt
