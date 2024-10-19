import csv
from google_play_scraper import app, reviews, Sort

def get_app_reviews(product_id, lang='id', country='id', num_reviews=100):
    result, _ = reviews(
        product_id,
        lang=lang,  
        country=country, 
        sort=Sort.NEWEST, 
        count=num_reviews  
    )
    return result

def get_app_name(product_id):
    result = app(product_id, lang='id', country='id')
    return result['title']  

def save_reviews_to_csv(reviews, filename, app_name, category):
    keys = ['appName', 'userName', 'reviews', 'rating', 'at', 'category']

    with open(filename, 'w', newline='', encoding='utf-8') as output_file:
        dict_writer = csv.DictWriter(output_file, fieldnames=keys)
        dict_writer.writeheader()  
        for review in reviews:
            filtered_review = {
                'appName': app_name,                              
                'userName': review.get('userName', '').strip(),    
                'reviews': review.get('content', '').strip(),     
                'rating': review.get('score', ''),                
                'at': review.get('at', ''),                        
                'category': category                               
            }
            dict_writer.writerow(filtered_review)  

product_id = 'com.lenovo.anyshare.gps'
category = 'Tools' 

app_name = get_app_name(product_id)
reviews = get_app_reviews(product_id)

if reviews:
    csv_filename = 'shareit_reviews.csv'
    save_reviews_to_csv(reviews, csv_filename, app_name, category)
    print(f"Ulasan berhasil disimpan ke {csv_filename}")
else:
    print("Tidak ada ulasan yang ditemukan untuk aplikasi ini.")