import marimo

__generated_with = "0.2.3"
app = marimo.App()


@app.cell
def __():
    import marimo as mo
    return mo,


@app.cell
def __(mo):
    mo.md("# Project 3, Group 2 Marimo Tool")
    return


@app.cell
def __(mo):
    mo.md("Welcome to our tool! This application was created using Marimo notebook and the Marimo library. Please feel free to interact with the sliders. The weight you prescribe to each data set influences the zip code recommended by the program.")
    return


@app.cell
def __(mo):
    crime_slider = mo.ui.slider(0, 10, label= "Violent Crime Rate")
    crime_slider
    return crime_slider,


@app.cell
def __(mo):
    crime_slider_2 = mo.ui.slider(0, 10, label= "Non-Violent Crime Rate")
    crime_slider_2
    return crime_slider_2,


@app.cell
def __(mo):
    build_rate_slider = mo.ui.slider(0, 10, label= "New Build Rate (lowest to highest)")
    build_rate_slider
    return build_rate_slider,


@app.cell
def __(mo):
    #can we make this a range filter?
    price_trend_slider = mo.ui.slider(0,10, label= "Pricing Trend (lowest prices to highest)")
    price_trend_slider
    return price_trend_slider,


if __name__ == "__main__":
    app.run()
