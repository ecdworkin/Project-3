import marimo

__generated_with = "0.2.3"
app = marimo.App()


@app.cell
def __():
    #library import section
    import marimo as mo
    import pandas as pd
    import numpy as np
    return mo, np, pd


@app.cell
def __(pd):
    #read in the income csv
    median_income = "Las Vegas Median Income - Zip Code.csv"
    median_income_df = pd.read_csv(median_income)
    income_columns = ['2018 Median income', '2019 Median income', '2020 Median income', '2021 Median income', '2022 Median income']

    for col in income_columns:
        # Remove commas and convert to numeric
        median_income_df[col] = median_income_df[col].str.replace(',', '').astype(float)
    return col, income_columns, median_income, median_income_df


@app.cell
def __(income_columns, median_income_df, np):
    # Calculate the slope for income
    def calculate_slope(row):
        # Filter out NaN values
        valid_data = row[income_columns].dropna()
        if len(valid_data) >= 2:  # Need at least two points to calculate slope
            # Get the corresponding years for the valid data
            valid_years = np.array([int(col.split()[0]) for col in valid_data.index])
            # Calculate the slope
            slope, _ = np.polyfit(valid_years, valid_data.values, 1)
            return slope
        else:
            return np.nan  # Not enough data to calculate slope

    # Apply the function to calculate the income trend
    median_income_df['Income Trend'] = median_income_df.apply(calculate_slope, axis=1)
    return calculate_slope,


@app.cell
def __(median_income_df):
    #add ranking for income
    median_income_df['Income Rank'] = median_income_df['Income Trend'].rank(method='dense', ascending=True).astype(int)
    median_income_df.rename(columns={'Zip Code': 'Zip'}, inplace=True)

    print(median_income_df)
    return


@app.cell
def __(pd):
    #read in population CSV.
    population_data = "Population Data CSV.csv"
    population_data_df = pd.read_csv(population_data)
    population_data_df['Population Rank'] = population_data_df['% Change'].rank(method='dense', ascending=True).astype(int)
    #NOTE: We used ascending to assign rank so that the slider weight can be multiplied by the rank (desireability score will be highest number) 
    print(population_data_df)
    return population_data, population_data_df


@app.cell
def __(pd):
    #read in pricing trend CSV
    pricing_file_path = "Resources/las_vegas_home_values_by_zip_codes.csv"
    pricing_df = pd.read_csv(pricing_file_path)
    pivoted_prices_df = pricing_df.pivot(index='ZipCode', columns='Date', values='Value').reset_index()
    pivoted_prices_df.columns.name = None
    pivoted_prices_df = pivoted_prices_df.rename(columns=lambda x: 'Value_' + x if x != 'ZipCode' else x)

    #print(pivoted_prices_df)
    return pivoted_prices_df, pricing_df, pricing_file_path


@app.cell
def __(np, pivoted_prices_df):
    #create the slope
    def calculate_pricing_slope(row):
        # Extract the non-null values and their corresponding dates
        row = row.drop(labels=['ZipCode'])
        values = row.dropna().values
        x_values = np.arange(len(values))

        # Perform linear regression if there are at least two points
        if len(values) >= 2:
            slope, intercept = np.polyfit(x_values, values, 1)
            return slope
        else:
            return np.nan

    # Apply the function to each row of the pivoted dataframe
    pivoted_prices_df['Slope'] = pivoted_prices_df.apply(calculate_pricing_slope, axis=1)

    #print(pivoted_prices_df)
    return calculate_pricing_slope,


@app.cell
def __(pivoted_prices_df):
    clean_prices_df = pivoted_prices_df[['ZipCode', 'Slope']]
    clean_prices_df = clean_prices_df.rename(columns={'ZipCode': 'Zip'})
    clean_prices_df['Pricing Rank'] = clean_prices_df['Slope'].rank(method='min')
    print(clean_prices_df)
    return clean_prices_df,


@app.cell
def __(clean_prices_df, median_income_df, pd, population_data_df):
    #merge dataframes on zip code and delete all frames other than rank
    merged_df = pd.merge(median_income_df, population_data_df, on='Zip')
    fully_merged_df = pd.merge(merged_df, clean_prices_df, on='Zip')
    rankings_df = fully_merged_df[['Zip', 'Population Rank', 'Income Rank', 'Pricing Rank']]
    print(rankings_df)
    return fully_merged_df, merged_df, rankings_df


@app.cell
def __(mo):
    mo.md("# Project 3, Group 2 Marimo Tool")
    return


@app.cell
def __(mo):
    mo.md("Welcome to our tool! This application was created using Marimo notebook and the Marimo library. Please feel free to interact with the sliders. The weight you prescribe to each data set influences the zip code recommended by the program.")
    return


@app.cell
def __():
    #crime_slider = mo.ui.slider(0, 10, label= "Violent Crime Rate")
    #crime_slider
    return


@app.cell
def __():
    #crime_slider_2 = mo.ui.slider(0, 10, label= "Non-Violent Crime Rate")
    #crime_slider_2
    return


@app.cell
def __(mo):
    price_trend_slider = mo.ui.slider(0,10, label= "Pricing Trend (lowest prices to highest)")
    price_trend_slider
    return price_trend_slider,


@app.cell
def __(mo):
    population_slider = mo.ui.slider(0, 10, label= "Population Growth")
    population_slider
    return population_slider,


@app.cell
def __(mo):
    median_income_slider = mo.ui.slider(0, 10, label= "High Median Income")
    median_income_slider
    return median_income_slider,


@app.cell
def __(
    median_income_slider,
    population_slider,
    price_trend_slider,
    rankings_df,
):
    # Values from sliders
    population_weight = population_slider.value
    income_weight = median_income_slider.value
    pricing_weight = price_trend_slider.value

    #def update_top_5_zips():
    # Calculate scores
    rankings_df.loc[:, 'Score'] = (rankings_df['Population Rank'] * population_weight) + \
        (rankings_df['Income Rank'] * income_weight) + \
        (rankings_df['Pricing Rank'] * pricing_weight)

    # Sort by score in descending order
    rankings_df_sorted = rankings_df.sort_values(by='Score', ascending=False)

    # Display the updated dataframe
    print(rankings_df_sorted)
    return (
        income_weight,
        population_weight,
        pricing_weight,
        rankings_df_sorted,
    )


@app.cell
def __(
    median_income_slider,
    mo,
    population_slider,
    rankings_df,
    top_5_zips_display,
):
    def update_top_5_zips():
     # Calculate scores and assign using .loc
        rankings_df.loc[:, 'Score'] = (rankings_df['Population Rank'] * population_slider.value) + \
                                      (rankings_df['Income Rank'] * median_income_slider.value)


        # Sort by score in descending order
        rankings_df_sorted = rankings_df.sort_values(by='Score', ascending=False)

        # Get the top 5 zip codes
        top_5_zips = rankings_df_sorted.head(5)['Zip'].tolist()

        # Convert the list of zip codes to a markdown string
        top_5_zips_md = ', '.join(str(zip_code) for zip_code in top_5_zips)

        # Update the markdown display with the new list of top 5 zip codes
        top_5_zips_display.update(f'Top 5 Zip Codes: {top_5_zips_md}')

        top_5_zips_md = ', '.join(str(zip_code) for zip_code in top_5_zips)

        # Display the top 5 zip codes in markdown
        mo.md("Top 5 Zip Codes: {top_5_zips_md}")
    return update_top_5_zips,


@app.cell
def __(rankings_df_sorted):
    #area to display/calculate top zip codes
    top_5_zips = rankings_df_sorted.head(5)
    print(top_5_zips)
    return top_5_zips,


@app.cell
def __(mo):
    mo.md("**Notes on Our Tool:**")
    return


@app.cell
def __(mo):
    mo.md("-Median Income prefers upward trends (using slope of line of best fit) in pricing from [2018] to [2022]")
    return


@app.cell
def __(mo):
    mo.md("-Population Growth prefers upward changes in population from 2020 to 2023")
    return


@app.cell
def __(mo):
    mo.md("**Sources**")
    return


@app.cell
def __(mo):
    mo.md("US Census Bureau")
    return


if __name__ == "__main__":
    app.run()
