

# Check if a Spark session is running
try:
    if spark:
        print("A Spark session is running.")
        print("Spark application name:", spark.sparkContext.appName)
    else:
        print("No active Spark session.")
except NameError:
    print("No Spark session variable exists.")
