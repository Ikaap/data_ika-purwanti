import pandas as pd
import validators
import numpy as np
import matplotlib.pyplot as plt

def extract_data():
    data = pd.read_csv('praktikum/source/house_listings.csv')
    return data

def min_max_normalization(data):
    min_val = data.min()
    max_val = data.max()
    normalized_data = (data - min_val) / (max_val - min_val)
    return normalized_data

def transform_data(data):
    # Normalisasi Data
        
    data['price'] = data['price'].str.replace(' ', '')
    data['price'] = pd.to_numeric(data['price'])
    data['price_1m2'] = data['price_1m2'].str.replace(' ', '')
    price_1m2_values = pd.to_numeric(data['price_1m2'].str.extract(r'(\d+)')[0])
    
    price_normalized = min_max_normalization(data['price'])
    price_m2_normalized = min_max_normalization(price_1m2_values)
    
    data['price_normalized'] = price_normalized
    data['price_m2_normalized'] = price_m2_normalized
    
    # Encoding Data Kategorikal
    data['encode_category'] = data['category'].astype('category').cat.codes
    data['encode_title_deed'] = data['title_deed'].astype('category').cat.codes
    data['encode_repair'] = data['repair'].astype('category').cat.codes
    data['encode_mortgage'] = data['mortgage'].astype('category').cat.codes
    
    # Aggregasi Data 
    data_with_price = data.dropna(subset=['price'])
    aggregated_data = data_with_price.groupby(['room_number', 'category']).agg({'price': ['mean', 'median', lambda x: x.mode().values[0]]})
    aggregated_data.columns = ['average_price', 'median_price', 'mode_price']
    data = pd.merge(data, aggregated_data, on=['room_number', 'category'], how='left')
    
    # Missing value
    split_floor = data['floor'].str.split(' / ', expand=True)
    values_one = pd.to_numeric(split_floor[0], errors='coerce')
    values_two = pd.to_numeric(split_floor[1], errors='coerce')
    median_value_one = values_one.median()
    median_value_two = values_two.median()
    median_value_one_str = f"{median_value_one:.0f}" if not np.isnan(median_value_one) else ''
    median_value_two_str = f"{median_value_two:.0f}" if not np.isnan(median_value_two) else ''

    median_floor = f"{median_value_one_str} / {median_value_two_str}"
    data['floor_imputed'] = median_floor
    data.loc[data['floor'].notna(), 'floor_imputed'] = data['floor']
    
    area_values = pd.to_numeric(data['area'].str.extract(r'(\d+)')[0])
    area_mean = area_values.mean()
    
    data['area_after_imputation'] = data['area']
    data.loc[data['area_after_imputation'].isnull(), 'area_after_imputation'] = f"{int(area_mean)} m²"
    
    # Mengatasi Outlier
    Q1 = data['price'].quantile(0.25)
    Q3 = data['price'].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    data['status_outlier'] = 'Within Range'
    data['status_outlier'] = data['price'].apply(lambda x: 'Outlier' if (x < lower_bound or x > upper_bound) else 'Within Range')
    
    # Menjaga Integritas Data
    data['address'] = data['address'].astype(str).str.rstrip('.')
    data['check_invalid_address'] = ~data['address'].str.match(r'^[A-Za-z0-9\s]+[,.][\sA-Za-z0-9]+$')
    data['check_invalid_urls'] = ~data['url'].apply(lambda x: validators.url(x))
    
    data['invalid_address'] = data['address'][data['check_invalid_address']]
    data['address'] = data.apply(lambda row: None if row['check_invalid_address'] else row['address'], axis=1)
    data['url'] = data.apply(lambda row: None if row['check_invalid_urls'] else row['url'], axis=1)
    
    return data

def export_to_excel(data, filename):
    data.to_excel(filename, index=False)
    print(f"Data has been exported to {filename}")
import numpy as np
import matplotlib.pyplot as plt


def visualize_data_one(data, save_path=None):
    fig, axes = plt.subplots(3, 2, figsize=(20, 24))

    # Visualisasi Normalisasi Data
    axes[0, 0].hist(data['price_normalized'], bins=30, color='skyblue', alpha=0.7, label='Normalized Price')
    axes[0, 0].hist(data['price'], bins=30, color='orange', alpha=0.5, label='Original Price')
    axes[0, 0].set_title('Distribution of Normalized Price vs. Original Price')
    axes[0, 0].set_xlabel('Price')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].legend()
    axes[0, 0].grid(True)

    # Visualisasi Encoding Data Kategorikal - Category
    data['category'].value_counts().plot(kind='bar', ax=axes[0, 1], color='green')
    axes[0, 1].set_title('Distribution of Categories')
    axes[0, 1].set_xlabel('Category')
    axes[0, 1].set_ylabel('Count')
    axes[0, 1].tick_params(axis='x', rotation=45)
    axes[0, 1].grid(axis='y')

    # Visualisasi Encoding Data Kategorikal - Title Deed
    data['title_deed'].value_counts().plot(kind='bar', ax=axes[1, 0], color='green')
    axes[1, 0].set_title('Distribution of Title Deed')
    axes[1, 0].set_xlabel('Title Deed')
    axes[1, 0].set_ylabel('Count')
    axes[1, 0].tick_params(axis='x', rotation=45)
    axes[1, 0].grid(axis='y')

    # Visualisasi Encoding Data Kategorikal - Repair
    data['repair'].value_counts().plot(kind='bar', ax=axes[1, 1], color='green')
    axes[1, 1].set_title('Distribution of Repair')
    axes[1, 1].set_xlabel('Repair')
    axes[1, 1].set_ylabel('Count')
    axes[1, 1].tick_params(axis='x', rotation=45)
    axes[1, 1].grid(axis='y')

    # Visualisasi Encoding Data Kategorikal - Mortgage
    data['mortgage'].value_counts().plot(kind='bar', ax=axes[2, 0], color='green')
    axes[2, 0].set_title('Distribution of Mortgage')
    axes[2, 0].set_xlabel('Mortgage')
    axes[2, 0].set_ylabel('Count')
    axes[2, 0].tick_params(axis='x', rotation=45)
    axes[2, 0].grid(axis='y')

    # Visualisasi Aggregasi Data
    data_with_price = data.dropna(subset=['price'])
    aggregated_data = data_with_price.groupby(['room_number', 'category']).agg({'price': ['mean', 'median', lambda x: x.mode().values[0]]})
    aggregated_data.plot(kind='bar', ax=axes[2, 1])
    axes[2, 1].set_title('Aggregated Data by Room Number and Category')
    axes[2, 1].set_xlabel('Room Number, Category')
    axes[2, 1].set_ylabel('Price')
    axes[2, 1].tick_params(axis='x', rotation=45)
    axes[2, 1].grid(axis='y')
    
    plt.savefig(save_path)
    print("Successfully save visualization one!")

def visualize_data_two(data, save_path=None):
    fig, axes = plt.subplots(3, 2, figsize=(20, 24))

    # Visualisasi Missing Value
    missing_values = data.isnull().sum()
    missing_values.plot(kind='bar', ax=axes[0, 0], color='skyblue')
    axes[0, 0].set_title('Missing Values in Each Feature')
    axes[0, 0].set_xlabel('Features')
    axes[0, 0].set_ylabel('Count of Missing Values')
    axes[0, 0].tick_params(axis='x', rotation=45)
    axes[0, 0].grid(axis='y')

    # Visualisasi Outlier menggunakan Scatter Plot
    axes[0, 1].scatter(data.index, data['price'], alpha=0.5, color='orange')
    axes[0, 1].set_title('Scatter Plot of Price')
    axes[0, 1].set_xlabel('Index')
    axes[0, 1].set_ylabel('Price')
    axes[0, 1].grid(True)
    
    # Visualisasi Check Invalid Address vs. Valid Address
    data['address_status'] = np.where(data['check_invalid_address'], 'Invalid', 'Valid')
    data['address_status'].value_counts().plot(kind='bar', color=['skyblue', 'orange'], ax=axes[1, 0])
    axes[1, 0].set_title('Check Invalid Address vs. Valid Address')
    axes[1, 0].set_xlabel('Address Status')
    axes[1, 0].set_ylabel('Count')
    axes[1, 0].tick_params(axis='x', rotation=0)
    axes[1, 0].grid(axis='y')

    # Visualisasi Check Invalid URL vs. Valid URL
    data['url_status'] = np.where(data['check_invalid_urls'], 'Invalid', 'Valid')
    data['url_status'].value_counts().plot(kind='bar', color=['skyblue', 'orange'], ax=axes[1, 1])
    axes[1, 1].set_title('Check Invalid URL vs. Valid URL')
    axes[1, 1].set_xlabel('URL Status')
    axes[1, 1].set_ylabel('Count')
    axes[1, 1].tick_params(axis='x', rotation=0)
    axes[1, 1].grid(axis='y')

    # Visualisasi histogram untuk fitur 'price'
    axes[2, 0].hist(data['price'], bins=30, color='skyblue')
    axes[2, 0].set_title('Distribution of Prices')
    axes[2, 0].set_xlabel('Price')
    axes[2, 0].set_ylabel('Frequency')
    axes[2, 0].grid(True)

    # Visualisasi scatter plot untuk fitur 'area' dan 'price'
    data['area'] = data['area'].str.replace(' m²', '').astype(float)
    data['price'] = data['price'].astype(float)
    axes[2, 1].scatter(data['area'], data['price'], alpha=0.5, color='orange')
    axes[2, 1].set_title('Price vs. Area')
    axes[2, 1].set_xlabel('Area (m²)')
    axes[2, 1].set_ylabel('Price')
    axes[2, 1].grid(True)
    
    plt.savefig(save_path)
    print("Successfully save visualization two!")
    
def visualize_data_three(data, save_path=None):
    fig, ax = plt.subplots(figsize=(20, 24))
    
    # Visualisasi bar plot untuk fitur 'category' dan 'average_price'
    avg_price_by_category = data.groupby('category')['average_price'].mean().reset_index()
    ax.bar(avg_price_by_category['category'], avg_price_by_category['average_price'], color='green')
    ax.set_title('Average Price by Category')
    ax.set_xlabel('Category')
    ax.set_ylabel('Average Price')
    ax.tick_params(axis='x', rotation=45)
    ax.grid(axis='y')
    
    plt.savefig(save_path)
    print("Successfully save visualization three!")

if __name__ == "__main__":
    extracted_data = extract_data()
    transformed_data = transform_data(extracted_data)
    export_to_excel(transformed_data, 'praktikum/file/transformed_house_listings.xlsx')
    
    transformed_data_excel = pd.read_excel('praktikum/file/transformed_house_listings.xlsx')
    visualize_data_one(transformed_data_excel, save_path='screenshots/visualization_one.png')
    visualize_data_two(transformed_data_excel, save_path='screenshots/visualization_two.png')
    visualize_data_three(transformed_data_excel, save_path='screenshots/visualization_three.png')