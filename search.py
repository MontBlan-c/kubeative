import sys
import yaml

def load_fields():
    with open("pod-spec-fields.yaml") as f:
        return yaml.safe_load(f)

def search(term, fields):
    term = term.lower()
    results = []
    for field, data in fields.items():
        # Search field name
        if term in field.lower():
            results.append((field, data))
            continue
        # Search description (case-insensitive, partial match)
        if 'description' in data and term in data['description'].lower():
            results.append((field, data))
    return results

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: k search <field or description keyword>")
        sys.exit(1)
    term = " ".join(sys.argv[1:])
    fields = load_fields()
    results = search(term, fields)
    if not results:
        print(f"No matches found for '{term}'.")
    else:
        for field, data in results:
            print(f"\033[1mField: {field}\033[0m")
            print(f"Description: {data['description']}\n")
            print("Sample YAML:\n")
            print(data['sample'])
            print('-' * 60)
