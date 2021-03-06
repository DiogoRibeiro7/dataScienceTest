import random
import time
import pandas as pd
import numpy as np
from random import seed, randint
import pathlib
import requests
import zipfile
import io
from datetime import datetime, date, timedelta
import re
from controls import urban, NUTS118NM, NUTS118NM_118CD

# get relative data folder
PATH = pathlib.Path().parent
DATA_PATH = PATH.joinpath("data").resolve()
FILE_PATH = DATA_PATH.joinpath('postcodes.csv').resolve()
FILE_PATH_1 = DATA_PATH.joinpath('conditions.csv').resolve()
FILE_PATH_2 = DATA_PATH.joinpath(
    'December_2018__to_NUTS3_to_NUTS2_to_NUTS1.csv').resolve()

regex = "^(?:(?P<a1>[Gg][Ii][Rr])(?P<d1>) (?P<s1>0)(?P<u1>[Aa]{2}))|(?:(?:(?:(?P<a2>[A-Za-z])(?P<d2>[0-9]{1,2}))|(?:(?:(?P<a3>[A-Za-z][A-Ha-hJ-Yj-y])(?P<d3>[0-9]{1,2}))|(?:(?:(?P<a4>[A-Za-z])(?P<d4>[0-9][A-Za-z]))|(?:(?P<a5>[A-Za-z][A-Ha-hJ-Yj-y])(?P<d5>[0-9]?[A-Za-z]))))) (?P<s2>[0-9])(?P<u2>[A-Za-z]{2}))$"

conditions = ['seizures',
              'hypertension',
              'parkinsons',
              'diabetes',
              'mentalIllness',
              'alzheimers',
              'irregularHeart',
              'bradicardia',
              'tachycardia',
              'respiratory',
              'multipleSclerosis',
              'miscNeural',
              'hypotension',
              'parkinsonDisease',
              'mentalHealthIssue',
              'paralysis',
              'cancer',
              'miscHeart',
              'bradycardia',
              'brainInjury',
              'stroke',
              'sleepApnea',
              'arthritis',
              'renalUrinary',
              'insomnia',
              'dementia',
              'otherHeartCondition']


def calculate_age(born):
    today = date.today()
    try:
        birthday = born.replace(year=today.year)
    except ValueError:  # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year, month=born.month+1, day=1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year


def gen_gender(number):
    gender = ['male', 'female', 'other']
    cond = []
    for _ in range(number):
        value = 1
        cond.append(random.sample(gender, value))
    return pd.DataFrame(cond, columns=['gender'])


def gen_dob(begin, end, sample_size):
    dob = []
    for i in range(sample_size):
        start_date = date(begin, 1, 1)
        end_date = date(end, 2, 1)

        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + timedelta(days=random_number_of_days)
        #date_time_obj = datetime.strptime(random_date, '%Y-%m-%d')
        dob.append(random_date)
    df = pd.to_datetime(dob)

    return pd.DataFrame(df)


def addNumberToDate(date, sample_size):
    number_to_add = np.random.randint(50, 1000, size=sample_size)
    exit = pd.to_datetime(date) + pd.to_timedelta(number_to_add, unit='D')
    return exit


def bmi_func(weight, height):
    height = height/100
    bmi = weight / height**2
    return bmi


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)


def generate_dates(start, end, prop, number_generate):
    users_dob = []
    column_names = ['dob']
    df = pd.DataFrame(columns=column_names)
    for i in range(number_generate):
        dob = random_date(start, end, random.random())
        users_dob.append(dob)

    return pd.DataFrame(users_dob, columns=['dob'])


def gen_weight_height(start, end, number, col):
    number_gen = []
    for _ in range(number):
        value = randint(start, end)
        number_gen.append(value)
    return pd.DataFrame(number_gen, columns=[col])


def gen_conditions(conditions, number):
    cond = []
    for _ in range(number):
        value = randint(0, 5)
        if value == 0:
            cond.append({'conditions': ['no conditions']})

        else:
            cond.append({'conditions': random.sample(conditions, value)})
    return pd.DataFrame(cond, columns=['conditions'])


def gen_postcodes(postcodes, sample_size):
    return pd.DataFrame(random.sample(postcodes, sample_size), columns=['postcode'])


def update_file():
    '''
    https://www.doogal.co.uk/postcodedownloads.php
    '''
    zip_file_url = 'https://www.doogal.co.uk/files/postcodes.zip'
    r = requests.get(zip_file_url)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall(DATA_PATH)
    z.close()
    data = pd.read_csv(FILE_PATH, low_memory=False)
    data = data[data['In Use?'] == 'Yes']

    data.Region.fillna(data['Country'], inplace=True)
    data.Region.fillna('Other', inplace=True)
    data = data.drop(data[(data['Region'] == 'England') |
                          (data['Region'] == 'Other')].index)

    data = data.reset_index(drop=True)

    data.to_csv(FILE_PATH, index=False)


def body_fat(data):
    '''
    Body fat percentage (BFP)
    "Overweight & Obesity." Centers for Disease Control and Prevention. www.cdc.gov/obesity/data/index.html
    '''
    data['BFP'] = 0

    data['BFP'][data['gender'] == 0] = 0
    data['BFP'][data['gender'] == 'female'] = 1.20 * data['BMI'][data['gender']
                                                                 == 'female'] + 0.23 * data['age'][data['gender'] == 'female'] - 5.4
    data['BFP'][data['gender'] == 'male'] = 1.20 * data['BMI'][data['gender']
                                                               == 'male'] + 0.23 * data['age'][data['gender'] == 'male'] - 16.2
    return data


def basalMetabolicRate(data):
    '''
    The Basal Metabolic Rate (BMR) Calculator estimates your basal metabolic rate — the 
    amount of energy expended while at rest in a neutrally temperate environment
    Mifflin-St Jeor Equation:
    For Men:
    BMR = 10W + 6.25H - 5A + 5
    For women:
    BMR = 10W + 6.25H - 5A - 161
    '''
    data['BMR'] = 0

    data['BMR'][data['gender'] == 0] = 0
    data['BMR'][data['gender'] == 'female'] = 10 * data['weights'][data['gender'] == 'female'] + 6.25 * \
        data['heights'][data['gender'] == 'female'] - 5 * \
        data['age'][data['gender'] == 'female'] - 161
    data['BMR'][data['gender'] == 'male'] = 10 * data['weights'][data['gender'] == 'male'] + \
        6.25 * data['heights'][data['gender'] == 'male'] - \
        5*data['age'][data['gender'] == 'male'] + 5

    return data


def check_bmi_status(bmi):
    '''
    World Health Organization's (WHO) recommended body weight based on BMI values for adults. 
    It is used for both men and women, age 18 or older.
    '''
    if (bmi == 0):
        return 'No Disclosure'
    elif (bmi < 16):
        return 'Severe Thinness'
    elif (bmi < 17):
        return 'Moderate Thinness'
    elif (bmi < 18.5):
        return 'Mild Thinness'
    elif (bmi < 25):
        return 'Normal'
    elif (bmi < 30):
        return 'Overweight'
    elif (bmi < 35):
        return 'Obese Class I'
    elif (bmi < 40):
        return 'Obese Class II'
    else:
        return 'Obese Class III'


def parse_postcode(postcode):
    pc = postcode
    pc_parts = pc.str.extract(regex, re.IGNORECASE, expand=True)

    pc_parsed = pc.reset_index()
    pc_parsed['postcode_area'] = pd.concat(
        [pc_parts[['a%s' % i]] for i in range(1, 6)], axis=1).bfill(axis=1).iloc[:, 0]
    pc_parsed['postcode_district_part'] = pd.concat(
        [pc_parts[['d%s' % i]] for i in range(1, 6)], axis=1).bfill(axis=1).iloc[:, 0]
    pc_parsed['postcode_sector_part'] = pd.concat(
        [pc_parts[['s%s' % i]] for i in range(1, 3)], axis=1).bfill(axis=1).iloc[:, 0]
    pc_parsed['postcode_district'] = pc_parsed['postcode_area'] + \
        pc_parsed['postcode_district_part']
    pc_parsed['postcode_sector'] = pc_parsed['postcode_area'] + \
        pc_parsed['postcode_district_part'] + \
        ' ' + pc_parsed['postcode_sector_part']
    #pc_parsed = pc_parsed[['postcode_1','postcode_area','postcode_district','postcode_sector']]
    return pc_parsed['postcode_area'], pc_parsed['postcode_district_part'], pc_parsed['postcode_sector_part'], pc_parsed['postcode_district'], pc_parsed['postcode_sector']


def postToRegion(df):

    df_1 = pd.read_csv(FILE_PATH, low_memory=False)
    df_1['Rural/urban'].fillna(0, inplace=True)
    df_1['Rural/urban'].replace(0, 'other', inplace=True)

    df_1.Region.fillna(df_1['Country'], inplace=True)
    df_1.Region.fillna('Other', inplace=True)

    list_region = pd.Series(df_1['Region'].values,
                            index=df_1['Postcode area']).to_dict()
    list_income = pd.Series(
        df_1['Average Income'].values, index=df_1['Postcode area']).to_dict()
    list_rural = pd.Series(df_1['Rural/urban'].values,
                           index=df_1['Postcode area']).to_dict()

    df['Region'] = df['postcode_area'].apply(lambda x: list_region[x])
    df['income'] = df['postcode_area'].apply(lambda x: list_income[x])
    df['type_area'] = df['postcode_area'].apply(lambda x: list_rural[x])
    df['type_area'] = df['type_area'].apply(lambda x: urban[x])
    df['NUTS118NM'] = df['Region'].apply(lambda x: NUTS118NM[x])
    df['NUTS118CD'] = df['NUTS118NM'].apply(lambda x: NUTS118NM_118CD[x])

    return df


def extractConditions(df):

    df1 = df['conditions'].apply(frozenset).to_frame(name='conditions')

    for genre in frozenset.union(*df1.conditions):
        df1[genre] = df1.apply(lambda _: int(genre in _.conditions), axis=1)

    df1 = df1.drop(['conditions'], axis=1)

    conditions_col = list(df1.columns)
    conditions_col_update = conditions_col.remove('no conditions')

    df = pd.concat([df, df1], axis=1, sort=False)
    df['total_conditions'] = 0
    for condition in conditions_col:
        df['total_conditions'] += df[condition]

    return df

def businessIntelligence(result):
    
    from pandas.tseries import offsets 
    
    result_1 = result[['index', 'enter','exit','Region']]
    result_1['week_enter'] = result_1['enter'] + offsets.Week(weekday=6)
    result_1['week_exit'] = result_1['exit'] + offsets.Week(weekday=6)

    userEnter = result_1[['index','week_enter']].groupby(['week_enter']).count()
    userExit = result_1[['index','week_exit']].groupby(['week_exit']).count()

    userEnter = userEnter.reset_index()
    userExit = userExit.reset_index()

    userEnter.rename(columns={'index': 'enter'},inplace=True)
    userExit.rename(columns={'index': 'exit'},inplace=True)

    users_in_platform = pd.concat([userEnter, userExit], ignore_index=True)

    users_in_platform['week'] = users_in_platform['week_enter'].fillna(users_in_platform['week_exit'])
    users_in_platform = users_in_platform.drop(['week_exit','week_enter'],axis=1).fillna(0)
    
    
    users_in_platform[['exit','enter']] = users_in_platform[['exit','enter']].fillna(0).astype(int)

    users_in_platform['number_in'] = (users_in_platform['enter'] - users_in_platform['exit']).cumsum()
    users_in_platform = users_in_platform.sort_values(by='week')
    users_in_platform = users_in_platform.reset_index(drop=True)
    users_in_platform = users_in_platform[users_in_platform['week'] <= pd.to_datetime('today')]
    
    return users_in_platform

def filter_dataframe(df, gender, region, number_conditions):
    dff = df[df["gender"].isin(gender) & df["Region"].isin(region) & (df["total_conditions"] >= number_conditions)]
    return dff


def produce_individual(dff):
    
    import helpers as hlp
    list_conditions = hlp.conditions.copy()
    list_conditions.append('no conditions') 
    df = pd.DataFrame (list_conditions,columns=['conditions'])
    df['count'] = 0
    df = df.set_index(['conditions'])
    
    users = 0
    male = 0
    female = 0
    other = 0
    condition = 0
    for user in dff['index']:
        users +=1
        if dff['gender'][user] == 'male':
            male +=1
        if dff['gender'][user] == 'female':
            female += 1
        if dff['gender'][user] == 'other':
            other += 1
        if dff['total_conditions'][user] != 0:
            condition += 1
        for cond in list_conditions:
            if dff[cond][user] == 1:
                df.loc[cond]['count'] += 1
                
                
    df['percentage'] = round(df['count']/users*100,2)
    df_1 = df[:-1]
    max_condition = df_1['count'].idxmax()
    min_condition = df_1['count'].idxmin()
    
    diseases_stats = {'condition_max': max_condition, 'condition_min': min_condition,}

    return users, round(male/users*100,2), round(female/users*100,2),round(other/users*100,2),round(condition/users*100,2),df.reset_index(),diseases_stats