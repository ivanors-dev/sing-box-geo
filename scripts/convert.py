import json
import yaml
import sys

# usage: python scripts/convert.py input.json output.yaml

json_file = sys.argv[1]
yaml_file = sys.argv[2]

with open(json_file, "r", encoding="utf-8") as f:
    data = json.load(f)

payload = []

for rule in data.get("rules", []):
    for d in rule.get("domain", []):
        payload.append(f"DOMAIN,{d}")
    for d in rule.get("domain_suffix", []):
        payload.append(f"DOMAIN-SUFFIX,{d}")
    for d in rule.get("domain_keyword", []):
        payload.append(f"DOMAIN-KEYWORD,{d}")
    if "domain_regex" in rule:
        payload.append(f"DOMAIN-REGEX,{rule['domain_regex']}")

yaml_data = {"payload": payload}

with open(yaml_file, "w", encoding="utf-8") as f:
    yaml.dump(yaml_data, f, allow_unicode=True, sort_keys=False)

print(f"✅ Convert {json_file} → {yaml_file}")
