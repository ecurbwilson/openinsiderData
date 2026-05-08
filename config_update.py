#updates YAML file with preferences

import yaml

with open("config.yaml", "r") as read_file:
    contents = yaml.safe_load(read_file)
    contents['scraping']['start_year'] = 2026
    contents['scraping']['start_month'] = 4
    contents['filters']['min_transaction_value'] = 500000
    contents['filters']['transaction_types'] = 'P'
    print(contents)

with open("output.yaml", "w") as dump_file:
    yaml.dump(contents, dump_file)