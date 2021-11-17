import folium
import pandas as pd
import json
import os
import tables
from django.db.models import F
from tables.models import covid_cases, covid_deaths
 
#import geopandas as gpd


#Import Data from Data Models and Convert to Pandas Data Frame
def model_to_df(model, columns):
        returning_list = []
        data_dict = {}
        data_rows = model.objects.all().count()
        for i in columns:
            temp_list = []
            for j in range(data_rows):
                row = model.objects.get(id=(j+1))
                temp_list.append(getattr(row, i))
            returning_list.append(temp_list)
            data_dict[i] = temp_list
        data_frame = pd.DataFrame(data=data_dict)
        return data_frame

def maps(map_choice):
    #Temp Stuff Till Database Finalized...
    counties = 'heat_map/data/ny_counties.json'    
    
    
    #Initializing Folium Map Cenetered in Central New York
    tooltip = 'Click for More Info'
    m = folium.Map(location=[43.2994, -74.2179], zoom_start=7)
    folium.TileLayer('CartoDB positron',name="Light Map",control=False).add_to(m)

    if map_choice == 'COVID-19 Cases':
        #Ryan Created Chloropleth Map For Percent Stat of Positive Covid Cases / Total Tests Performed by County
        m.choropleth(
            geo_data=counties,
            name='choropleth',
            data= model_to_df(covid_cases, ['county', 'C_Pos_C_Test']),
            columns=['county', 'C_Pos_C_Test'],
            key_on='feature.properties.name',
            fill_color='OrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Percent Positive',
        )
        folium.LayerControl().add_to(m)

    elif map_choice == 'COVID-19 Deaths':
        #Ryan Created Chloropleth Map For Deaths Per 100k By County
        m.choropleth(
            geo_data=counties,
            name='choropleth',
            data= model_to_df(covid_deaths, ['county', 'deaths_per100']),
            columns=['county', 'deaths_per100'],
            key_on='feature.properties.name',
            fill_color='OrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Deaths Per 100,000',
        )
        folium.LayerControl().add_to(m)

    elif map_choice == 'Median Income':
        median_data = 'heat_map/data/median_income.csv'
        inc_data = pd.read_csv(median_data) 
        m.choropleth(
            geo_data=counties,
            name='choropleth',
            data = inc_data,
            # data= model_to_df(med_income, ['county', 'median_income']),
            columns=['county', 'median_income'],
            key_on='feature.properties.name',
            fill_color='OrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Median Income',
        )
        folium.LayerControl().add_to(m)

    elif map_choice == 'Insurance Coverage':
        folium.Marker([43.362600, -74.208500], 
            popup='<strong>Location Four</strong>',
            tooltip=tooltip,
            icon=folium.Icon(color='green', icon='leaf')
        ).add_to(m)
    else:
        pass
    
    #Generate map as HTML Text String and return
    map_html_text = m.get_root().render()

    return map_html_text
