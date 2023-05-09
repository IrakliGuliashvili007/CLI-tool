import argparse
import boto3

# Parse command line arguments
parser = argparse.ArgumentParser(description='Create a VPC and associate an Internet Gateway with it')
parser.add_argument('name', metavar='NAME', type=str, help='name for the VPC')
args = parser.parse_args()

# Create a VPC with the given name
ec2 = boto3.resource('ec2')
vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
vpc.create_tags(Tags=[{'Key': 'Name', 'Value': args.name}])
vpc.wait_until_available()

# Create an Internet Gateway and attach it to the VPC
igw = ec2.create_internet_gateway()
igw.attach_to_vpc(VpcId=vpc.id)

print(f"VPC '{args.name}' ({vpc.id}) created with Internet Gateway '{igw.id}'")
