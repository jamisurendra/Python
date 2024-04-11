# Dept Wise Highest Salary
from pyspark.sql.functions import *

data=[('Genece' , 2 , 75000),
('𝗝𝗮𝗶𝗺𝗶𝗻' , 2 , 80000 ),
('𝗣𝗮𝗻𝗸𝗮𝗷' , 2 , 80000 ),
('Tarvares' , 2 , 70000),
('Marlania' , 4 , 70000),
('Briana' , 4 , 85000),
('𝗞𝗶𝗺𝗯𝗲𝗿𝗹𝗶' , 4 , 55000),
('𝗚𝗮𝗯𝗿𝗶𝗲𝗹𝗹𝗮' , 4 , 55000),  
('Lakken', 5, 60000),
('Latoynia' , 5 , 65000) ]
schema="emp_name string,dept_id int,salary int"
df=spark.createDataFrame(data,schema)


df1 = df.groupBy('dept_id').agg(min("salary").alias("Min_salary"), max("salary").alias("Max_Salary")).withColumnRenamed("dept_id","dept_id_new")

df2 = df.join(df1, df.dept_id == df1.dept_id_new, how = 'inner')
df3 = df2.filter("salary == Max_Salary").select('emp_name','salary','dept_id')

df3.display()
