
import pandas as pd

def descriptive_analyses(dataframe):

    print('Beginning of the descriptive analysis!')
    print('-' * 50)

    dataframe_size = len(dataframe)
    print(f'Dataset size: {dataframe_size}!')

    # Percentage of converted clients
    print('-' * 50)
    converted_clients = len(dataframe[dataframe['converted'] == 1])
    print(f'Converted clients percentage: {(converted_clients / dataframe_size):.2%}')
    print(f'Not converted clients percentage: {((dataframe_size - converted_clients) / dataframe_size):.2%}')

    # The percentage of clients who viewed the private advertisement, as well as the percentage who did not
    print('-' * 50)
    group_private_ad = len(dataframe[dataframe['groups'] == 1])
    print(f'Percentage of clients subject to private advertisement: {(group_private_ad / dataframe_size):.2%}')
    print(f'Percentage of clients subject to public advertisement: {((dataframe_size - group_private_ad) / dataframe_size):.2%}')

    # On average, the quantity of advertisements viewed by each person
    print('-' * 50)
    average_ads = dataframe['total_ads'].mean()
    print(f'Quantity of advertisement seen by person, on average: {average_ads:.2f}')

    # The percentage of total advertisements for each day of the week
    print('-' * 50)
    print('The percentage of total advertisements for each day of the week!')
    days_map = {1 : 'Sunday', 2 : 'Monday', 3 :'Tuesday', 4 : 'Wednesday', 5 : 'Thursday', 6 : 'Friday', 7 : 'Saturday'}
    days_ads = dataframe['most_ads_day'].map(days_map).value_counts().sort_values(ascending = False).apply(lambda x: round((x / dataframe_size) * 100, 2)).apply(lambda x: str(x) + '%')
    print(days_ads)

    # The percentage of total advertisements (early morning, morning, afternoon and evening)
    print('-' * 50)
    print('The percentage of total advertisements (early morning, morning, afternoon and evening)')
    hours_map = {0 : '0h - 5h', 1 : '6h - 11h', 2 : '12h - 17h', 3: '18h - 23h'}
    hours_ads = dataframe['most_ads_hour'].map(hours_map).value_counts().sort_values(ascending = False).apply(lambda x: round((x / dataframe_size) * 100, 2)).apply(lambda x: str(x) + '%')
    print(hours_ads)
    
    # Contingency table between converted, groups and total_ads columns
    print('-' * 50)
    print('Contingency Table!')
    groupby_results = dataframe.groupby(['converted'], as_index = False)[['groups', 'total_ads']].mean()
    groupby_results = groupby_results.apply(lambda x: round(x, 2))
    print(groupby_results)

    # End
    print('-' * 50)
    return print('End of descriptive analysis!')
