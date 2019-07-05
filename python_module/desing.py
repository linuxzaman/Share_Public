#!/bin/bash/env python3

def design():
    title="Amazon Web Services"
    d="|"
    data = [
"Amazon EC2",
"Amazon Elastic Container Registry",
"Amazon Elastic Container Service",
"AWS Lambda",
"Amazon Virtual Private Cloud",
"AWS Elastic Beanstalk",
"Auto Scaling",
"Elastic Load Balancing",
"Amazon S3",
"Amazon EBS",
"Amazon Glacier",
"AWS Storage Gateway",
"Amazon RDS",
"Amazon DynamoDB",
"Amazon ElastiCache",
"Amazon Redshift",
"Amazon CloudFront",
"AWS Direct Connect",
"AWS CodeDeploy",
"Amazon CloudWatch",
"Amazon EC2 Systems Manager",
"Amazon CloudFormation",
"AWS CloudTrail",
"AWS Config",
"Amazon API Gateway",
"AWS Management Console",
"AWS IAM",
"Amazon EMR",
"Amazon Kinesis",
"Amazon SWF",
"Amazon SQS",
"Amazon SNS",
"AWS Premium Support",
"AWS IoT Platform",
"AWS Deep Learning AMIs",
"AWS Server Migration Service",
"AWS CodeBuild",
"Amazon GameLift",
"Amazon Polly",
"AWS PrivateLink",
"AWS IoT Device Management",
"AWS Step Functions",
"AWS Elemental MediaConvert",
"AWS Key Management Service",
"AWS License Manager",
"AWS IoT Greengrass"]
    #add=input("Enter topic name:")
    print(title)
    cnt=1
    for i in data:
        e="-"
        h=3*e + i
        u = d+h
        print(u)
        #cnt=cnt+1
design()
