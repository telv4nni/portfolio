import os
import pandas as pd

### This code compares OLD and NEW sales data files and generates a comprehensive Excel validation report
### It checks summary metrics, store-level sales, product hierarchies, item descriptions, and identifies missing records between both datasets

## 
### Variables to personalize
##

# Extensions (.csv/ .txt/ .xlsx are compatible)
extension_old = '.txt' # old input file extension
extension_new = '.xlsx' # new input file extension
hierarchy_filename = 'Hierarchia.xlsx' # hierarchy filename

# Set file separators
oldsep = '\t'
newsep = ''

# Select if you wish to export records that are not in old/new files (0 - don't export, 1 - export) [Takes a long time, good idea to disable for testing]
not_in_new = 1
not_in_old = 1

# Select 0 if headers are identical to not paste below headers to the old file
add_headers = 1

# Old file headers
headers_old = [
    "Week", "Year", "Shop Code", "Wojewodztwo",
    "Product group code level 1", "Product group code level 2", "Product group code level 3", "Product group code level 4",
    "Product group code level 1+2+3+4", "LAC Code", "Description", "EAN",
    "Manufacturer code", "Manufacturer", "Quantity", "Price",
    "Value"
]

# Select 1 to add hierarchy file
add_hierarchy = 1

# Name hierarchy column to compare
hierkey = "Product group code level 1+2+3+4"
# Name columns in hierarchy file (optional)
hiersector = "Sector"
hierdepartment = "Department"
hiergroup = "Group Class"
hierclass = "Class"

# Set hierarchy columns to compare
hierarchy_old_cols = [hiersector, hierdepartment, hiergroup, hierclass]
hierarchy_new_cols = ["sector_no", "department_no", "group_no", "subgroup_no"]

# Select 1 if columns are identical in both files
identical_columns = 0

# Column names
store_no_old = 'Shop Code' # Store number column name in old file
value_old = 'Value' # Sales value column name in old file
description_old = 'Description' # Description column name in old file
ean_old = 'EAN' # EAN column name in old file

# If columns are not identical define names for columns in new file, else copy names from old file
if identical_columns == 0:
    store_no_new = 'store_no' # Store number column name in new file
    value_new = 'value' # Sales value column name in new file
    description_new = 'item_name' # Description column name in new file
    ean_new = 'ean' # EAN column name in new file
else:
    store_no_new = store_no_old
    value_new = value_old
    description_new = description_old
    ean_new = ean_old

# If both files share identical headers, use the same column names
if add_headers == 0:
    store_no_old    = store_no_new
    value_old       = value_new
    description_old = description_new
    ean_old         = ean_new

#
## MAIN SCRIPT
#

# Get directory
script_dir = os.path.dirname(os.path.abspath(__file__))

# Get folder directories
folder_old = os.path.join(script_dir, 'input_old')
folder_new = os.path.join(script_dir, 'input_new')

# Get filename
def get_file_name(folder, extension):
    for f in os.listdir(folder):
        if f.endswith(extension):
            return f

# Merge full filename
filename_old = get_file_name(folder_old, extension_old)
filename_new = get_file_name(folder_new, extension_new)

# Full file paths
path_old = os.path.join(folder_old, filename_old)
path_new = os.path.join(folder_new, filename_new)

# Output report path
output_excel_path = os.path.join(script_dir, "report.xlsx")

# Load data into dataframe
if add_headers == 0:
    # Both files have identical headers; read old file with its header row
    df_old = pd.read_csv(path_old, sep=oldsep, encoding='ISO-8859-2', low_memory=False, dtype=str)
else:
    # Old file has no headers; use the predefined headers_old
    df_old = pd.read_csv(path_old, sep=oldsep, encoding='ISO-8859-2',
                         header=None, names=headers_old,
                         low_memory=False, dtype=str)

# Load data from excel file or csv, txt file
if path_new.endswith('.xlsx'):
    df_new = pd.read_excel(path_new, dtype=str)
elif path_new.endswith(('.csv', '.txt')):
    df_new = pd.read_csv(path_new, encoding='ISO-8859-2', sep=newsep, low_memory=False, dtype=str)
else:
    raise ValueError(f"Unsupported file format for new file: {path_new}")

# Convert EANs to strings
df_old[ean_old] = df_old[ean_old].astype(str).str.strip()
df_new[ean_new] = df_new[ean_new].astype(str).str.strip()

## Hierarchy

# Add hierarchy if enabled
if add_hierarchy == 1:
    hierarchy_path = os.path.join(script_dir, hierarchy_filename)
    hierarchy_df = pd.read_excel(hierarchy_path, header=None, dtype=str)

    # Select columns 0, 2, 4, 6 and key column 5
    hierarchy_df_selected = hierarchy_df[[5, 0, 2, 4, 6]].dropna()
    hierarchy_df_selected.columns = [
        hierkey,
        hiersector, hierdepartment, hiergroup, hierclass
    ]

    # Merge with df_old
    df_old = df_old.merge(hierarchy_df_selected, on=hierkey, how='left')


# Prepare hierarchy 
hierarchy_old = df_old[[ean_old] + hierarchy_old_cols].drop_duplicates()
hierarchy_new = df_new[[ean_new] + hierarchy_new_cols].drop_duplicates()

# Match ean column name
if ean_new != ean_old:
    hierarchy_new = hierarchy_new.rename(columns={ean_new: ean_old})

# Change column names for comparison adding suffixes
hierarchy_old = hierarchy_old.rename(columns={col: f"{col}_old" for col in hierarchy_old_cols})
hierarchy_new = hierarchy_new.rename(columns={col: f"{col}_new" for col in hierarchy_new_cols})

# Merge data to compare hierarchy
hierarchy_compare = pd.merge(hierarchy_old, hierarchy_new, on=ean_old, how="inner")

# Compare hierarchy
diff_mask = pd.Series([False] * len(hierarchy_compare))
hierarchy_compare = hierarchy_compare.fillna('')
for h_old, h_new in zip(hierarchy_old_cols, hierarchy_new_cols):
    diff_mask |= hierarchy_compare[f"{h_old}_old"] != hierarchy_compare[f"{h_new}_new"]

hierarchy_diff = hierarchy_compare[diff_mask]

## Sales, rowcount, size check
# Convert sales to floats
df_old[value_old] = pd.to_numeric(df_old[value_old].astype(str).str.replace(',', '.', regex=False), errors='coerce')
df_new[value_new] = pd.to_numeric(df_new[value_new].astype(str).str.replace(',', '.', regex=False), errors='coerce')

# Variables to compare
size_old = os.path.getsize(path_old)
size_new = os.path.getsize(path_new)
rowcount_old = len(df_old)
rowcount_new = len(df_new)

# Sum Store sales per store
stores_old = df_old.groupby(store_no_old)[value_old].sum()
stores_new = df_new.groupby(store_no_new)[value_new].sum()

# Summary 
summary_data = {
    'Metric': ['File Size (Bytes)', 'Row Count', 'Unique Stores', 'Total Sales Value'],
    'Old': [size_old, rowcount_old, stores_old.count(), df_old[value_old].sum()],
    'New': [size_new, rowcount_new, stores_new.count(), df_new[value_new].sum()],
    'Difference (%)': [
        round((size_new / size_old - 1) * 100, 2),
        round((rowcount_new / rowcount_old - 1) * 100, 2),
        round((stores_new.count() / stores_old.count() - 1) * 100, 2),
        round((df_new[value_new].sum() / df_old[value_old].sum() - 1) * 100, 2)
    ]
}

df_summary = pd.DataFrame(summary_data)

# Compare store sales
store_comparison = pd.DataFrame({
    'Old Sales': stores_old,
    'New Sales': stores_new
})
store_comparison['Difference (%)'] = ((store_comparison['New Sales'] / store_comparison['Old Sales']) - 1) * 100
store_comparison = store_comparison.round(2)


## Descriptions compare
# Remove duplicate EANs before setting index
desc_old = df_old.drop_duplicates(subset=ean_old).set_index(ean_old)[description_old]
desc_new = df_new.drop_duplicates(subset=ean_new).set_index(ean_new)[description_new]

# Align indexes to avoid reindexing errors
common_eans = desc_old.index.intersection(desc_new.index)

# Create comparison DataFrame only for common EANs
desc_diff = pd.DataFrame({
    'Old Description': desc_old.loc[common_eans].fillna(''),
    'New Description': desc_new.loc[common_eans].fillna('')
})

# Filter rows where descriptions differ
desc_diff = desc_diff[desc_diff['Old Description'] != desc_diff['New Description']]

# Create comparison keys
if not_in_new == 1 or not_in_old == 1:
    df_old['key'] = (
        df_old[store_no_old].astype(str).str.strip() + "_" +
        df_old[ean_old].astype(str).str.strip() + "_" +
        df_old[value_old].round(2).astype(str)
    )

    df_new['key'] = (
        df_new[store_no_new].astype(str).str.strip() + "_" +
        df_new[ean_new].astype(str).str.strip() + "_" +
        df_new[value_new].round(2).astype(str)
    )

    # Find rows in old but not in new
    old_not_in_new = df_old[~df_old['key'].isin(df_new['key'])]

    # Find rows in new but not in old
    new_not_in_old = df_new[~df_new['key'].isin(df_old['key'])]

## Generate Excel report
with pd.ExcelWriter(output_excel_path, engine='openpyxl') as writer:
    df_summary.to_excel(writer, sheet_name='Summary', index=False)
    store_comparison.to_excel(writer, sheet_name='Store Sales Comparison')
    desc_diff.to_excel(writer, sheet_name='Description Differences')
    hierarchy_diff.to_excel(writer, sheet_name='Hierarchy Differences', index=False)
    if not_in_new == 1:
        old_not_in_new.to_excel(writer, sheet_name='Old Not In New', index=False)
    if not_in_old == 1:
        new_not_in_old.to_excel(writer, sheet_name='New Not In Old', index=False)


print(f"Excel report generated at: {output_excel_path}")
