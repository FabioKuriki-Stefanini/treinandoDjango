import boto3

endpoint_url = "http://localhost.localstack.cloud:4566"
# alternatively, to use HTTPS endpoint on port 443:
# endpoint_url = "https://localhost.localstack.cloud"

def listarEC2s():
    ec2 = boto3.client("ec2", 
                        endpoint_url=endpoint_url,
                        region_name='us-east-1',
                        aws_access_key_id='test',
                        aws_secret_access_key='test',)
    resposta = ec2.describe_instances()
    print(resposta)
    

def criarEC2():
    ec2 = boto3.resource('ec2',
                        endpoint_url=endpoint_url,
                        region_name='us-east-1',
                        aws_access_key_id='test',
                        aws_secret_access_key='test',)
    
    ec2.create_instances(MaxCount=1,
                        MinCount=1)

if __name__ == "__main__":
    # criarEC2()
    listarEC2s()