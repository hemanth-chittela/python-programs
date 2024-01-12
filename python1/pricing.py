import boto3
client = boto3.client('ce',region_name='ap-south-1')

response = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2024-01-01',
        'End': '2024-01-31'        
},
Granularity='MONTHLY',
    Metrics=[
        'AmortizedCost',
    ]
)

value=response['ResultsByTime'][0]['Total']['AmortizedCost']['Amount']
print("the current billing for the month is $",round(float(value),2))
