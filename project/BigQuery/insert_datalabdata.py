# TODO(developer): Uncomment the lines below and replace with your values.#import blog_crawler
from google.cloud import bigquery
import crawl_NAVER_datalab

def insert(title, postdate):
    rows_to_insert = [(loc, date, ratio)] #schema

client = bigquery.Client(project = 'bigquery-259414')
dataset_id = 'blog_post'
# For this sample, the table must already exist and have a defined schema
table_id = 'datalab'
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)  # API request

rows_to_insert = crawl_NAVER_datalab.make_list()

errors = client.insert_rows(table, rows_to_insert)  # API request

assert errors == []




