import urllib.request
import json
import pandas as pd
import random

print("🚀 Fetching REAL E-Commerce Database (Strictly NO Duplicates)...")

# Fetch all unique products from the database
url = "https://dummyjson.com/products?limit=0"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

try:
    with urllib.request.urlopen(req) as response:
        raw_data = json.loads(response.read().decode())
        products = raw_data['products']
except Exception as e:
    print(f"Error fetching data: {e}")
    exit()

data = []

# Iterate ONLY through the unique products (No 2000 loop!)
for p in products:
    name = p['title']
    
    # Clean up missing brands by falling back to the category name
    brand = p.get('brand', p.get('category', 'Generic').capitalize())
    category = p.get('category', 'General')
    
    # Use the real database rating, generate realistic review counts
    rating = p.get('rating', round(random.uniform(3.5, 5.0), 1))
    reviews = random.randint(15, 3000)
    
    # The real, verified product image
    image_url = p['thumbnail']
    
    # Create rich text tags for your Machine Learning NLP engine
    tags = f"{category.lower()} {brand.lower()} {name.lower()}"
    
    data.append([name, brand, rating, reviews, image_url, tags])

# 1. Save the main dataset (Exactly ~194 highly unique, real products)
df = pd.DataFrame(data, columns=['Name', 'Brand', 'Rating', 'ReviewCount', 'ImageURL', 'Tags'])

# CRITICAL FIX: Drop any accidental duplicates just in case
df = df.drop_duplicates(subset=['Name', 'ImageURL'])

df.to_csv('models/clean_data.csv', index=False)
print(f"✅ models/clean_data.csv created! ({len(df)} Unique Real Products)")

# 2. Save the trending products (Top 8 most popular items)
trending_df = df.sort_values(by=['ReviewCount', 'Rating'], ascending=[False, False]).head(8)
trending_df.to_csv('models/trending_products.csv', index=False)
print("✅ models/trending_products.csv created! (Top 8 Trending)")

print("🔥 Done! The clone bug is fixed. Launch your app.")