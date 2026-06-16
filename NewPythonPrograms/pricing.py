import boto3
import requests
client = boto3.client('ce',region_name='ap-south-1')
response = client.get_cost_and_usage(
    TimePeriod={
        'Start': '2026-03-01',
        'End': '2026-03-31'        
},
Granularity='MONTHLY',
    Metrics=[
        'AmortizedCost',
    ]
)
#results=requests.get(response)
value=response['ResultsByTime'][0]['Total']['AmortizedCost']['Amount']
print(response)
print("the current billing for the month is $",round(float(value),3))
