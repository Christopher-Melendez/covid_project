import folium
#Create map object, N&E positive, S&W negative
map = folium.Map(location=[43.2994, -74.2179], zoom_start=12)

#Global tooltip
tooltip = 'Click for More Info'

#Create markers
folium.Marker([43.302600, -74.258500], 
               popup='<strong>Location One</strong>',
               tooltip=tooltip).add_to(map),
folium.Marker([43.272600, -74.458500], 
               popup='<strong>Location Two</strong>',
               tooltip=tooltip,
               icon=folium.Icon(icon='cloud')).add_to(map),
folium.Marker([43.332600, -74.228500], 
               popup='<strong>Location Three</strong>',
               tooltip=tooltip,
               icon=folium.Icon(color='purple')).add_to(map),
folium.Marker([43.362600, -74.208500], 
               popup='<strong>Location Four</strong>',
               tooltip=tooltip,
               icon=folium.Icon(color='green', icon='leaf')).add_to(map),

#Circle marker
folium.CircleMarker(
   location=[43.1009, -75.2327],
   radius=50,
   popup='Utica',
   color='#428BCA',
   fill=True,
   fill_color='#428BCA'
).add_to(map),


#Figure out how to generate map with different dimensions (~%50)

#Generate map
map.save('map.html')