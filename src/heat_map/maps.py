import folium
import pandas as pd
from django.db.models import F
from tables.models import covid_cases, covid_deaths, labor_stats, health_stats

#Import Data from Data Models and Convert to Pandas Data Frame
from tables.tables import model_to_df


def maps(map_choice):
    #Temp Stuff Till Database Finalized...
    counties = 'heat_map/data/ny_counties.json'    
    
    
    #Initializing Folium Map Cenetered in Central New York
    tooltip = 'Click for More Info'
    m = folium.Map(location=[43.0994, -75.9179], zoom_start=6)
    folium.TileLayer('CartoDB positron',name="Light Map",control=False).add_to(m)

    if map_choice == 'COVID-19 Cases':
        #Ryan Created Chloropleth Map For Percent Stat of Positive Covid Cases / Total Tests Performed by County
        m.choropleth(
            geo_data=counties,
            name='choropleth',
            data= model_to_df(covid_cases, ['county', 'C_Pos_C_Test']),
            columns=['county', 'C_Pos_C_Test'],
            key_on='feature.properties.name',
            fill_color='YlGn',
            fill_opacity=0.7,
            line_opacity=0.5,
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
            line_opacity=0.5,
            legend_name='Deaths Per 100,000',
        )
        folium.LayerControl().add_to(m)

    elif map_choice == 'Median Income': 
        m.choropleth(
            geo_data=counties,
            name='choropleth',
            data= model_to_df(labor_stats, ['county', 'median_income']),
            columns=['county', 'median_income'],
            key_on='feature.properties.name',
            fill_color='GnBu',
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name='Median Income',
        )
        folium.LayerControl().add_to(m)

    elif map_choice == 'College Education':
      m.choropleth(
          geo_data=counties,
          name='choropleth',
          data= model_to_df(labor_stats, ['county', 'percent_college']),
          columns=['county', 'percent_college'],
          key_on='feature.properties.name',
          fill_color='BuPu',
          fill_opacity=0.7,
          line_opacity=0.5,
          legend_name='Percent of Adults with College Education',
      )
      folium.LayerControl().add_to(m)

    elif map_choice == 'Unemployment':
      m.choropleth(
          geo_data=counties,
          name='choropleth',
          data= model_to_df(labor_stats, ['county', 'percent_unemployed']),
          columns=['county', 'percent_unemployed'],
          key_on='feature.properties.name',
          fill_color='YlGnBu',
          fill_opacity=0.7,
          line_opacity=0.5,
          legend_name='Percent of Adults who are Unemployed',
      )
      folium.LayerControl().add_to(m)

    elif map_choice == 'Poverty': 
      m.choropleth(
          geo_data=counties,
          name='choropleth',
          data= model_to_df(labor_stats, ['county', 'percent_poverty']),
          columns=['county', 'percent_poverty'],
          key_on='feature.properties.name',
          fill_color='YlOrBr',
          fill_opacity=0.7,
          line_opacity=0.5,
          legend_name='Percent of Population Living in Poverty',
      )
      folium.LayerControl().add_to(m)

    elif map_choice == 'Insurance Coverage':
        m.choropleth(
            geo_data=counties,
            name='choropleth',
            data= model_to_df(health_stats, ['county', 'percent_insured']),
            columns=['county', 'percent_insured'],
            key_on='feature.properties.name',
            fill_color='RdPu',
            fill_opacity=0.7,
            line_opacity=0.5,
            legend_name='Percent Insured',
        )
        folium.LayerControl().add_to(m)
    else:
        pass
    
    #Generate map as HTML Text String and return
    map_html_text = m.get_root().render()

    return map_html_text
