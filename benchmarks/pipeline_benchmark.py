import time
from src.pipelines import etl

start = time.time()
df = etl.load_raw()
transformed = etl.transform(df)
etl.save_processed(transformed)
print(f"Elapsed: {time.time() - start:.2f}s")
