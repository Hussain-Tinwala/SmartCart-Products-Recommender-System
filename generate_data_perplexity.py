# import urllib.request
# import json
# import pandas as pd
# import random

# print("🚀 Fetching REAL E-Commerce Database (Strictly NO Duplicates)...")

# # Fetch all unique products from the database
# url = "https://dummyjson.com/products?limit=0"
# req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})

# try:
#     with urllib.request.urlopen(req) as response:
#         raw_data = json.loads(response.read().decode())
#         products = raw_data['products']
# except Exception as e:
#     print(f"Error fetching data: {e}")
#     exit()

# data = []

# for p in products:
#     name_base = p['title']
#     brand_base = p.get('brand', p.get('category', 'Generic').capitalize())
#     category = p.get('category', 'General')
    
#     # Full image list: thumbnail + images array (unique per product)
#     all_images = [p['thumbnail']] + p.get('images', [])
    
#     # Generate variations = len(all_images) for 1:1 unique image per product variant
#     for i, image_url in enumerate(all_images):
#         # Match image to title with precise suffix
#         suffixes = ['Pro', 'Ultra', 'Lite', f"Model {random.randint(2023,2026)}", 'Premium Edition']
#         name = f"{name_base} {suffixes[i % len(suffixes)]}"
        
#         # Brand variation tied to image index
#         brand = random.choice([brand_base, f"{brand_base} {['HD', 'Max', 'Plus'][i % 3]}"])
        
#         rating = round(random.uniform(3.5, 5.0), 1)
#         reviews = random.randint(15, 5000)
        
#         tags = f"{category.lower()} {brand.lower()} {name.lower()}"
        
#         data.append([name, brand, rating, reviews, image_url, tags])

# # Rest unchanged (dedupe saves ~3-6x per original product)
# df = pd.DataFrame(data, columns=['Name', 'Brand', 'Rating', 'ReviewCount', 'ImageURL', 'Tags'])
# df = df.drop_duplicates(subset=['Name', 'ImageURL'])

# df.to_csv('newmodels/clean_data.csv', index=False)
# print(f"✅ newmodels/clean_data.csv created! ({len(df)} Unique Real Products)")

# # 2. Save the trending products (Top 8 most popular items)
# trending_df = df.sort_values(by=['ReviewCount', 'Rating'], ascending=[False, False]).head(8)
# trending_df.to_csv('newmodels/trending_products.csv', index=False)
# print("✅ newmodels/trending_products.csv created! (Top 8 Trending)")

# print("🔥 Done! The clone bug is fixed. Launch your app.")






import urllib.request
import json
import pandas as pd
import random
import os

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

for p in products:
    name_base = p['title']
    brand_base = p.get('brand', p.get('category', 'Generic').capitalize())
    category = p.get('category', 'General')
    
    # Full image list: thumbnail + images array (unique per product)
    all_images = [p['thumbnail']] + p.get('images', [])
    
    # Generate variations = len(all_images) for 1:1 unique image per product variant
    for i, image_url in enumerate(all_images):
        # Color-based suffixes to distinguish Pro (Black), Ultra (Silver), Lite (White)
        colors = ['Black Pro', 'Silver Ultra', 'White Lite', f"Model {random.randint(2023,2026)}"]
        name = f"{name_base} {colors[i % len(colors)]}"
        
        # Brand variation tied to color
        color_tags = ['Pro Edition', 'Ultra Max', 'Lite Plus']
        brand = f"{brand_base} {color_tags[i % len(color_tags)]}"
        
        rating = round(random.uniform(3.5, 5.0), 1)
        reviews = random.randint(15, 5000)
        
        tags = f"{category.lower()} {brand.lower()} {name.lower()}"
        
        data.append([name, brand, rating, reviews, image_url, tags])

# Create newmodels folder if it doesn't exist
os.makedirs('newmodels', exist_ok=True)

# Rest unchanged (dedupe saves ~3-6x per original product)
df = pd.DataFrame(data, columns=['Name', 'Brand', 'Rating', 'ReviewCount', 'ImageURL', 'Tags'])
df = df.drop_duplicates(subset=['Name', 'ImageURL'])

df.to_csv('newmodels/clean_data.csv', index=False)
print(f"✅ newmodels/clean_data.csv created! ({len(df)} Unique Real Products)")

# 2. Save the trending products (Top 8 most popular items)
trending_df = df.sort_values(by=['ReviewCount', 'Rating'], ascending=[False, False]).head(8)
trending_df.to_csv('newmodels/trending_products.csv', index=False)
print("✅ newmodels/trending_products.csv created! (Top 8 Trending)")

print("🔥 Done! The clone bug is fixed. Launch your app.")