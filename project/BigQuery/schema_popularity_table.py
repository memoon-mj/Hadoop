from google.cloud import bigquery

schema = [
    bigquery.SchemaField("full_name", "STRING", mode="REQUIRED"),
    bigquery.SchemaField("age", "INTEGER", mode="REQUIRED"),
]

# TODO(developer): Construct a BigQuery client object.
client = bigquery.Client(project = 'bigquery-259414')

# TODO(developer): Set table_id to the ID of the table to create
table_id = "bigquery-259414.poulartime.popularity"

table = bigquery.Table(table_id, schema=schema)
table = client.create_table(table)  # API request
print(
    "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
)