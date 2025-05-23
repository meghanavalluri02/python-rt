import os
 
DIR = '.'  # Directory to track ('.' for current directory)
SNAPSHOT = 'snapshot.txt'  # File to store last known state
 
def snapshot(dir_path):
    return set(os.path.join(dp, f) for dp, _, filenames in os.walk(dir_path) for f in filenames)
 
current = snapshot(DIR)
 
if os.path.exists(SNAPSHOT):
    with open(SNAPSHOT, 'r') as f:
        previous = set(line.strip() for line in f)
 
    added = current - previous
    removed = previous - current
 
    print("✅ Added files:\n", *added, sep="\n")
    print("\n❌ Removed files:\n", *removed, sep="\n")
else:
    print("📸 First run — snapshot created.")
 
# Save the current file list to snapshot.txt
with open(SNAPSHOT, 'w') as f:
    for path in sorted(current):
        f.write(path + '\n')
