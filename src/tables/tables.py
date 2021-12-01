from tables.models import covid_cases, covid_deaths, labor_stats, health_stats
import pandas as pd

#Helper Function to take model elements and create a pandas dataframe
def model_to_df(model, columns):
    #Local Variables
    returning_list = []
    data_dict = {}

    #Find out how many rows to cycle through
    data_rows = model.objects.all().count()

    #Build a dictionary of a list of values from each model.
    for i in columns:
        temp_list = []
        for j in range(data_rows):
            row = model.objects.get(id=(j+1))
            temp_list.append(getattr(row, i))
        returning_list.append(temp_list)
        data_dict[i] = temp_list
    
    #Convert dictionary to pandas dataframe
    data_frame = pd.DataFrame(data=data_dict)
    return data_frame

def make_table(table_choice):
    table_html = ""

    #Return html text of appropriate model using pandas dataframes and builtin html table functionality
    if table_choice == 'COVID-19 Cases':
        table_html = model_to_df(covid_cases, ['county', 'C_Pos_C_Test']).to_html()
    elif table_choice == 'COVID-19 Deaths':
        table_html = model_to_df(covid_deaths, ['county', 'deaths_per100']).to_html()
    elif table_choice == 'Median Income':
        table_html = model_to_df(labor_stats, ['county', 'median_income']).to_html()
    elif table_choice == 'College Education':
        table_html = model_to_df(labor_stats, ['county', 'percent_college']).to_html()
    elif table_choice == 'Unemployment':
        table_html = model_to_df(labor_stats, ['county', 'percent_unemployed']).to_html()
    elif table_choice == 'Poverty':
        table_html = model_to_df(labor_stats, ['county', 'percent_poverty']).to_html()
    elif table_choice == 'Insurance Coverage':
        table_html = model_to_df(health_stats, ['county', 'percent_insured']).to_html()
    else:
        table_html = "<p>Sorry No Data Found, Try Again Later</p>"
        
    return table_html