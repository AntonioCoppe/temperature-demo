# EPICA Dome C Temperature Stripes

This project visualizes 800,000 years of Antarctic temperature anomalies from the EPICA Dome C ice core using interactive "warming stripes" and bar charts. It includes both a web-based visualization (using Chart.js) and a Python script for generating a static image.

## Features

- **Interactive Web Visualization** (`index.html`)
  - Four views: Warming Stripes, Labelled Stripes, Bars, and Bars + Scale.
  - Data: EPICA Dome C Ice Core 800KYr Temperature Estimates.
  - Switch between views to explore the data with or without axis labels and scales.
  - Responsive design for desktop and mobile.

- **Python Script** (`show_stripes.py`)
  - Generates a static warming stripes image using Matplotlib.
  - Downloads the same dataset and produces a figure similar to the web version.

## Files

- `index.html`  
  Main web app. Open in your browser via a local server.

- `EPICA_Dome_C_Ice_Core_800KYr_Temperature_Estimates_229_35.csv`  
  The temperature anomaly dataset (Age in years BP, dT in °C).

- `show_stripes.py`  
  Python script to generate a static warming stripes image.

## Usage

### Web Visualization

1. Start a local server in the project directory:
   ```
   python3 -m http.server 8000
   ```
2. Open your browser and go to [http://localhost:8000/index.html](http://localhost:8000/index.html)
3. Use the buttons at the top to switch between visualization modes:
   - **Warming Stripes**: Minimalist, no axes.
   - **Labelled Stripes**: Adds time axis with 200,000-year ticks.
   - **Bars**: Shows temperature anomalies as bars, no axes.
   - **Bars + Scale**: Adds axes and grid for detailed inspection.

> All dependencies (Chart.js, PapaParse) are loaded via CDN. No installation required for the web app.

### Python Script

1. Install dependencies:
   ```
   pip install pandas matplotlib
   ```
2. Run the script:
   ```
   python show_stripes.py
   ```
   This will display a static warming stripes image using the same dataset.

## Data

- **Source**: EPICA Dome C Ice Core 800KYr Temperature Estimates
- **Columns**:  
  - `Age`: Years before present (BP)
  - `dT`: Temperature anomaly (°C)
- The dataset is filtered to ages ≤ 800,000 years BP.

## Credits

- Data: [EPICA Dome C Ice Core](https://www.nature.com/articles/nature02599)
- Visualization inspired by Ed Hawkins' "Warming Stripes" concept.
- Charting: [Chart.js](https://www.chartjs.org/), [PapaParse](https://www.papaparse.com/)
- Python: [Matplotlib](https://matplotlib.org/), [pandas](https://pandas.pydata.org/) 