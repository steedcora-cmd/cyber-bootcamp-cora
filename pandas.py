iimport requests
import pandas as pd
response = requests.get("https://jsonplaceholder.typicode.com/comments")
data = response.json()
df = pd.DataFrame(data)
print(df.head())
