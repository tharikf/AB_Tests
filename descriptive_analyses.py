
import pandas as pd

def descriptive_analyses(dataframe):

    print('Beginning of the descriptive analysis!')
    print('-' * 50)

    dataframe_size = len(dataframe)
    print(f'Dataset size: {dataframe_size}!')

    # Percentage of clients converted in dataframe
    print('-' * 50)
    converted_clientes = len(dataframe[dataframe['converted'] == 1])
    print(f'Converted clients percentage: {(converted_clientes / dataframe_size):.2%}')
    print(f'Not converted clients percentage: {((dataframe_size - converted_clientes) / dataframe_size):.2%}')

    # Percentage of clients who saw the private advertisement and the percentage who did not
    print('-' * 50)
    group_private_ad = len(dataframe[dataframe['groups'] == 1])
    print(f'Percentage of clients subject to private advertisement: {(group_private_ad / dataframe_size):.2%}')
    print(f'Percentage of clients subject to public advertisement: {((dataframe_size - group_private_ad) / dataframe_size):.2%}')

    # Average advertisement saw by person
    print('-' * 50)
    average_ads = dataframe['total_ads'].mean()
    print(f'Average advertisement seen by person: {average_ads:.2f}')

    # Days which occurs most advertisement
    print('-' * 50)
    print('Days which people view advertisement the most!')
    days_map = {1 : 'Sunday', 2 : 'Monday', 3 :'Tuesday', 4 : 'Wednesday', 5 : 'Thursday', 6 : 'Friday', 7 : 'Saturday'}
    days_ads = dataframe['most_ads_day'].map(days_map).value_counts().sort_values(ascending = False).apply(lambda x: round((x / dataframe_size) * 100, 2)).apply(lambda x: str(x) + '%')
    print(days_ads)

    # Hours which occurs most adverstisement
    print('-' * 50)
    print('Part of the day which people view advertisement the most')
    hours_map = {0 : '0h - 5h', 1 : '6h - 11h', 2 : '12h - 17h', 3: '18h - 23h'}
    hours_ads = dataframe['most_ads_hour'].map(hours_map).value_counts().sort_values(ascending = False).apply(lambda x: round((x / dataframe_size) * 100, 2)).apply(lambda x: str(x) + '%')
    print(hours_ads)
    
    # Contingency table between converted column and columns groups and total_ads
    print('-' * 50)
    print('Contingency Table')
    groupby_results = dataframe.groupby(['converted'], as_index = False)[['groups', 'total_ads']].mean()
    groupby_results = groupby_results.apply(lambda x: round(x, 2))
    print(groupby_results)

    # End
    print('\n')
    return print('End of descriptive analysis!')
