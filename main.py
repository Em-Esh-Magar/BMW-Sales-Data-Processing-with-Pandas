import pandas as pd
from datetime import datetime as dt


def Vehicle_Age_Category(age):
    if age == 0:
        return 'Brand New'
    elif age <= 2:
        return 'Like New'
    elif age <= 5:
        return 'Recent'
    elif age <= 8:
        return 'Used'
    elif age <= 12:
        return 'Older'
    else:
        return 'Classic'
    
    
def Price_Category(price):
    if price <= 50000:
        return "Budget"
    elif price <= 100000:
        return "Mid Budget"
    else:
        return "Premium"


def Collection_Category(collection):
    if collection > 800:
        return "Very High Profit"
    elif collection > 500:
        return "High Profit"
    elif collection > 100:
        return "Profit"
    else:
        return "Low Profit"
    
def Engine(engine):
    if engine <= 2.5:
        return "Small"
    elif engine <=3.5:
        return "Medium"
    else:
        return "Large"

# Extract Data
def extract_data():

    data = pd.read_csv("D:\ETL Practise\BMW\BMW-Sales-Data-Processing-with-Pandas\BMW sales data.csv")

    print(data.head())
    print(data.describe())
    print(data.info())
    print(data.shape)
    return data



# Transform Data starts from here

def transform_data(data):
# Checking if my datasets has nan value by shape
    a = data.dropna()
    print(data.shape)


    # Total missing values per column
    print("Missing values per column:")
    print(data.isnull().sum())


    # Checking if there are duplicates data or not
    duplicates_data = data.drop_duplicates()
    print(f"Original data shape {data.shape} and after removing duplicates data {duplicates_data.shape}")


    # Convert to proper data types
    data['Year'] = data['Year'].astype('int32')
    data['Price_USD'] = data['Price_USD'].astype('float32')
    data['Mileage_KM'] = data['Mileage_KM'].astype('int32')
    data['Sales_Volume'] = data['Sales_Volume'].astype('int32')


    # Convert categorical columns
    categorical_cols = ['Model', 'Region', 'Color', 'Fuel_Type', 'Transmission', 'Sales_Classification']
    for col in categorical_cols:
        if col in data.columns:
            data[col] = data[col].astype('category')
            
    print(data.info())


    # Age of vehicle
    current_year = dt.now().year
    data["Vehicle_Age"] = current_year - data["Year"]
    # print(data.head())

    # Categorized the vehicle age 
    data["Age_Category"] = data["Vehicle_Age"].apply(Vehicle_Age_Category)
    # print(data.head())


    # Categorized as price 
    # print(data.Price_USD.describe())
    data["Price_Category"] = data["Price_USD"].apply(Price_Category)


    # Renaming the columns name
    data.rename(columns={'Mileage_KM':'Distance_Covered'})


    # creating a new columns which holds the total collection in terms of million
    data["Collection_Million"] = data['Price_USD'] * data['Sales_Volume'] / 1000000
    # print(data.head())
    # print(data.Collection_Million.describe())
    data["Collection_Category"] = data["Collection_Million"].apply(Collection_Category)
    # print(data.head())


    # Average km run per year 
    data['Avg KM'] = data['Mileage_KM'] / data['Vehicle_Age']


    # Engine category 
    print(data['Engine_Size_L'].describe())
    data['Engine_Size'] = data['Engine_Size_L'].apply(Engine)
    # print(data.head())


    data = data.drop(["Transmission",'Engine_Size_L','Mileage_KM','Price_USD','Sales_Volume'],axis=1)



    # Findings
    print("Collection Categoried with respect to Car Color: ")
    print(data.groupby('Color')['Collection_Category'].value_counts())

    print("Collection Categoried with respect to Car Model: ")
    print(data.groupby('Model')['Collection_Category'].value_counts())


    print("Model Categoried with respect to Car sales in Region: ")
    print(data.groupby('Region')['Model'].value_counts())


    print("Collection in Million with respect to Car Fuel Type: ")
    print(data.groupby('Fuel_Type')['Collection_Million'].max())


    print("Price Categorized with respect to Car Model: ")
    print(data.groupby('Model')['Price_Category'].value_counts())


    print("Engine Size Categorized with respect to Car Model: ")
    print(data.groupby('Model')['Engine_Size'].value_counts())


    print("Average Collection in Million by a Car Model: ")
    print(data.groupby('Model')['Collection_Million'].mean().round(2))

    return data


# Load Part 
def load_data(data):
    # On Excel File 
    data.to_excel("Transformed_Data.xlsx",index = False)
    data.to_csv("Transformed_Data.csv",index = False)


if __name__ == "__main__":
    raw_data = extract_data()
    cleaned_data = transform_data(raw_data)
    load_data(cleaned_data)