import folium
import json
import pandas as pd

f = open(r'N03-190101_13_GML/N03-19_13_190101.geojson', 'r', encoding='utf-8_sig')
geojson = json.load(f)
f.close()

import pandas as pd
prod_df = pd.read_csv(r'input/tokyo.csv', dtype='object') 
prod_df.columns = ["A", "B", "C", "D", "E", "F"]
prod_df['F'] = prod_df['F'].astype('float')
prod_df['A'] = prod_df['A'].astype('str')
prod_df['A'] = prod_df['A'].str[:5]
map_center = [35.70049, 139.48025] 
m2 = folium.Map(location=map_center, tiles='https://cyberjapandata.gsi.go.jp/xyz/blank/{z}/{x}/{y}.png', attr='国土地理院 白地図', zoom_start=11)

folium.Choropleth(
    name='Tokyo choropleth Map',
    geo_data=geojson,
    data=prod_df,
    columns=['A', 'F'], 
    key_on='feature.properties.N03_007',
    fill_color='BuGn',
    nan_fill_color='darkgray',
    fill_opacity=0.8,
    nan_fill_opacity=0.8,
    line_opacity=0.2,
    legend_name='区市町村別　陽性者数累計（人）　2021年10月15日時点 ... '
).add_to(m2)
folium.LayerControl().add_to(m2)
m2.save('tokyo_choropleth_map.html')