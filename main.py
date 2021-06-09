# %%
from collections import defaultdict
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv('dataset.csv', sep=',')
df.head()
# %%
# count unique users
count_users = df['user_id'].nunique()
print(count_users)
# %%
# percentage of country
percentage_country = df['country'].value_counts(normalize=True) * 100
print(percentage_country)
# %%
# number of users by country
def percentage_users_by_country():
    users_id = df['user_id'].to_list()
    countries = df['country'].to_list()
    viewed_users = []
    country_count_users = defaultdict(int)
    for i, country in enumerate(countries):
        if users_id[i] in viewed_users:
            continue
        country_count_users[country] += 1
        viewed_users.append(users_id[i])
    return country_count_users

prctg_user_country = percentage_users_by_country()
print(prctg_user_country)
# %%
def visualization_prctg_user_country():
    _, ax = plt.subplots()
    countries = prctg_user_country.keys()
    y_pos = np.arange(len(countries))
    x_values = list(prctg_user_country.values())
    ax.barh(y_pos, x_values)
    ax.set_yticks(y_pos)
    ax.set_yticklabels(countries)

    ax.set_xlabel('Number of users')
    ax.set_ylabel('Countries')
    ax.set_title('Number of users by country')

    plt.show()

visualization_prctg_user_country()
# %%
# number event types by countries
def count_event_types_by_countries():
    event_types = df['event_type'].to_list()
    countries = df['country'].to_list()
    count_event_types = defaultdict(lambda: {'countries': [], 'count': []})
    for i, event_type in enumerate(event_types):
        if not countries[i] in count_event_types[event_type]['countries']:
            count_event_types[event_type]['countries'].append(countries[i])
            count_event_types[event_type]['count'].append(0)
        else:
            for j, country in enumerate(count_event_types[event_type]['countries']):
                if countries[i] == country:
                    count_event_types[event_type]['count'][j] += 1
                    break
    return count_event_types

cnt_event_types_countries = count_event_types_by_countries()
print(cnt_event_types_countries)
# %%
def visualization_cnt_event_types_countries():
    _, ax = plt.subplots()
    event_types = cnt_event_types_countries.keys()
    countries = []
    for cnt_event_type_country in cnt_event_types_countries.values():
        for country in cnt_event_type_country['countries']:
            if not country in countries:
                countries.append(country)

    y_pos = np.arange(len(cnt_event_types_countries))
    x_pos = np.arange(len(countries))
    ax.set_yticks(y_pos)
    ax.set_yticklabels(event_types)
    ax.set_xticks(x_pos)
    ax.set_xticklabels(countries)

    area = []
    for cnt_event_type_country in cnt_event_types_countries.values():
        c = []
        for country in countries:
            if country in cnt_event_type_country['countries']:
                index_country = cnt_event_type_country['countries'].index(country)
                c.append(cnt_event_type_country['count'][index_country])
            else:
                c.append(0)
        area.append(c)

    plt.pcolormesh(x_pos, y_pos, area, shading='auto')
    plt.show()

visualization_cnt_event_types_countries()
# %%
