import pandas as pd
import sys, re, json

df = pd.read_csv(sys.argv[1],dtype=str)

def clean(c):
    ret = re.sub(r'[^a-z0-9]+','_',c.lower().strip())
    return ret

df.columns = map(clean,df.columns)


# open(sys.argv[2],"w").write(df.to_json())
# print df.dtypes

# outfh = open(sys.argv[2],"w")
# print df.to_json()
# outfh.write("[")
# for obj, i in df.iterrows():
#     print i
print df.to_csv(index=False())
