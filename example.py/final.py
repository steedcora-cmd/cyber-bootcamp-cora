# Group comments by emails, count comments.
# Save to comments.csv.

import pandas as pd
response = requests.get("https://jsonplaceholder.typicode.com/comments")
response.raise_for_status
data = response.json()
df = pd.DataFrame(data)
try:
print(df.head())
