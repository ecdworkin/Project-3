import marimo

__generated_with = "0.2.3"
app = marimo.App()


@app.cell
def __():
    #library import section
    import marimo as mo
    import pandas as pd
    return mo, pd


@app.cell
def __(pd):
    #read in the income csv
    median_income = "Las Vegas Median Income - Zip Code.csv"
    median_income_df = pd.read_csv(median_income)
    #print(median_income_df)
    return median_income, median_income_df


@app.cell
def __():
    #read in crime rate CSV

    #create two new dfs from the csv - violent and non violent crime


    return


@app.cell
def __():
    #read in build rate CSV. Note: Build rate csv uses completions

    return


@app.cell
def __():
    #read in pricing trend CSV
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
    return


@app.cell
def __(mo):
    crime_slider = mo.ui.slider(0, 10, label= "Violent Crime Rate")
    crime_slider
    return crime_slider,


@app.cell
def __():
    #crime_slider_2 = mo.ui.slider(0, 10, label= "Non-Violent Crime Rate")
    #crime_slider_2
    return


@app.cell
def __():
    #build_rate_slider = mo.ui.slider(0, 10, label= "New Build Rate (lowest to highest)")
    #build_rate_slider
    return


@app.cell
def __(mo):
    population_slider = mo.ui.slider(0, 10, label= "Population Growth")
    population_slider
    return population_slider,


@app.cell
def __(mo):
    #can we make this a range filter?
    price_trend_slider = mo.ui.slider(0,10, label= "Pricing Trend (lowest prices to highest)")
    price_trend_slider
    return price_trend_slider,


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
def __(
    build_rate_slider,
    crime_slider,
    crime_slider_2,
    price_trend_slider,
    update_list,
):
    # Connect the sliders to the update_list function
    crime_slider.observe(update_list, names='value')
    crime_slider_2.observe(update_list, names='value')
    build_rate_slider.observe(update_list, names='value')
    price_trend_slider.observe(update_list, names='value')
    return


@app.cell
def __():
    return


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
