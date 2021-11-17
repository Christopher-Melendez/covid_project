from tables.models import covid_cases, covid_deaths
import pandas as pd

# def get_model_fields_str(model):
#     all_fields = model._meta.get_fields()
#     fields_list = []
#     for field_obj in all_fields:
#         field = field_obj.__repr__()
#         starting_point = field.find(':')
#         processed_field = field[starting_point+2:len(field)-1]
#         if processed_field == 'id':
#             pass
#         else:
#             fields_list.append(processed_field.title().replace("_"," "))
#     return fields_list

# def get_data(model):
#     pass
#     return

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

def make_table(table_choice):
    table_html = ""

    if table_choice == 'COVID-19 Cases':
        table_html = model_to_df(covid_cases, ['county', 'C_Pos_C_Test']).to_html()
    elif table_choice == 'COVID-19 Deaths':
        table_html = model_to_df(covid_deaths, ['county', 'deaths_per100']).to_html()
    elif table_choice == 'Median Income':
        table_html = "<p>Sorry No Data Found, Try Again Later</p>"
    elif table_choice == 'Insurance Coverage':
        table_html = "<p>Sorry No Data Found, Try Again Later</p>"
    else:
        table_html = "<p>Sorry No Data Found, Try Again Later</p>"
        
    return table_html