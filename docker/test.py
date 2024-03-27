import boto3

def process_data(data):
    for item in data:
        if item == 'stop':
            break
        elif item == 'skip':
            continue
        else:
            print(item)

data = ['apple', 'banana', 'skip', 'cherry', 'stop', 'date']
process_data(data)

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        for item in self.data:
            if item == 'stop':
                break
            elif item == 'skip':
                continue
            else:
                yield item

data = ['apple', 'banana', 'skip', 'cherry', 'stop', 'date']
processor = DataProcessor(data)
for item in processor:
    print(item)


class CustomObject:
    def __init__(self, data):
        self.data = data

    def __contains__(self, item):
        return item in self.data

    def __not_contains__(self, item):
        return item not in self.data

obj = CustomObject(['apple', 'banana', 'cherry'])

if 'apple' in obj:
    print('Apple is in the object')

if 'orange' not in obj:
    print('Orange is not in the object')


    def create_iam_policy(policy_name, policy_document):
        iam_client = boto3.client('iam')
        response = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=policy_document
        )
        return response['Policy']['Arn']

    policy_name = 'UnrestrictedPolicy'
    policy_document = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "*",
                "Resource": "*"
            }
        ]
    }

    policy_arn = create_iam_policy(policy_name, policy_document)
    print(f"Created IAM policy with ARN: {policy_arn}")