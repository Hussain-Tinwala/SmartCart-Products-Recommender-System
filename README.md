# SmartCart - AI Product Recommendation Engine

> **Live Demo:** https://smartcart-chcf.onrender.com/

## Overview
SmartCart is an intelligent, content-based e-commerce recommendation engine. Instead of relying on generic product tags or basic SQL queries, it leverages Natural Language Processing (NLP) to understand product attributes and calculate similarity scores. This allows the system to serve highly accurate, personalized product recommendations in real-time.

The frontend features a modern, responsive Glassmorphism UI, designed to replicate the feel of a premium, enterprise-level web application.

## Core Features
* **Machine Learning Engine:** Utilizes TF-IDF (Term Frequency-Inverse Document Frequency) vectorization to process text data.
* **Predictive Matching:** Implements Cosine Similarity to mathematically compute and rank the closest product matches based on multi-dimensional feature vectors.
* **Fuzzy Search Handling:** Case-insensitive, partial-match querying allows the engine to route generic user searches (e.g., "lotion") to specific product datasets.
* **Premium UI/UX:** Built with a custom Glassmorphism design system, featuring fluid CSS animations, dynamic hover states, and a clean layout.
* **Stateless Architecture:** Designed for rapid deployment and horizontal scaling without database bottlenecks.

## Tech Stack
* **Backend:** Python 3, Flask, Gunicorn
* **Machine Learning:** Scikit-Learn, Pandas, NumPy
* **Frontend:** HTML5, CSS3, Bootstrap 4, Jinja2 Templating
* **Deployment:** Render 

## How It Works (Under the Hood)
The recommendation engine operates purely on content-based filtering:
1. **Data Ingestion:** Loads a pre-cleaned dataset of e-commerce products containing features like Name, Brand, Rating, and a combined `Tags` string.
2. **Text Vectorization:** The `TfidfVectorizer` converts the unstructured `Tags` data into a matrix of TF-IDF features, filtering out common English stop words.
3. **Similarity Matrix:** The `cosine_similarity` function calculates the angle between the multi-dimensional vectors. A score closer to 1 indicates a higher contextual match.
4. **Ranking & Retrieval:** The algorithm sorts the similarity scores in descending order, strips out the queried item itself, and returns the top *N* items to the frontend.

## Installation & Local Setup

To run this application on your local machine:

**1. Clone the repository:**
```bash
git clone [https://github.com/Hussain-Tinwala/SmartCart-Products-Recommender-System.git](https://github.com/Hussain-Tinwala/SmartCart-Products-Recommender-System.git)
cd smartcart-ai-recommender
```

**2. Create a virtual environment:**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install the dependencies:**
```bash
pip install -r requirements.txt
```

**4. Run the Flask application:**
```bash
python app.py
```
   
**5. Access the app:**
Open your browser and navigate to `http://127.0.0.1:5000`

## Project Structure
```text
smartcart-ai-recommender/
│
├── models/
│   ├── clean_data.csv          # Main dataset for vectorization
│   └── trending_products.csv   # Dataset for the homepage trending section
│
├── static/
│   ├── img/                    # Product placeholder images
│   └── v.mp4                   # Hero section background video
│
├── templates/
│   ├── index.html              # Landing page UI
│   └── main.html               # Search and recommendation engine UI
│
├── app.py                      # Core Flask application and ML routing
├── requirements.txt            # Python dependencies
└── README.md                   # Project documentation
```

## Future Enhancements
* Implement Collaborative Filtering to combine user behavior with the existing content-based model.
* Integrate a real-time database (PostgreSQL/MongoDB) for persistent user authentication and cart management.
* Deploy a containerized version using Docker.

---