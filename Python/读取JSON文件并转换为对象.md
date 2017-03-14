```python
import json


class JSONObject:
    def __init__(self, d):
        self.__dict__ = d
        
data = json.loads("data.json", object_hook=JSONObject)
```