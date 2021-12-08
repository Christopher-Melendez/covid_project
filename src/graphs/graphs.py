from tables.models import covid_cases, covid_deaths, labor_stats, health_stats
from tables.tables import model_to_df
import pandas as pd
import plotly.express as px

def create_graph(graph_choice):
    if graph_choice == 'COVID-19 Cases':
        graph = model_to_df(covid_cases, ['county', 'C_Pos_C_Test'])
        fig = px.bar(graph, x= 'county', y = 'C_Pos_C_Test')
    elif graph_choice == 'COVID-19 Deaths':
        graph = model_to_df(covid_deaths, ['county', 'deaths_per100'])
        fig = px.bar(graph, x= 'county', y = 'deaths_per100')
    elif graph_choice == 'Median Income':
        graph = model_to_df(labor_stats, ['county', 'median_income'])
        fig = px.bar(graph, x= 'county', y = 'median_income')
    elif graph_choice == 'College Education':
        graph = model_to_df(labor_stats, ['county', 'percent_college'])
        fig = px.bar(graph, x= 'county', y = 'percent_college')
    elif graph_choice == 'Unemployment':
        graph = model_to_df(labor_stats, ['county', 'percent_unemployed'])
        fig = px.bar(graph, x= 'county', y = 'percent_unemployed')
    elif graph_choice == 'Poverty':
        graph = model_to_df(labor_stats, ['county', 'percent_poverty'])
        fig = px.bar(graph, x= 'county', y = 'percent_poverty')
    elif graph_choice == 'Insurance Coverage':
        graph = model_to_df(health_stats, ['county', 'percent_insured'])
        fig = px.bar(graph, x= 'county', y = 'percent_insured')
    else:
        graph = "<p>Sorry No Data Found, Try Again Later</p>"
    return fig
