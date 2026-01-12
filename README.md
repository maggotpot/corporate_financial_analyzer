# Corporate Financial Statement Analyzer

## Project Overview
This project is a financial analysis tool designed to automatically collect, analyze, and visualize financial statement data for publicly listed companies.

The project replicates the type of analytical work performed in corporate finance, consulting, equity research, and audit/transaction services.

## Project Objectives
- Demonstrate strong financial statement literacy
- Apply financial ratio analysis in a practical context
- Showcase automation and data analytics skills using Python
- Communicate insights clealry through data visualization

## Companies Analyzed
- Apple Inc. (AAPL) - Technology
- Coca-Cola Co. (KO) - Consumer Staples
- JPMorgan Chase & Co. (JPM) - Financial Services

## Data Sources
Financial data is retrieved using Yahoo Finance API via the yfinance Python library.

Financial statements collected:
- Income Statement
- Balance Sheet
- Cash Flow Statement

!All data is historical and publicly available!

## Tools & Technologies 
- Python
- Pandas & NumPy
- yfinance
- matplotlib
- seaborn

## Financial Ratios Calculated
- LIQUIDITY RATIOS: Current Ratio
- PROFITABILITY RATIOS: Net Profit Margin & ROA
- SOLVENCY RATIOS: Debt-to-Equity Ratio

!!! Due to variations in financial statement structures across companies and reporting periods, not all ratios are available for every firm. The model explicitly handles missing data to ensure analytical integrity. !!!

## Results & Insights
()

## Limitations
- Yahoo Finance data may differ slightly from official SEC filings
- Direct comparability is limited due to accounting differences across sectors
- No valuation model in base version