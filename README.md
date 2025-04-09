# Sales Trend Analyzer

A data engineering project that processes retail sales data using PySpark, saves results with Pandas, and integrates with AWS S3 for cloud storage. This repository demonstrates skills in big data processing, cloud computing, and version control, built as a portfolio piece for showcasing technical proficiency.

## Project Overview
- **Purpose**: Analyze mock retail sales data to identify the top 5 products by total sales, then upload the results to AWS S3.
- **Technologies**: Python 3.11, PySpark, Pandas, AWS S3, AWS CLI, Git, PowerShell.
- **Output**: `top_products.csv` containing the top 5 products by total sales.

## Prerequisites
To run this project locally, ensure you have:
- Python 3.11 or higher
- PySpark (`pip install pyspark`)
- Pandas (`pip install pandas`)
- Faker (`pip install faker`)
- AWS CLI (configured with `aws configure` using your credentials)
- Git
- Hadoop `winutils.exe` (installed at `C:\hadoop\bin` with `HADOOP_HOME` set)

## Repository Structure
- `generate_data.py`: Generates 10,000 rows of mock sales data into `retail_sales_data.csv`.
- `analyze_sales.py`: Processes data with PySpark, identifies top 5 products, and saves to `top_products.csv` using Pandas.
- `upload_to_s3.ps1`: PowerShell script to upload `top_products.csv` to an S3 bucket.

## Setup and Execution
Follow these steps to replicate the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LihleDon/Sales-Trend-Analyzer.git
   cd Sales-Trend-Analyzer

2. **Generate Mock Data**:
  ```bash
  python generate_data.py

3. **Analyze Sales Data**:
  ```powershell
  $env:SPARK_LOCAL_HOSTNAME = "localhost"
  python analyze_sales.py

Outputs top_products.csv with the top 5 products.

4. **Upload to AWS S3**:
  ```powershell
  .\upload_to_s3.ps1

Creates sales-trend-analyzer-bucket, uploads top_products.csv, and lists the bucket contents.

5. **Clean Up S3 (Optional)**:
  ```powershell
  aws s3 rm s3://sales-trend-analyzer-bucket/output/top_products.csv
  aws s3 rb s3://sales-trend-analyzer-bucket --force

Results
Sample output from a recent run (April 9, 2025):

+----------+------------------+
|product_id|       total_sales|
+----------+------------------+
|  PROD_077|32037.230000000003|
|  PROD_091| 31917.67999999999|
|  PROD_082|31265.200000000004|
|  PROD_041|30798.160000000014|
|  PROD_038| 30705.73999999999|
+----------+------------------+

S3 Upload Confirmation: View `screenshots/s3_upload.png` (#)
Shows the successful upload of top_products.csv to S3 with bucket listing.

**Technical Challenges**
Overcame UnsatisfiedLinkError on Windows by switching from Spark’s native file writing to Pandas’ to_csv() method, ensuring compatibility.

**License**
This project is licensed under the MIT License. Feel free to use or adapt it as needed.
**Contact**
GitHub: LihleDon
Email: 1lihle001@gmail.com





