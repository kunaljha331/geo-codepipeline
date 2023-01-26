import json
import pandas as pd

def lambda_handler(event, context):
    # TODO implement
    d={'col1':[1,2],'col2':[3,4]}
    df=pd.DataFrame(data=d)
    print(df)
    print('done1.0')
    print(event)
    print(context)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }