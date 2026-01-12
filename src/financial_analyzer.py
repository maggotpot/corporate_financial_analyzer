# Corporate Financial Data Analyzer
# Author: Elena Bulajic

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

TICKERS = ["AAPL", "KO", "JPM"]


def get_financial_statements(ticker):
    company = yf.Ticker(ticker)

    income_stmt = company.financials.T # Transpose for easier reading
    balance_sheet = company.balance_sheet.T
    cash_flow = company.cashflow.T

    return income_stmt, balance_sheet, cash_flow


def calculate_ratios(income, balance):
    """
    Calculates financial ratios with proper index alignment.
    """

    # Align years (intersection only)
    common_years = income.index.intersection(balance.index)
    income = income.loc[common_years]
    balance = balance.loc[common_years]

    ratios = pd.DataFrame(index=common_years)

    # Liquidity
    if "Current Assets" in balance.columns and "Current Liabilities" in balance.columns:
        ratios["Current Ratio"] = (
            balance["Current Assets"] /
            balance["Current Liabilities"]
        )

    # Profitability
    if "Net Income" in income.columns and "Total Revenue" in income.columns:
        ratios["Net Profit Margin"] = (
            income["Net Income"] / income["Total Revenue"]
        )

    if "Net Income" in income.columns and "Total Assets" in balance.columns:
        ratios["Return on Assets (ROA)"] = (
            income["Net Income"] / balance["Total Assets"]
        )

    # Solvency
    if (
        "Total Liabilities Net Minority Interest" in balance.columns and
        "Stockholders Equity" in balance.columns
    ):
        ratios["Debt to Equity"] = (
            balance["Total Liabilities Net Minority Interest"] /
            balance["Stockholders Equity"]
        )

    return ratios


def plot_ratio(ratios_dict, ratio_name):
    """
    Plots a financial ratio over time for all companies
    and automatically saves the chart in the 'charts' folder.
    """

    # Define the folder inside the function
    charts_folder = "charts"
    if not os.path.exists(charts_folder):
        os.makedirs(charts_folder)

    plt.figure(figsize=(8, 5))
    plotted = False

    for ticker, ratios in ratios_dict.items():
        if ratio_name in ratios.columns:
            series = ratios[ratio_name].dropna()
            if not series.empty:
                plt.plot(series.index, series.values, marker="o", label=ticker)
                plotted = True

    if plotted:
        plt.title(f"{ratio_name} Over Time")
        plt.xlabel("Year")
        plt.ylabel(ratio_name)
        plt.legend()
        plt.grid(True)
        plt.tight_layout()

        # Saved to charts folder
        filepath = os.path.join(charts_folder, f"{ratio_name.replace(' ', '_').lower()}.png")
        plt.savefig(filepath)
        print(f"Saved {filepath}")

        plt.show()
    else:
        print(f"No data available to plot {ratio_name}")


def build_comparison_table(ratios_dict):
    """
    Builds a comparison table using average available ratios.
    """

    comparison = pd.DataFrame()

    for ticker, ratios in ratios_dict.items():
        if "Net Profit Margin" in ratios.columns:
            comparison.loc[ticker, "Avg Net Profit Margin"] = ratios["Net Profit Margin"].mean()
        if "Debt to Equity" in ratios.columns:
            comparison.loc[ticker, "Avg Debt to Equity"] = ratios["Debt to Equity"].mean()

    return comparison



if __name__ == "__main__":
    
    all_ratios = {}

    for ticker in TICKERS:
        income, balance, cashflow = get_financial_statements(ticker)
        ratios = calculate_ratios(income, balance)
        all_ratios[ticker] = ratios
        print(f"\n--- {ticker} BALANCE SHEET COLUMNS ---")
        print(balance.columns.tolist())

        print(f"\n--- {ticker} INCOME STATEMENT COLUMNS ---")
        print(income.columns.tolist())
        ratios_clean = ratios.dropna(how="all")
        print(ratios_clean.round(3))
    
    plot_ratio(all_ratios, "Net Profit Margin")
    plot_ratio(all_ratios, "Debt to Equity")

    comparison_table = build_comparison_table(all_ratios)

    print("\n--- Company Comparison (Averages) ---")
    print(comparison_table.round(3))