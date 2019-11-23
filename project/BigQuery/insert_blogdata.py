# TODO(developer): Uncomment the lines below and replace with your values.#import blog_crawler
from google.cloud import bigquery
import ex_crawl

def insert(title, postdate):
    rows_to_insert = [(title,postdate,"1")]

client = bigquery.Client(project = 'bigquery-259414')
dataset_id = 'blog_post'
# For this sample, the table must already exist and have a defined schema
table_id = 'blog_title'
table_ref = client.dataset(dataset_id).table(table_id)
table = client.get_table(table_ref)  # API request

#ex_crawl.make_list("데이트", 1)
rows_to_insert = ex_crawl.make_list("데이트",20)
#rows_to_insert = [
    #('Phred Phlyntstone', "32","1"),
    #('naver','1',"2"),
    #('Wylma Phlyntstone', "29","2"),
#]
errors = client.insert_rows(table, rows_to_insert)  # API request

assert errors == []




