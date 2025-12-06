# Task-1: Exploratory Data Analysis on Insurance Dataset

## **Objective**

The goal of Task-1 is to perform a comprehensive **Exploratory Data Analysis (EDA)** on an insurance dataset. The dataset contains demographic and insurance-related information for policyholders. This task helps understand the data distribution, relationships between variables, and potential anomalies or outliers.

---

## **Dataset Description**

The dataset used in this task (`insurance_data.csv`) contains the following columns:

| Column Name | Description                                   |
| ----------- | --------------------------------------------- |
| `age`       | Age of the policyholder                       |
| `sex`       | Gender of the policyholder (male/female)      |
| `bmi`       | Body Mass Index of the policyholder           |
| `children`  | Number of children/dependents                 |
| `smoker`    | Whether the policyholder is a smoker (yes/no) |
| `region`    | Residential region of the policyholder        |
| `charges`   | Insurance charges for the policyholder        |

---

## **Steps Performed**

### **1. Basic Information**

* Checked the shape, columns, and datatypes of the dataset.
* Identified missing values.
* Calculated descriptive statistics for numeric variables.

### **2. Univariate Analysis**

* **Numeric columns (`age`, `bmi`, `children`, `charges`)**

  * Plotted histograms with KDE to examine distribution and skewness.
* **Categorical columns (`sex`, `smoker`, `region`)**

  * Count plots to observe category frequencies.

### **3. Bivariate Analysis**

* Examined relationships between numeric variables and `charges` using scatter plots.
* Compared `charges` across categories (`sex`, `smoker`, `region`) using boxplots.

### **4. Correlation Analysis**

* Plotted a heatmap of numeric variables to identify correlations.

### **5. Outlier Detection**

* Boxplots for numeric variables to identify potential outliers.

### **6. Pairwise Relationships**

* Optional pairplot to visualize pairwise interactions, colored by `smoker` status.

---

## **Libraries Used**

* `pandas` – for data manipulation.
* `numpy` – for numerical operations.
* `matplotlib.pyplot` – for plotting.
* `seaborn` – for statistical visualizations.

---

## **How to Run**

1. Install required libraries (if not installed):

   ```bash
   pip install pandas numpy matplotlib seaborn
   ```
2. Place the `insurance_data.csv` file in the `data` folder (or update the path in the script).
3. Run the Python script:

   ```bash
   python task1_eda.py
   ```
4. Visualizations will be displayed for each step of the analysis.

---

## **Outcome**

* Clear understanding of data distributions.
* Identification of correlations and patterns.
* Detection of potential outliers.
* Insights into the effect of factors like `age`, `bmi`, `smoker`, and `region` on insurance charges.
