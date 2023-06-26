import sys
import time
import boto3

JOB_JAR = "s3://sparkJob-assembly-0.1.0-SNAPSHOT.jar"

def lambda_handler(event, context):
    conn = boto3.client("emr")
    clusters = conn.list_clusters()
    clusters = [c["Id"] for c in clusters["Clusters"] 
                if c["Status"]["State"] in ["RUNNING", "WAITING"]]
    print (f"clusters = {clusters}")
    if not clusters:
        sys.stderr.write("No valid clusters\n")
        sys.stderr.exit()
    # take the first relevant cluster
    cluster_id = clusters[0]
    CODE_DIR = "/home/hadoop/code/"
    step =  {
            "Name": "Main spark-submit job",
            "ActionOnFailure": 'CONTINUE',
            'HadoopJarStep': {
                "Jar": "command-runner.jar",
                "Args": [
                    "spark-submit",
                    "--deploy-mode",
                    "cluster",
                    "--class", "dev.SparkApp3",
                    "s3://sparkJob-assembly-0.1.0-SNAPSHOT.jar"
                ]
            }

        }
    print (f"step = {step}")
    action = conn.add_job_flow_steps(JobFlowId=cluster_id, Steps=[step])
    return "Added step: %s"%(action)