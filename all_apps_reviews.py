import pandas as pd
import glob

path = "/Users/veronicadwiyanti/Documents/Scraping-GooglePlayStore/"
all_files = glob.glob(path + "*_reviews.csv")  

if not all_files:
    print("Tidak ada file CSV ditemukan dengan akhiran '_reviews.csv' di folder ini.")
else:
    print(f"File yang ditemukan: {all_files}")

dataframes = []

for filename in all_files:
    try:
        df = pd.read_csv(filename)  
        df['appName'] = filename.split('/')[-1].replace('_reviews.csv', '') 
        dataframes.append(df) 
        print(f"Berhasil membaca: {filename}")  
    except Exception as e:
        print(f"Gagal membaca {filename}: {e}")  

if dataframes:
    combined_df = pd.concat(dataframes, ignore_index=True)

    combined_df.to_csv('all_apps_reviews_combined.csv', index=False, encoding='utf-8')
    print("Semua ulasan berhasil digabungkan ke dalam all_apps_reviews_combined.csv")
else:
    print("Tidak ada DataFrame yang berhasil dibaca, tidak ada yang dapat digabungkan.")

