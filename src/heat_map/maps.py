import folium
import pandas as pd
import json
import os
import tables
from django.db.models import F
from tables.models import covid_cases
 
#import geopandas as gpd


#TEST COMMENT NEW THING DONE

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

    #Create map object, N&E positive, S&W negative

    #Global tooltip
    tooltip = 'Click for More Info'

    #Create markers


    #Result Set to store SQL query Wtih all rows.. run for loop to iterate through results and populate the overlays..

    #counties = os.path.join('data', 'ny_counties.json')
    #covid_data = os.path.join('data', 'COVID_CASES.csv')
    counties = 'heat_map/data/ny_counties.json'
    #covid_data = 'heat_map/data/COVID_CASES.csv'
    #county_data = pd.read_csv(covid_data)
    
    #data_rows = covid_cases.objects.filter()
    

        
            


        # list_1 = []
        # list_2 = []
        # for i in range(data_rows):
        #     row = model.objects.get(id=(i+1))
        #     for i in range(columns):
        #         temp_list = []
        #         temp_list.append(getattr(row, columns[i]))
        #     list_1.append(getattr(row, columns[0]))
        #     list_2.append(getattr(row, columns[1]))
        # data_dict = {columns[0]: list_1, columns[1]: list_2}
        # data_frame = pd.DataFrame(data=data_dict)
        # print("Worked?")
        # return data_frame


    # data_rows = covid_cases.objects.all().count()
    # list_1 = []
    # list_2 = []
    
    # for i in range(data_rows):
    #     row = covid_cases.objects.get(id=(i+1))
    #     list_1.append(row.county)
    #     list_2.append(row.C_Pos_C_Test)
    
    # data_dict = {'County': list_1, 'C_POS/C_TEST': list_2}
    # data_frame = pd.DataFrame(data=data_dict)

    m = folium.Map(location=[43.2994, -74.2179], zoom_start=7)
    folium.TileLayer('CartoDB positron',name="Light Map",control=False).add_to(m)

    if map_choice == 'COVID-19 Cases':
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
        covid_deaths = 'heat_map/data/COVID_DEATHS.csv'
        county_data = pd.read_csv(covid_deaths)

        m.choropleth(
            geo_data=counties,
            name='choropleth',
            data= county_data,
            columns=['County', 'Deaths P'],
            key_on='feature.properties.name',
            fill_color='OrRd',
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name='Deaths Per 100,000',
        )
        folium.LayerControl().add_to(m)

    elif map_choice == 'Median Income':
        folium.Marker(
            [43.332600, -74.228500], 
            popup='<strong>Location Three</strong>',
            tooltip=tooltip,
            icon=folium.Icon(color='purple')
        ).add_to(m)
    elif map_choice == 'Insurance Coverage':
        folium.Marker([43.362600, -74.208500], 
            popup='<strong>Location Four</strong>',
            tooltip=tooltip,
            icon=folium.Icon(color='green', icon='leaf')
        ).add_to(m)
    else:
        pass
    
    # folium.Marker([lat_1, long_1], 
    #             popup='<strong>Location One</strong>',
    #             tooltip=tooltip).add_to(map),
    # folium.Marker([43.272600, -74.458500], 
    #             popup='<strong>Location Two</strong>',
    #             tooltip=tooltip,
    #             icon=folium.Icon(icon='cloud')).add_to(map),
    # folium.Marker([43.332600, -74.228500], 
    #             popup='<strong>Location Three</strong>',
    #             tooltip=tooltip,
    #             icon=folium.Icon(color='purple')).add_to(map),
    # folium.Marker([43.362600, -74.208500], 
    #             popup='<strong>Location Four</strong>',
    #             tooltip=tooltip,
    #             icon=folium.Icon(color='green', icon='leaf')).add_to(map),


    
 



    #Generate map
    
    map_html_text = m.get_root().render()

    return map_html_text
