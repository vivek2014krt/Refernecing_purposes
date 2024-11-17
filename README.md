# Refernecing_purposes
from pyspark.sql import SparkSession

# Create SparkSession with Kerberos authentication
spark = (
    SparkSession.builder
    .appName("Kerberos_Jupyter_Session")  # Replace with your app name
    .config("spark.master", "yarn")  # Use YARN as the cluster manager
    .config("spark.submit.deployMode", "client")  # Run in client mode
    .config("spark.yarn.principal", "your_username@YOUR.REALM.COM")  # Kerberos principal
    .config("spark.yarn.keytab", "/path/to/your.keytab")  # Path to the keytab file
    .config("spark.hadoop.fs.defaultFS", "hdfs://your-hdfs-cluster")  # Default Hadoop filesystem
    .config("spark.hadoop.security.authentication", "kerberos")  # Enable Kerberos
    .config("spark.hadoop.security.authorization", "true")  # Enable authorization
    .getOrCreate()
)

# Verify the session
print("Spark session created successfully.")
