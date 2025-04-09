# Define paths
$localFile = "C:\Users\Lihle\Downloads\GithubProjects\Sales-Trend-Analyzer\top_products.csv"
$s3Path = "s3://sales-trend-analyzer-bucket/output/top_products.csv"

# Create S3 bucket (if it doesn’t exist)
aws s3 mb s3://sales-trend-analyzer-bucket --region af-south-1

# Upload the file to S3
aws s3 cp $localFile $s3Path

# Verify the upload
aws s3 ls s3://sales-trend-analyzer-bucket/output/

# Confirmation message
Write-Host "Successfully uploaded top_products.csv to S3."