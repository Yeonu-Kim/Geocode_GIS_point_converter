class Config:
    input_path = './data/seocho_edu.csv'
    output_path = './output/test.csv'

    target_country = 'South Korea' # Set geocoding country to South Korea
    encoding = 'cp949' # Set encoding cp949 (Window-kr)
    address_field = '도로명주소'

    field_lat_name = 'latitude'
    field_lng_name = 'longitude'

    missing_value_lat = 0.0
    missing_value_lng = 0.0