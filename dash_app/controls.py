# Controls for webapp






urban = dict(
    {
        'Large urban area': 'urban',
        'Accessible rural area': 'rural',
        'Accessible small town': 'small town',
        'Other urban area': 'urban',
        'Remote rural area': 'rural',
        'Very remote rural area': 'rural',
        'Remote small town': 'small town',
        'Urban city and town': 'urban',
        'Rural village': 'rural',
        'Rural hamlet and isolated dwellings': 'rural',
        'Rural town and fringe': 'rural',
        'Urban major conurbation': 'urban',
        'Rural town and fringe in a sparse setting': 'rural',
        'Rural village in a sparse setting': 'rural',
        'Rural hamlet and isolated dwellings in a sparse setting': 'rural',
        'Urban city and town in a sparse setting': 'urban',
        'Urban minor conurbation': 'urban', 'Very remote small town': 'small town', 'other': 'other'
    }
)

REGIONS = {
    "001": 'Yorkshire and The Humber',
    "003": 'East of England',
    "005": 'South West',
    "007": 'Scotland',
    "009": 'North West',
    "011": 'Wales',
    "013": 'Northern Ireland',
    "015": 'East Midlands',
    "017": 'London',
    "019": 'South East',
    "021": 'West Midlands',
    "023": 'North East',
}

regions = {
    'Yorkshire and The Humber',
    'East of England',
    'South West (England)',
    'Scotland',
    'North West (England)',
    'Wales',
    'Northern Ireland',
    'East Midlands (England)',
    'London',
    'South East (England)',
    'West Midlands (England)',
    'North East (England)',
}


NUTS118NM = dict(
    {
        'Yorkshire and The Humber': 'Yorkshire and The Humber',
        'East of England': 'East of England',
        'South West': 'South West (England)',
        'Scotland': 'Scotland',
        'North West': 'North West (England)',
        'Wales': 'Wales',
        'Northern Ireland': 'Northern Ireland',
        'East Midlands': 'East Midlands (England)',
        'London': 'London',
        'South East': 'South East (England)',
        'West Midlands': 'West Midlands (England)',
        'North East': 'North East (England)',
    }
)

NUTS118NM_118CD = dict(
    {
        'London': 'UKI',
        'South East (England)': 'UKJ',
        'East Midlands (England)': 'UKF',
        'West Midlands (England)': 'UKG',
        'East of England': 'UKH',
        'North East (England)': 'UKC',
        'South West (England)': 'UKK',
        'North West (England)': 'UKD',
        'Scotland': 'UKM',
        'Northern Ireland': 'UKN',
        'Wales': 'UKL',
        'Yorkshire and The Humber': 'UKE',
    }
)

NUTS118CD_118NM = dict(
    {
        'UKI': 'London',
        'UKJ': 'South East (England)',
        'UKF': 'East Midlands (England)',
        'UKG': 'West Midlands (England)',
        'UKH': 'East of England',
        'UKC': 'North East (England)',
        'UKK': 'South West (England)',
        'UKD': 'North West (England)',
        'UKM': 'Scotland',
        'UKN': 'Northern Ireland',
        'UKL': 'Wales',
        'UKE': 'Yorkshire and The Humber',
    }
)

