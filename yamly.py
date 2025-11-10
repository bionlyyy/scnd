import yaml
import json

def yaml_to_json(yaml_string):
    data = yaml.safe_load(yaml_string)
    return json.dumps(data, ensure_ascii=False, indent=2)


yaml_data = """
person:
  name: "Иван"
  age: 25
  hobbies:
    - программирование
    - музыка
"""

json_data = yaml_to_json(yaml_data)
print(json_data)