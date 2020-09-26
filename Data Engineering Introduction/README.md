# Data Engineering 101

This is a simple data engineering project that extracts the top headlines from a news website that has been created and loads them into a csv file then stores it in an AWS S3 Bucket.

### Steps to use the project

- Run the index.html file on the specified port.
- Create a file called `auth.py` and specify the AWS credentials as follows:
  ```
  ACCESS_KEY="<YOUR-ACCESS-KEY-HERE>"
  SECRET_KEY="<YOUR-SECRET-KEY-HERE>"
  ```
- Install all the python packages mentioned in the `requirements.txt`.
- Make sure to change the bucket name where I've used `aws-data-engineering-csv-etl-pipeline-demo`.
- Run the `script.py` file.

### Result

A `data.csv` file is created locally in the project directory and also it gets loaded in your AWS S3 Bucket.