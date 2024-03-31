import pandas as pd
from geopy.geocoders import Nominatim
from config import Config

# Import dataframe from data directory
df = pd.read_csv(Config.input_path, encoding=Config.encoding)
total_count = len(df)

# Set geocoder
geo = Nominatim(user_agent=Config.target_country)

for idx, row in df.iterrows():
    # Get address from df
    address = row[Config.address_field]

    if (idx == 5):
        break

    try:
        # Save latitude and longitude in dataframe
        response = geo.geocode(address)
        df.at[idx, Config.field_lat_name] = response.latitude
        df.at[idx, Config.field_lng_name] = response.longitude
        print(f"[{idx+1}/{total_count}]: get coordinate!")
        
    except:
        # Save missing data to dataframe
        df.at[idx, Config.field_lat_name] = Config.missing_value_lat
        df.at[idx, Config.field_lng_name] = Config.missing_value_lng
        print(f"[{idx+1}/{total_count}]: cannot get coordinate")

# Save dataframe to a csv file
df.to_csv(Config.output_path, index = False, encoding=Config.encoding)
    