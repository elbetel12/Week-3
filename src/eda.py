import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.utilis import create_folder

def load_data(filepath):
    """Load dataset with error handling."""
    try:
        df = pd.read_csv(filepath)
        return df
    except FileNotFoundError:
        print(f"Error: File {filepath} not found.")
        return None

def basic_info(df):
    """Print basic info about the dataset."""
    print("Shape:", df.shape)
    print("\nData Types:\n", df.dtypes)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nDescriptive Stats:\n", df.describe())

def univariate_analysis(df, numeric_cols, plot_dir="plots"):
    """Plot histograms for numeric columns."""
    create_folder(plot_dir)
    for col in numeric_cols:
        try:
            plt.figure(figsize=(7,4))
            sns.histplot(df[col], kde=True)
            plt.title(f"Distribution of {col}")
            plt.savefig(f"{plot_dir}/{col}_distribution.png")
            plt.close()
        except Exception as e:
            print(f"Could not plot {col}: {e}")

def bivariate_analysis(df, plot_dir="plots"):
    """Bivariate analysis: example with charges vs region and smoker."""
    create_folder(plot_dir)
    try:
        df['LossRatio'] = df['charges'] / df['charges'].mean()  # example
        plt.figure(figsize=(10,5))
        sns.boxplot(data=df, x="region", y="LossRatio")
        plt.xticks(rotation=45)
        plt.title("Loss Ratio by Region")
        plt.savefig(f"{plot_dir}/lossratio_by_region.png")
        plt.close()
    except Exception as e:
        print(f"Bivariate analysis failed: {e}")

def correlation_heatmap(df, numeric_cols, plot_dir="plots"):
    """Plot correlation heatmap."""
    create_folder(plot_dir)
    try:
        plt.figure(figsize=(8,6))
        sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='coolwarm')
        plt.title("Correlation Heatmap")
        plt.savefig(f"{plot_dir}/correlation_heatmap.png")
        plt.close()
    except Exception as e:
        print(f"Correlation heatmap failed: {e}")
