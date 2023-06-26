#from aws_requests_auth.aws_auth import AWSRequestsAuth
import requests
import json
import boto3
import datetime as dt


AWS_ACCESS_KEY = ""
AWS_SECRET_ACCESS_KEY =  ""
USER_ALIAS = ""

def write_to_s3(s3_client, bucket_name, key_name, json_data):
    print(f"s3_client = {s3_client}, bucket_name = {bucket_name}, key_name = {key_name}, json_data = {json_data}")
    try:
        s3_client.put_object(Body=json.dumps(json_data), Bucket=bucket_name, Key=key_name)
    except Exception as e:
        print(f"s3 put object failed : {str(e)}")

def get_auth():
    return

def compute_snapshot(auth):
    url = ""
    headers = {"x-amz-user-alias": USER_ALIAS, "results-type": "direct"}
    url = url.format(USER_ALIAS=USER_ALIAS)
    print(f"url = {url}")
    print(f"headers = {headers}")
    response = requests.get(url, headers=headers, auth=auth, timeout=5)
    print(f"status code = {response.status_code}")
    query_id, total_chunks = response.json()["queryId"], response.json()["totalChunks"]
    return query_id, total_chunks

def get_download_chunk(auth, query_id, chunk):
    result = []
    headers = {'x-amz-user-alias' : USER_ALIAS}
    chunk_url = ""
    print(f"chunk_url = {chunk_url}")
    response = requests.get(chunk_url, headers=headers, auth=auth, timeout=5)
    resp_data = response.json()
    if resp_data["queryStatus"] == "complete":
        print("append result")
        result.append(response.json())
    return result

def cur_time_formatter(format):
    return dt.datetime.utcnow().strftime(format)

def lambda_handler(event, context):
    _client = boto3.client("sts")
    resp1 = _client.get_caller_identity()    
    cur_time, cur_date = cur_time_formatter('%Y-%m-%d-%H-%M-%S'), cur_time_formatter('%Y/%m/%d')
    _s3_client = boto3.client("s3")
    bucket_name = ""
    auth = get_auth()
    query_id, total_chunks = compute_snapshot(auth)
    print (f"query_id = {query_id}, total_chunks = {total_chunks}")    
    print(">>> write to s3 start")
    for chunk in range(total_chunks):
        json_data = get_download_chunk(auth, query_id, chunk)
        try:
            key_name = f"dev1/{cur_date}/{cur_time}-{chunk}.json"
            print (f"bucket_name = {bucket_name}, key_name =  {key_name}")
            write_to_s3(_s3_client, bucket_name, key_name, json_data)
            resp = {"status": "200", "statusDescription": "OK", "body": "write_to_s3 run OK"}
            print(">>> write to s3 OK")
        except Exception as e:
            print(f"error : {e}")
            raise e
        print(">>> write to s3 end")