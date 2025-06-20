import sys
import yaml
import os

def load_fields(filename="pod-spec-fields.yaml"):
    if not os.path.exists(filename):
        print(f"Error: {filename} not found.")
        sys.exit(1)
    with open(filename, encoding="utf-8") as f:
        try:
            return yaml.safe_load(f)
        except yaml.YAMLError as e:
            print(f"Error parsing {filename}: {e}")
            sys.exit(1)

def search(term, fields):
    term = term.lower()
    results = []
    for field, data in fields.items():
        if term in field.lower():
            results.append((field, data))
            continue
        if 'description' in data and term in data['description'].lower():
            results.append((field, data))
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 search.py <field or description keyword>")
        sys.exit(1)
    term = " ".join(sys.argv[1:]).strip()
    fields = load_fields()
    results = search(term, fields)
    if not results:
        print(f"No matches found for '{term}'.")
    else:
        for field, data in results:
            print(f"\033[1mField: {field}\033[0m")
            print(f"Description: {data.get('description','No description available.')}\n")
            print("Sample YAML:\n")
            print(data.get('sample', 'No sample available.').strip())
            print('-' * 60)
