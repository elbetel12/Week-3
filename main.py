from src.eda import load_data, basic_info, univariate_analysis, bivariate_analysis, correlation_heatmap

NUMERIC_COLS = ['age', 'bmi', 'children', 'charges']
DATA_PATH = "data/insurance_data.csv"
PLOT_DIR = "plots"

def main():
    df = load_data(DATA_PATH)
    if df is None:
        return

    # Basic info
    basic_info(df)

    # Univariate analysis
    univariate_analysis(df, NUMERIC_COLS, PLOT_DIR)

    # Bivariate analysis
    bivariate_analysis(df, PLOT_DIR)

    # Correlation heatmap
    correlation_heatmap(df, NUMERIC_COLS, PLOT_DIR)

if __name__ == "__main__":
    main()
