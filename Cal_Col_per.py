#Calculate Percentage of eacch column

from pyspark.sql.functions import col

data = [("Raj","Doe",None),
 (None,"Samuel","VIZAG"),
 ("David","Smith", None),
 ("Samson",None, "HYD"),
 ("Immi", "Steve", "BNG"),
 (None, None, None)]

columns = ["Firstname", "Lastname", "City"]

df = spark.createDataFrame(data,columns)
df.cache()
for i in df.columns:
    total_count = df.select(col(i)).count()
    null_count = df.filter(col(i).isNull()).count()
    percentage = (null_count/total_count)*100
    print(i, percentage)
