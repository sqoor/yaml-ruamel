import json
from ruamel.yaml import YAML

# Create a YAML instance
yaml = YAML()

# Load the YAML file with comments
with open("conf.yaml", "r") as yaml_file:
    yaml_data = yaml.load(yaml_file)


# Edit the YAML data
# yaml_data["name"] = "Jane Doe # updated"
# yaml_data["age"] = 35

yaml_data["abc"].append("b")
yaml_data["abc"].yaml_add_eol_comment("comment 4", 1)  # takes column of comment 1
yaml_data["xyz"].yaml_add_eol_comment("comment 5", "c")  # takes column of comment 2
yaml_data["xyz"].yaml_add_eol_comment("comment 6", "e")  # takes column of comment 3
yaml_data["xyz"].yaml_add_eol_comment("comment 7", "d", column=20)


# Save the changes to the YAML file while preserving comments
with open("output.yaml", "w") as yaml_file:
    yaml.dump(yaml_data, yaml_file)
