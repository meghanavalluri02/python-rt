import os
try:
    cd = os.getcwd()
    items= os.listdir(cd)
    for item in items:
        print(item)

except FileNotFoundError:
    print("The directory was not found.")
except PermissionError:
    print("You do not have permission to access this directory.")
