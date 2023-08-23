from __future__ import print_function

import sys
import ruamel.yaml

# https://yaml.readthedocs.io/en/latest/detail.html

yaml = ruamel.yaml.YAML()  # defaults to round-trip


with open("conf2.yaml", "r") as yaml_file:
    data = yaml.load(yaml_file)

print(data)

data["abc"].append("b")
data["abc"].yaml_add_eol_comment("comment 4", 1)
# data["xyz"].yaml_add_eol_comment("comment 5", "c")
# data["xyz"].yaml_add_eol_comment("comment 6", "e")
# data["xyz"].yaml_add_eol_comment("comment 7", "d", column=20)
data["file"] = "gs://bucket-name/file.csv"

data.yaml_set_comment_before_after_key(
    "file", before="This comment will be placed above 'file' key"
)
data.yaml_set_comment_before_after_key(
    "abc", after="This will be place below 'abc:b' value."
)

data.yaml_set_comment_before_after_key("lucky", before="comment before 'lucky' key")
data.yaml_set_comment_before_after_key("lucky", after="comment after 'lucky' key")

data.yaml_set_comment_before_after_key(
    "file", before="This is the 'file' key.", indent=10
)

## added a new key and a comment beside it
data["key"] = "value"  # Updated value for 'key' key
data.yaml_add_eol_comment("Comment beside the value", key="key", column=20)

# key without a value
data["key2"] = ""
data.yaml_set_comment_before_after_key("key2", after="Here is my comment.", indent=0)

# print(type(data["xyz"]))

with open("output2.yaml", "w") as yaml_file:
    yaml.dump(data, yaml_file)


import site

print(site.getsitepackages())
