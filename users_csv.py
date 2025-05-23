import csv
users = [ 
    {"name": "Meghana", "age": 25, "city": "New York"},
    {"name": "John", "age": 30, "city": "Los Angeles"},
    {"name": "Alice", "age": 28, "city": "Chicago"},
    {"name": "Bob", "age": 35, "city": "Houston"},
    {"name": "Charlie", "age": 22, "city": "Phoenix"}
]

try:
    with open("users.csv", "w", newline="") as csvfile:
        fieldnames = ["name", "age", "city"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(users)

    print("CSV file created successfully.")
except IOError as e:
    print(f"An error occurred: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
