import argparse
import boto3

ec2 = boto3.resource('ec2')

# Define command-line arguments
parser = argparse.ArgumentParser(description='Create a VPC and an Internet Gateway')
parser.add_argument('--name', metavar='NAME', type=str, required=True, help='name of the VPC')
parser.add_argument('--cidr', metavar='CIDR', type=str, default='10.0.0.0/16', help='CIDR block for the VPC')
parser.add_argument('--region', metavar='REGION', type=str, default='us-east-1', help='AWS region to create the VPC in')

# Parse command-line arguments
args = parser.parse_args()

# Create VPC
vpc = ec2.create_vpc(CidrBlock=args.cidr)

# Add tags to VPC
vpc.create_tags(Tags=[{"Key": "Name", "Value": args.name}])

# Create Internet Gateway
igw = ec2.create_internet_gateway()

# Attach Internet Gateway to VPC
igw.attach_to_vpc(VpcId=vpc.id)

# Add name tag to Internet Gateway
igw.create_tags(Tags=[{"Key": "Name", "Value": args.name + "-igw"}])

# Print results
print("VPC created with ID:", vpc.id)
print("Internet Gateway created with ID:", igw.id)
