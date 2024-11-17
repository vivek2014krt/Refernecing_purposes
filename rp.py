

# Check if a Spark session is running
try:
    if spark:
        print("A Spark session is running.")
        print("Spark application name:", spark.sparkContext.appName)
    else:
        print("No active Spark session.")
except NameError:
    print("No Spark session variable exists.")

#spark session with kerberos (just trying)
spark = (
    SparkSession.builder
    .appName("Kerberos_Jupyter_Session")
    .config("spark.master", "yarn")
    .config("spark.submit.deployMode", "client")
    .config("spark.yarn.principal", "your_username@YOUR.REALM.COM")
    .config("spark.hadoop.fs.defaultFS", "hdfs://your-hdfs-cluster")
    .config("spark.hadoop.security.authentication", "kerberos")
    .config("spark.hadoop.security.authorization", "true")
    .getOrCreate()
)

