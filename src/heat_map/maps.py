import folium
import json


#TEST COMMENT NEW THING DONE


def maps(map_choice):

    #Create map object, N&E positive, S&W negative
    map = folium.Map(location=[43.2994, -74.2179], zoom_start=12)

    #Global tooltip
    tooltip = 'Click for More Info'

    #Create markers


    #Result Set to store SQL query Wtih all rows.. run for loop to iterate through results and populate the overlays..



    lat_1 = 43.302600
    long_1 = -74.258500

    if map_choice == 'COVID-19 Cases':
        print("YEEEEES")
        folium.Marker(
            [lat_1, long_1],
            pop_up = '<strong>Location One</strong>',
            tooltip=tooltip
        ).add_to(map)
    elif map_choice == 'COVID-19 Deaths':
        folium.Marker(
            [43.272600, -74.458500],
            popup='<strong>Location Two</strong>',
            tooltip=tooltip,
            icon=folium.Icon(icon='cloud')
        ).add_to(map)
    elif map_choice == 'Median Income':
        folium.Marker(
            [43.332600, -74.228500], 
            popup='<strong>Location Three</strong>',
            tooltip=tooltip,
            icon=folium.Icon(color='purple')
        ).add_to(map)
    elif map_choice == 'Insurance Coverage':
        folium.Marker([43.362600, -74.208500], 
            popup='<strong>Location Four</strong>',
            tooltip=tooltip,
            icon=folium.Icon(color='green', icon='leaf')
        ).add_to(map)
    else:
        print("WELP ~.~")
    
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

    #Circle marker
    folium.CircleMarker(
    location=[43.1009, -75.2327],
    radius=50,
    popup='Utica',
    color='#428BCA',
    fill=True,
    fill_color='#428BCA'
    ).add_to(map),


    #Generate map
    file_path = 'heat_map/temp/map.html'
    map.save(file_path)

    with open(file_path, 'r') as file:
        map_html_text = file.read().replace('\n', '')



    return map_html_text
