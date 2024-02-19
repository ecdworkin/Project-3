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

    #print(median_income_df)
    return


@app.cell
def __():
    #read in crime rate CSV

    return


@app.cell
def __(pd):
    #read in population CSV.
    population_data = "Population Data CSV.csv"
    population_data_df = pd.read_csv(population_data)
    population_data_df['Population Rank'] = population_data_df['% Change'].rank(method='dense', ascending=True).astype(int)
    #NOTE: We used ascending to assign rank so that the slider weight can be multiplied by the rank (desireability score will be highest number) 
    #print(population_data_df)
    return population_data, population_data_df


@app.cell
def __():
    #read in pricing trend CSV
    return


@app.cell
def __():
    #merge dataframes on zip code?
    return


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
    population_slider = mo.ui.slider(0, 10, label= "Population Growth")
    population_slider
    return population_slider,


@app.cell
def __(mo):
    median_income_slider = mo.ui.slider(0, 10, label= "High Median Income")
    median_income_slider
    return median_income_slider,


@app.cell
def __():
    #price_trend_slider = mo.ui.slider(0,10, label= "Pricing Trend (lowest prices to highest)")
    #price_trend_slider
    return


@app.cell
def __(df, slider1, slider2, slider3, slider4):
    #area to display/calculate top zip codes
    def calculate_scores():
        df['score'] = df['var1'] * slider1.value + df['var2'] * slider2.value + \
                      df['var3'] * slider3.value + df['var4'] * slider4.value
        return df.sort_values('score', ascending=False)['zip_code'].head(5).tolist()


    return calculate_scores,


@app.cell
def __(calculate_scores, top_zip_codes_text):
    # Function to update the list of top zip codes
    def update_list():
        top_zip_codes = calculate_scores()
        top_zip_codes_text.content = '\n'.join(top_zip_codes)
    return update_list,


@app.cell
def __(median_income_slider, population_slider_slider, update_list):
    # Connect the sliders to the update_list function
    #crime_slider.observe(update_list, names='value')
    #crime_slider_2.observe(update_list, names='value')
    #build_rate_slider.observe(update_list, names='value')
    #price_trend_slider.observe(update_list, names='value')
    median_income_slider.observe(update_list, names='value')
    population_slider_slider.observe(update_list, names='value')
    return


@app.cell
def __(Text, update_list):
    # Display the top zip codes
    top_zip_codes_text = Text()
    update_list(None)  # Initial update
    return top_zip_codes_text,


@app.cell
def __(mo):
    mo.md("**Notes on Our Tool:**")
    return


@app.cell
def __(mo):
    mo.md("-Pricing Trends prefers upward trends in pricing from [insert year] to [insert year]")
    return


@app.cell
def __(mo):
    mo.md("-Population Growth prefers upward trends in population from 2020 to 2023")
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
