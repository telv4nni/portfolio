import pandas as pd
import glob
import os

### This code counts SUM of 1P, 1P3P SALES and creates aggregated, cleaned DB with sales per zipcode
### It loads multiple files from selected date range and uses chunks to save memory while dealing with huge data 

#Load list of all csv files
files = glob.glob(r'Z:\Client\*.csv')

#Create list of files within date range
targetfiles = [
    f"Client_{d.strftime('%Y-%m-%d')}_pl.csv"
    for d in pd.date_range('2026-07-20', '2026-10-11')
]

#Filter the original file list by list within date range
files = [f for f in files if os.path.basename(f) in targetfiles]

#Define variables to sum sales value of 1st party and 1p3p sales
sum1p = 0
sum1p3p = 0

#Create empty list for aggregated chunks
aggregated_chunks = []

#Iterating load of the files by chunks:
for file in files:

    print(f"Processing {os.path.basename(file)}")

    for chunk in pd.read_csv(
        file,
        encoding='utf-8',
        sep=',',
        usecols=[
            'transaction_id',
            'transaction_date',
            'seller',
            'delivery_country',
            'delivery_zip_code',
            'sales_value',
            'sales_units'
        ],
        chunksize=500_000
    ):
        #Convert sales_value, sales_units and transaction_id to numeric and fill out empty values with 0
        chunk['sales_value'] = pd.to_numeric(
            chunk['sales_value'],
            errors='coerce'
        ).fillna(0)
        chunk['transaction_id'] = pd.to_numeric(
            chunk['transaction_id'],
            errors='coerce'
        ).fillna(0)
        chunk['sales_units'] = pd.to_numeric(
            chunk['sales_units'],
            errors='coerce'
        ).fillna(0)
        
        #Filter out transactions with ID, units or value = 0
        chunk = chunk[
            (chunk['transaction_id'] != 0) &
            (chunk['sales_units'] != 0) &
            (chunk['sales_value'] != 0)
        ]

        #Convert delivery_country to uppercase string
        chunk['delivery_country'] = chunk['delivery_country'].astype(str).str.upper()

        #Filter only transactions where delivery_country = POLAND
        chunk = chunk[
            chunk['delivery_country'] == 'POLAND'
        ]


        #Create zipcode5 -> delivery zip_code as str, keep only digits
        chunk['zipcode5'] = (
            chunk['delivery_zip_code']
            .astype(str)
            .str.replace(r'\D', '', regex=True)
        )

        #Create a mask to identify valid 5-digit zipcodes
        mask = chunk['zipcode5'].str.len() == 5

        #Set delivery_zip_code to OTHERS for all transactions
        chunk['delivery_zip_code'] = 'OTHERS'

        #Take 5 digit codes and make them in format 01-234
        chunk.loc[mask, 'delivery_zip_code'] = (
            chunk.loc[mask, 'zipcode5'].str[:2]
            + '-'
            + chunk.loc[mask, 'zipcode5'].str[2:]
        )

        #Calculate sum for 1p3p sales
        sum1p3p += chunk['sales_value'].sum()

        #Calculate sum for 1p sales
        sum1p += chunk.loc[
            chunk['seller'] == 'Retailer 1P',
            'sales_value'
        ].sum()

        #Aggregate sales by seller, transaction_date and delivery_zip_code for current chunk
        grouped = (
            chunk.groupby(
                ['seller', 'transaction_date', 'delivery_zip_code'],
                as_index=False
            )['sales_value']
            .sum()
        )
        aggregated_chunks.append(grouped)

#Create sales per zip df from aggregated_chunks
salesperzip = (
    pd.concat(aggregated_chunks)
    .groupby(
        ['seller', 'transaction_date', 'delivery_zip_code'],
        as_index=False
    )['sales_value']
    .sum()
)

#Save sales per zip df
salesperzip.to_csv(
    'salesperzip2.csv',
    index=False
)

#Print sums of sales
print(f"1P: {sum1p:,.2f}")
print(f"1P+3P: {sum1p3p:,.2f}")