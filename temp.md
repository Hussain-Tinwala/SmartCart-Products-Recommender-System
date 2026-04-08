SmartPhones
Shoes
Watch
laptop
Bags








To fix this—and to give you the perfect "Hybrid Recommender System" answer for your professor—we are going to implement a Weighted Bayesian Average.

Here is what the new logic does:

The NLP Content Engine (TF-IDF): Finds items that match exactly what the user is looking at (Shoes stay with Shoes).

The Collaborative Engine (Bayesian Score): It calculates a true "Popularity Score" by combining the Rating with the Number of Reviews. (This means a 4.8-star shoe with 3,000 reviews will now perfectly outrank a 5.0-star shoe with only 1 review).

The Hybrid Output: It mathematically combines both scores. This guarantees the search and trending pages strictly show the best products from top to bottom, and the product page strictly shows the closest matching items first.