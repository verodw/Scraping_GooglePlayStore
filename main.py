# import os
# import csv
# from serpapi import GoogleSearch

# api_key = "cded61d8f992be4e32cab99cc033254434d29217e5ade46f50179749e2b4bad6"

# print(f"Using API key: {api_key}")

# # Fungsi untuk mendapatkan rekomendasi aplikasi
# def get_app_recommendations(num_results=100):
#     params = {
#         "engine": "google_play",
#         "store": "apps",
#         "api_key": api_key,
#         "hl": "en",  # Set language to Indonesian
#         "gl": "id",  # Set location to Indonesia
#         "num": num_results
#     }

#     search = GoogleSearch(params)
#     results = search.get_dict()

#     # Debug: print hasil dari API
#     print(f"Results from SerpAPI: {results}")

#     if 'error' in results:
#         print(f"Error: {results['error']}")
#         return []

#     apps_data = []
#     # Ambil informasi dari hasil pencarian
#     for item in results.get('items_highlight', []):
#         for app in item:
#             app_data = {
#                 'title': app.get('title'),
#                 'link': app.get('link'),
#                 'subtitle': app.get('subtitle'),
#                 'product_id': app.get('product_id'),
#                 'thumbnail': app.get('thumbnail')
#             }
            
#             # Mendapatkan ulasan untuk aplikasi
#             app_reviews = get_app_reviews(app.get('product_id'))
#             app_data['reviews'] = app_reviews
            
#             apps_data.append(app_data)

#     return apps_data

# # Fungsi untuk mengambil ulasan aplikasi berdasarkan product_id
# def get_app_reviews(product_id, num_reviews=100):
#     params = {
#         "engine": "google_play_product",
#         "product_id": product_id,
#         "api_key": api_key,
#         "hl": "en",
#         "gl": "id",
#         "num": num_reviews
#     }

#     search = GoogleSearch(params)
#     results = search.get_dict()

#     reviews_data = []
#     for review in results.get('reviews', []):
#         review_data = {
#             'user_name': review.get('user_name'),
#             'rating': review.get('rating'),
#             'text': review.get('text'),
#             'date': review.get('date'),
#             'product_id': product_id  # Add product_id to link review to app
#         }
#         reviews_data.append(review_data)

#     return reviews_data

# # Fungsi untuk menyimpan data ke CSV
# def save_to_csv(data, filename):
#     if not data:
#         print("No data to save.")
#         return
#     keys = data[0].keys()  # Ambil header dari data pertama
#     with open(filename, 'w', newline='', encoding='utf-8') as output_file:
#         dict_writer = csv.DictWriter(output_file, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(data)

# # Eksekusi scraping rekomendasi aplikasi dan ulasan
# print("Fetching app recommendations...")
# recommended_apps = get_app_recommendations(num_results=10)  # Mengambil 10 aplikasi dulu untuk uji coba

# # Buat direktori jika belum ada
# save_dir = os.path.expanduser("~/Documents/Scraping-GooglePlayStore")
# os.makedirs(save_dir, exist_ok=True)

# # Simpan rekomendasi aplikasi ke CSV
# csv_filename = os.path.join(save_dir, 'recommended_apps.csv')
# save_to_csv(recommended_apps, csv_filename)

# # Kumpulkan semua ulasan dari semua aplikasi ke dalam satu list
# all_reviews = []
# for app in recommended_apps:
#     for review in app['reviews']:
#         all_reviews.append(review)

# # Simpan semua ulasan ke CSV terpisah
# reviews_csv_filename = os.path.join(save_dir, 'app_reviews.csv')
# save_to_csv(all_reviews, reviews_csv_filename)

# print(f"Recommendations saved to {csv_filename}")
# print(f"User reviews saved to {reviews_csv_filename}")







# import os
# import csv
# from serpapi import GoogleSearch

# api_key = "cded61d8f992be4e32cab99cc033254434d29217e5ade46f50179749e2b4bad6"

# print(f"Using API key: {api_key}")

# # Fungsi untuk mendapatkan rekomendasi aplikasi
# def get_app_recommendations(num_results=100):
#     params = {
#         "engine": "google_play",
#         "store": "apps",
#         "api_key": api_key,
#         "hl": "en",  # Set language to Indonesian
#         "gl": "id",  # Set location to Indonesia
#         "num": num_results
#     }

#     search = GoogleSearch(params)
#     results = search.get_dict()

#     # Debug: print hasil dari API
#     print(f"Results from SerpAPI: {results}")

#     if 'error' in results:
#         print(f"Error: {results['error']}")
#         return []

#     apps_data = []
#     # Ambil informasi dari hasil pencarian
#     for item in results.get('items_highlight', []):
#         for app in item:
#             product_id = app.get('product_id')
#             if product_id:  # Pastikan product_id ada
#                 app_data = {
#                     'title': app.get('title'),
#                     'link': app.get('link'),
#                     'subtitle': app.get('subtitle'),
#                     'product_id': product_id,
#                     'thumbnail': app.get('thumbnail')
#                 }
                
#                 # Mendapatkan ulasan untuk aplikasi
#                 app_reviews = get_app_reviews(product_id)
#                 app_data['reviews'] = app_reviews
                
#                 apps_data.append(app_data)
#             else:
#                 print(f"Skipping app without product_id: {app.get('title')}")

#     return apps_data

# # Fungsi untuk mengambil ulasan aplikasi berdasarkan product_id
# def get_app_reviews(product_id, num_reviews=100):
#     params = {
#         "engine": "google_play_product",
#         "product_id": product_id,
#         "api_key": api_key,
#         "hl": "en",
#         "gl": "id",
#         "num": num_reviews
#     }

#     search = GoogleSearch(params)
#     results = search.get_dict()

#     reviews_data = []
#     for review in results.get('reviews', []):
#         review_data = {
#             'user_name': review.get('user_name'),
#             'rating': review.get('rating'),
#             'text': review.get('text'),
#             'date': review.get('date'),
#             'product_id': product_id  # Add product_id to link review to app
#         }
#         reviews_data.append(review_data)

#     return reviews_data

# # Fungsi untuk menyimpan data ke CSV
# def save_to_csv(data, filename):
#     if not data:
#         print("No data to save.")
#         return
#     keys = data[0].keys()  # Ambil header dari data pertama
#     with open(filename, 'w', newline='', encoding='utf-8') as output_file:
#         dict_writer = csv.DictWriter(output_file, keys)
#         dict_writer.writeheader()
#         dict_writer.writerows(data)

# # Eksekusi scraping rekomendasi aplikasi dan ulasan
# print("Fetching app recommendations...")
# recommended_apps = get_app_recommendations(num_results=10)  # Mengambil 10 aplikasi dulu untuk uji coba

# # Buat direktori jika belum ada
# save_dir = os.path.expanduser("~/Documents/Scraping-GooglePlayStore")
# os.makedirs(save_dir, exist_ok=True)

# # Simpan rekomendasi aplikasi ke CSV
# csv_filename = os.path.join(save_dir, 'recommended_apps_new.csv')
# save_to_csv(recommended_apps, csv_filename)

# # Kumpulkan semua ulasan dari semua aplikasi ke dalam satu list
# all_reviews = []
# for app in recommended_apps:
#     for review in app['reviews']:
#         all_reviews.append(review)

# # Simpan semua ulasan ke CSV terpisah
# reviews_csv_filename = os.path.join(save_dir, 'app_reviews.csv')
# save_to_csv(all_reviews, reviews_csv_filename)

# print(f"Recommendations saved to {csv_filename}")
# print(f"User reviews saved to {reviews_csv_filename}")



import os
import csv
from serpapi import GoogleSearch

api_key = "cded61d8f992be4e32cab99cc033254434d29217e5ade46f50179749e2b4bad6"

print(f"Using API key: {api_key}")

# Fungsi untuk mendapatkan rekomendasi aplikasi
def get_app_recommendations(num_results=100, max_pages=5):
    apps_data = []
    seen_product_ids = set()  # Set untuk melacak product_id yang sudah ditambahkan

    for page in range(max_pages):
        params = {
            "engine": "google_play",
            "store": "apps",
            "api_key": api_key,
            "hl": "en",
            "gl": "id",
            "num": num_results,
            "start": page * num_results  # Menggunakan offset untuk paginasi
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        # Debug: print hasil dari API
        print(f"Results from SerpAPI (Page {page + 1}): {results}")

        if 'error' in results:
            print(f"Error: {results['error']}")
            break

        # Ambil informasi dari hasil pencarian
        for item in results.get('items_highlight', []):
            for app in item:
                product_id = app.get('product_id')
                if product_id and product_id not in seen_product_ids:  # Pastikan product_id ada dan belum ditambahkan
                    app_data = {
                        'title': app.get('title'),
                        'link': app.get('link'),
                        'subtitle': app.get('subtitle'),
                        'product_id': product_id,
                        'thumbnail': app.get('thumbnail')
                    }
                    
                    # Mendapatkan ulasan untuk aplikasi
                    app_reviews = get_app_reviews(product_id)
                    
                    if app_reviews:  # Jika ada ulasan, tambahkan ke data
                        app_data['reviews'] = app_reviews
                    
                    apps_data.append(app_data)
                    seen_product_ids.add(product_id)  # Tambahkan product_id ke set
                else:
                    print(f"Skipping app without product_id or already seen: {app.get('title')}")

    return apps_data

# Fungsi untuk mengambil ulasan aplikasi berdasarkan product_id
def get_app_reviews(product_id, num_reviews=100):
    params = {
        "engine": "google_play_product",
        "product_id": product_id,
        "api_key": api_key,
        "hl": "en",
        "gl": "id",
        "num": num_reviews
    }

    search = GoogleSearch(params)
    results = search.get_dict()

    reviews_data = []
    for review in results.get('reviews', []):
        review_data = {
            'user_name': review.get('user_name'),
            'rating': review.get('rating'),
            'text': review.get('text'),
            'date': review.get('date'),
            'product_id': product_id  # Add product_id to link review to app
        }
        reviews_data.append(review_data)

    return reviews_data

# Fungsi untuk menyimpan data ke CSV
def save_to_csv(data, filename):
    if not data:
        print("No data to save.")
        return
    keys = data[0].keys()  # Ambil header dari data pertama
    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)

# Eksekusi scraping rekomendasi aplikasi dan ulasan
print("Fetching app recommendations...")
recommended_apps = get_app_recommendations(num_results=20, max_pages=5)  # Mengambil lebih banyak aplikasi

# Buat direktori jika belum ada
save_dir = os.path.expanduser("~/Documents/Scraping-GooglePlayStore")
os.makedirs(save_dir, exist_ok=True)

# Simpan rekomendasi aplikasi ke CSV
csv_filename = os.path.join(save_dir, 'apps.csv')
save_to_csv(recommended_apps, csv_filename)

# Kumpulkan semua ulasan dari semua aplikasi ke dalam satu list
all_reviews = []
for app in recommended_apps:
    if 'reviews' in app:  # Cek apakah ada ulasan untuk aplikasi ini
        for review in app['reviews']:
            all_reviews.append(review)

# Simpan semua ulasan ke CSV terpisah
reviews_csv_filename = os.path.join(save_dir, 'app_reviews.csv')
save_to_csv(all_reviews, reviews_csv_filename)

print(f"Recommendations saved to {csv_filename}")
print(f"User reviews saved to {reviews_csv_filename}")



