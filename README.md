<h1 align="center">Air Quality Dashboard</h1>

# Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Tech Stack](#tech-stack)
- [Data Source](#data-source)
- [Installation](#installation)

# Overview

This project analyzes and visualizes air quality data, including data wrangling, EDA, and a Streamlit dashboard for interactive exploration. It provides insights into air quality patterns, correlations, and trends in a specific region.

Please visit this link to view the deployed version [streamlit deployed](https://air-quality-dashboard-fg.streamlit.app/)

# Project Structure

```
├── dashboard/
    ├── dashboard.py    # dashboard code
    ├── df.csv          # cleaned dataset
├── data/               # original dataset
├── notebook.ipynb      # notebook for data analysis
├── README.md           # documentation for this project
├── requirements.txt    # dependencies used in the project
```

# Tech Stack

<a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue"/></a>
<a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter-F37626.svg?&style=for-the-badge&logo=Jupyter&logoColor=white"/></a>
<a href="https://pandas.pydata.org/"><img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white"/></a>
<a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"/></a>

# Data Source

Data used in this project is taken from [data-source](https://github.com/marceloreis/HTI/tree/master)

# Installation

1. Clone this repository

   ```bash
   git clone https://github.com/FrederickGodiva/Air-Quality-Dashboard.git
   ```

2. Create Python Virtual Environment

   ```bash
   virtualenv venv
   ```

3. Activate the Environment

   ```bash
   venv\Scripts\activate
   ```

4. Install all the requirements

   ```bash
   pip install -r requirements.txt
   ```

5. Run the streamlit dashboard

   ```bash
   streamlit run .\dashboard\dashboard.py
   ```

6. Stop the streamlit dashboard press `ctrl + c`

---

Copyright &copy; 2025 - Frederick Godiva
