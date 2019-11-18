from starbase import Connection
import csv

c = Connection()
ratings = c.table('ratings')
if(ratings.exists()):
    ratings.drop()
ratings.create('rating')

batch = ratings.batch()
if batch:
    print("batch update...\n")
    with open("C:/Users/NB42/Desktop/ml-latest-small/ratings.csv","r") as f:
        reader = csv.reader(f, delimiter = ',')
        next(reader)
        for row in reader:
            batch.update(row[0], {'rating':{row[1]:row[2]}})

    print("Committing...\n")
    batch.commit(finalize = True)

    print("Get ratings for users..\n")
    print("ratings for userid 1:")
    print(ratings.fetch("1"))
    print("\n")
    print("ratings for userid 33:")
    print(raings.fetch("33"))