from src.eda import load_data, basic_info, univariate_analysis, bivariate_analysis, correlation_heatmap

def main():
    df = load_data("data/insurance_data.csv")  # pipe-separated text file
    if df is not None:
        basic_info(df)
        univariate_analysis(df)
        bivariate_analysis(df)
        correlation_heatmap(df)

if __name__ == "__main__":
    main()
