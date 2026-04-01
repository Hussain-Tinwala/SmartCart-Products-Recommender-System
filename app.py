# from flask import Flask, request, render_template
# import pandas as pd
# import random
# from flask_sqlalchemy import SQLAlchemy
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# app = Flask(__name__)

# # load files===========================================================================================================
# trending_products = pd.read_csv("models/trending_products.csv")
# train_data = pd.read_csv("models/clean_data.csv")

# # database configuration---------------------------------------
# app.secret_key = "alskdjfwoeieiurlskdjfslkdjf"
# app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://root:@localhost/productsrecommender"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# # Define your model class for the 'signup' table
# class Signup(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)

# # Define your model class for the 'signup' table
# class Signin(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(100), nullable=False)
#     password = db.Column(db.String(100), nullable=False)


# # Recommendations functions============================================================================================
# # Function to truncate product name
# def truncate(text, length):
#     if len(text) > length:
#         return text[:length] + "..."
#     else:
#         return text


# # def content_based_recommendations(train_data, item_name, top_n=10):
# #     # Check if the item name exists in the training data
# #     if item_name not in train_data['Name'].values:
# #         print(f"Item '{item_name}' not found in the training data.")
# #         return pd.DataFrame()

# #     # Create a TF-IDF vectorizer for item descriptions
# #     tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# #     # Apply TF-IDF vectorization to item descriptions
# #     tfidf_matrix_content = tfidf_vectorizer.fit_transform(train_data['Tags'])

# #     # Calculate cosine similarity between items based on descriptions
# #     cosine_similarities_content = cosine_similarity(tfidf_matrix_content, tfidf_matrix_content)

# #     # Find the index of the item
# #     item_index = train_data[train_data['Name'] == item_name].index[0]

# #     # Get the cosine similarity scores for the item
# #     similar_items = list(enumerate(cosine_similarities_content[item_index]))

# #     # Sort similar items by similarity score in descending order
# #     similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)

# #     # Get the top N most similar items (excluding the item itself)
# #     top_similar_items = similar_items[1:top_n+1]

# #     # Get the indices of the top similar items
# #     recommended_item_indices = [x[0] for x in top_similar_items]

# #     # Get the details of the top similar items
# #     recommended_items_details = train_data.iloc[recommended_item_indices][['Name', 'ReviewCount', 'Brand', 'ImageURL', 'Rating']]

# #     return recommended_items_details

# def content_based_recommendations(train_data, item_name, top_n=10):
#     # 1. Convert search query to lowercase for a case-insensitive search
#     search_query = str(item_name).lower()

#     # 2. Find any product names that contain the search query
#     matches = train_data[train_data['Name'].str.lower().str.contains(search_query, na=False)]

#     # 3. Check if we found any matches
#     if matches.empty:
#         print(f"Item containing '{item_name}' not found in the training data.")
#         return pd.DataFrame()

#     # 4. Grab the exact name of the first product that matched the search
#     exact_item_name = matches.iloc[0]['Name']
#     print(f"Matched user search '{item_name}' to product: '{exact_item_name}'")

#     # Create a TF-IDF vectorizer for item descriptions
#     tfidf_vectorizer = TfidfVectorizer(stop_words='english')

#     # Apply TF-IDF vectorization to item descriptions
#     tfidf_matrix_content = tfidf_vectorizer.fit_transform(train_data['Tags'])

#     # Calculate cosine similarity between items based on descriptions
#     cosine_similarities_content = cosine_similarity(tfidf_matrix_content, tfidf_matrix_content)

#     # Find the index of our matched item
#     item_index = train_data[train_data['Name'] == exact_item_name].index[0]

#     # Get the cosine similarity scores for the item
#     similar_items = list(enumerate(cosine_similarities_content[item_index]))

#     # Sort similar items by similarity score in descending order
#     similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)

#     # Get the top N most similar items (excluding the item itself)
#     top_similar_items = similar_items[1:top_n+1]

#     # Get the indices of the top similar items
#     recommended_item_indices = [x[0] for x in top_similar_items]

#     # Get the details of the top similar items
#     recommended_items_details = train_data.iloc[recommended_item_indices][['Name', 'ReviewCount', 'Brand', 'ImageURL', 'Rating']]

#     return recommended_items_details


# # routes===============================================================================
# # List of predefined image URLs
# random_image_urls = [
#     "static/img/img_1.png",
#     "static/img/img_2.png",
#     "static/img/img_3.png",
#     "static/img/img_4.png",
#     "static/img/img_5.png",
#     "static/img/img_6.png",
#     "static/img/img_7.png",
#     "static/img/img_8.png",
# ]


# @app.route("/")
# def index():
#     # Create a list of random image URLs for each product
#     random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
#     price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
#     return render_template('index.html',trending_products=trending_products.head(8),truncate = truncate,
#                            random_product_image_urls=random_product_image_urls,
#                            random_price = random.choice(price))

# @app.route("/main")
# def main():
#     return render_template('main.html')

# # routes
# @app.route("/index")
# def indexredirect():
#     # Create a list of random image URLs for each product
#     random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
#     price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
#     return render_template('index.html', trending_products=trending_products.head(8), truncate=truncate,
#                            random_product_image_urls=random_product_image_urls,
#                            random_price=random.choice(price))

# @app.route("/signup", methods=['POST','GET'])
# def signup():
#     if request.method=='POST':
#         username = request.form['username']
#         email = request.form['email']
#         password = request.form['password']

#         new_signup = Signup(username=username, email=email, password=password)
#         db.session.add(new_signup)
#         db.session.commit()

#         # Create a list of random image URLs for each product
#         random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
#         price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
#         return render_template('index.html', trending_products=trending_products.head(8), truncate=truncate,
#                                random_product_image_urls=random_product_image_urls, random_price=random.choice(price),
#                                signup_message='User signed up successfully!'
#                                )

# # Route for signup page
# @app.route('/signin', methods=['POST', 'GET'])
# def signin():
#     if request.method == 'POST':
#         username = request.form['signinUsername']
#         password = request.form['signinPassword']
#         new_signup = Signin(username=username,password=password)
#         db.session.add(new_signup)
#         db.session.commit()

#         # Create a list of random image URLs for each product
#         random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
#         price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
#         return render_template('index.html', trending_products=trending_products.head(8), truncate=truncate,
#                                random_product_image_urls=random_product_image_urls, random_price=random.choice(price),
#                                signup_message='User signed in successfully!'
#                                )
# @app.route("/recommendations", methods=['POST', 'GET'])
# def recommendations():
#     if request.method == 'POST':
#         prod = request.form.get('prod')
#         nbr = int(request.form.get('nbr'))
#         content_based_rec = content_based_recommendations(train_data, prod, top_n=nbr)

#         if content_based_rec.empty:
#             message = "No recommendations available for this product."
#             return render_template('main.html', message=message)
#         else:
#             # Create a list of random image URLs for each recommended product
#             random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
#             print(content_based_rec)
#             print(random_product_image_urls)

#             price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
#             return render_template('main.html', content_based_rec=content_based_rec, truncate=truncate,
#                                    random_product_image_urls=random_product_image_urls,
#                                    random_price=random.choice(price))


# if __name__=='__main__':
#     app.run(debug=True)




from flask import Flask, request, render_template
import pandas as pd
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# load files===========================================================================================================
trending_products = pd.read_csv("models/trending_products.csv")
train_data = pd.read_csv("models/clean_data.csv")

# Recommendations functions============================================================================================
def truncate(text, length):
    if len(text) > length:
        return text[:length] + "..."
    else:
        return text

def content_based_recommendations(train_data, item_name, top_n=10):
    search_query = str(item_name).lower()
    matches = train_data[train_data['Name'].str.lower().str.contains(search_query, na=False)]

    if matches.empty:
        return pd.DataFrame()

    exact_item_name = matches.iloc[0]['Name']

    tfidf_vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix_content = tfidf_vectorizer.fit_transform(train_data['Tags'])

    cosine_similarities_content = cosine_similarity(tfidf_matrix_content, tfidf_matrix_content)
    item_index = train_data[train_data['Name'] == exact_item_name].index[0]

    similar_items = list(enumerate(cosine_similarities_content[item_index]))
    similar_items = sorted(similar_items, key=lambda x: x[1], reverse=True)
    top_similar_items = similar_items[1:top_n+1]
    
    recommended_item_indices = [x[0] for x in top_similar_items]
    recommended_items_details = train_data.iloc[recommended_item_indices][['Name', 'ReviewCount', 'Brand', 'ImageURL', 'Rating']]

    return recommended_items_details

# routes===============================================================================
random_image_urls = [
    "static/img/img_1.png", "static/img/img_2.png", "static/img/img_3.png",
    "static/img/img_4.png", "static/img/img_5.png", "static/img/img_6.png",
    "static/img/img_7.png", "static/img/img_8.png",
]

@app.route("/")
@app.route("/index")
def index():
    random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
    price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
    return render_template('index.html', trending_products=trending_products.head(8), truncate=truncate,
                           random_product_image_urls=random_product_image_urls,
                           random_price=random.choice(price))

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        # Just grab the username to personalize the fake success message
        username = request.form.get('username')
        
        random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
        price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
        
        return render_template('index.html', trending_products=trending_products.head(8), truncate=truncate,
                               random_product_image_urls=random_product_image_urls, random_price=random.choice(price),
                               signup_message=f'Account created successfully for {username}!')
    
    return render_template('index.html')

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    if request.method == 'POST':
        # Same thing here, fake the login for the demo
        username = request.form.get('signinUsername')
        
        random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
        price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
        
        return render_template('index.html', trending_products=trending_products.head(8), truncate=truncate,
                               random_product_image_urls=random_product_image_urls, random_price=random.choice(price),
                               signup_message=f'Welcome back, {username}!')
                               
    return render_template('index.html')

@app.route("/recommendations", methods=['POST', 'GET'])
def recommendations():
    if request.method == 'POST':
        prod = request.form.get('prod')
        nbr = int(request.form.get('nbr'))
        content_based_rec = content_based_recommendations(train_data, prod, top_n=nbr)

        if content_based_rec.empty:
            message = "No recommendations available for this product."
            return render_template('main.html', message=message)
        else:
            random_product_image_urls = [random.choice(random_image_urls) for _ in range(len(trending_products))]
            price = [40, 50, 60, 70, 100, 122, 106, 50, 30, 50]
            return render_template('main.html', content_based_rec=content_based_rec, truncate=truncate,
                                   random_product_image_urls=random_product_image_urls,
                                   random_price=random.choice(price))
                                   
    return render_template('main.html')

if __name__=='__main__':
    # Turned off debug mode and bound to 0.0.0.0 so the cloud server can actually expose it to the web
    app.run(debug=False, host='0.0.0.0')