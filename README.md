# DATA-CLEANING-AND-PREPROCESSNG

## Dataset:
Netflix Movies and TV Shows from Kaggle.

## Steps Performed:
- Loaded dataset using Pandas.
- Filled missing values in `director` and `cast`.
- Removed rows with null `date_added`.
- Standardized country names (lowercase).
- Converted `date_added` to datetime format.
- Cleaned column headers (snake_case).
- Removed duplicate rows.
- Saved final cleaned data to `netflix_cleaned.csv`.
