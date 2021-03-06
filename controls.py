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

COUNTIES = {
    "001": "Albany",
    "003": "Allegany",
    "005": "Bronx",
    "007": "Broome",
    "009": "Cattaraugus",
    "011": "Cayuga",
    "013": "Chautauqua",
    "015": "Chemung",
    "017": "Chenango",
    "019": "Clinton",
    "021": "Columbia",
    "023": "Cortland",
    "025": "Delaware",
    "027": "Dutchess",
    "029": "Erie",
    "031": "Essex",
    "033": "Franklin",
    "035": "Fulton",
    "037": "Genesee",
    "039": "Greene",
    "041": "Hamilton",
    "043": "Herkimer",
    "045": "Jefferson",
    "047": "Kings",
    "049": "Lewis",
    "051": "Livingston",
    "053": "Madison",
    "055": "Monroe",
    "057": "Montgomery",
    "059": "Nassau",
    "061": "New York",
    "063": "Niagara",
    "065": "Oneida",
    "067": "Onondaga",
    "069": "Ontario",
    "071": "Orange",
    "073": "Orleans",
    "075": "Oswego",
    "077": "Otsego",
    "079": "Putnam",
    "081": "Queens",
    "083": "Rensselaer",
    "085": "Richmond",
    "087": "Rockland",
    "089": "St. Lawrence",
    "091": "Saratoga",
    "093": "Schenectady",
    "095": "Schoharie",
    "097": "Schuyler",
    "099": "Seneca",
    "101": "Steuben",
    "103": "Suffolk",
    "105": "Sullivan",
    "107": "Tioga",
    "109": "Tompkins",
    "111": "Ulster",
    "113": "Warren",
    "115": "Washington",
    "117": "Wayne",
    "119": "Westchester",
    "121": "Wyoming",
    "123": "Yates",
}

WELL_STATUSES = dict(
    AC="Active",
    AR="Application Received to Drill/Plug/Convert",
    CA="Cancelled",
    DC="Drilling Completed",
    DD="Drilled Deeper",
    DG="Drilling in Progress",
    EX="Expired Permit",
    IN="Inactive",
    NR="Not Reported on AWR",
    PA="Plugged and Abandoned",
    PI="Permit Issued",
    PB="Plugged Back",
    PM="Plugged Back Multilateral",
    RE="Refunded Fee",
    RW="Released - Water Well",
    SI="Shut-In",
    TA="Temporarily Abandoned",
    TR="Transferred Permit",
    UN="Unknown",
    UL="Unknown Located",
    UM="Unknown Not Found",
    VP="Voided Permit",
)

WELL_TYPES = dict(
    BR="Brine",
    Confidential="Confidential",
    DH="Dry Hole",
    DS="Disposal",
    DW="Dry Wildcat",
    GD="Gas Development",
    GE="Gas Extension",
    GW="Gas Wildcat",
    IG="Gas Injection",
    IW="Oil Injection",
    LP="Liquefied Petroleum Gas Storage",
    MB="Monitoring Brine",
    MM="Monitoring Miscellaneous",
    MS="Monitoring Storage",
    NL="Not Listed",
    OB="Observation Well",
    OD="Oil Development",
    OE="Oil Extension",
    OW="Oil Wildcat",
    SG="Stratigraphic",
    ST="Storage",
    TH="Geothermal",
    UN="Unknown",
)

WELL_COLORS = dict(
    GD="#FFEDA0",
    GE="#FA9FB5",
    GW="#A1D99B",
    IG="#67BD65",
    OD="#BFD3E6",
    OE="#B3DE69",
    OW="#FDBF6F",
    ST="#FC9272",
    BR="#D0D1E6",
    MB="#ABD9E9",
    IW="#3690C0",
    LP="#F87A72",
    MS="#CA6BCC",
    Confidential="#DD3497",
    DH="#4EB3D3",
    DS="#FFFF33",
    DW="#FB9A99",
    MM="#A6D853",
    NL="#D4B9DA",
    OB="#AEB0B8",
    SG="#CCCCCC",
    TH="#EAE5D9",
    UN="#C29A84",
)