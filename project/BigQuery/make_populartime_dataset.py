from google.cloud import bigquery

# TODO(developer): Construct a BigQuery client object.
client = bigquery.Client(project = 'bigquery-259414')

# TODO(developer): Set dataset_id to the ID of the dataset to create.
dataset_id = "{}.populartime".format(client.project)

# Construct a full Dataset object to send to the API.
dataset = bigquery.Dataset(dataset_id)

# TODO(developer): Specify the geographic location where the dataset should reside.
dataset.location = "US"

# Send the dataset to the API for creation.
# Raises google.api_core.exceptions.Conflict if the Dataset already
# exists within the project.
dataset = client.create_dataset(dataset)  # API request
print("Created dataset {}.{}".format(client.project, dataset.dataset_id))