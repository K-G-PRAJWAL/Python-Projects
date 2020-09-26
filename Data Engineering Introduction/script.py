from bs4 import BeautifulSoup
import requests
import csv
import boto3
from auth import ACCESS_KEY, SECRET_KEY

# Get data from the site and store in CSV file
soup = BeautifulSoup(requests.get('http://127.0.0.1:5500/').text, 'lxml')
csv_file = open('data.csv', 'w', newline='')
writer = csv.writer(csv_file)

articles = soup.find_all('article')
writer.writerow(['header', 'summary', 'link'])

for article in articles:
    headline = article.h2.a.text
    summary = article.p.text
    link = article.h2.a["href"]
    writer.writerow([headline, summary, link])

csv_file.close()


# Store to AWS S3 bucket
client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
)

client.create_bucket(Bucket='aws-data-engineering-csv-etl-pipeline-demo')
with open("data.csv", "rb") as f:
    client.upload_fileobj(f, "aws-data-engineering-csv-etl-pipeline-demo", "data.csv")
print('Task Completed Sucessfully!')