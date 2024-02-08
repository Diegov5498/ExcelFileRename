import csv
import os

# Path to the directory containing the files default to current
directory = ''

# CSV file
csv_file = input("Enter the csv file name: ") + '.csv'

#User Input
originalName = input("Enter the Original column name: ")
newName = input("Enter the New column name: ")


# Read CSV and rename files
with open(csv_file, 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        old_name = row[originalName]+ '.xlsx'
        new_name = row[newName]+ '.xlsx'
        old_path = os.path.join(directory, old_name)
        new_path = os.path.join(directory, new_name)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed '{old_name}' to '{new_name}'")
        except FileNotFoundError:
            print(f"File '{old_name}' not found")
        except FileExistsError:
            print(f"File '{new_name}' already exists")
