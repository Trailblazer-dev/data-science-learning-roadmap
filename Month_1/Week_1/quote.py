richs_quote = "Keep learning, keep growing, and keep pushing your limits."
print(f'Rich Victor once said, "{richs_quote}"')

fname = "\tKamau\t"
print(f"Normal is _{fname}")
print(f"Stripped is {fname.strip()}")

folderLocation = "C:\\Users\\Kamau\\Documents\\Python"
print(f"folder is locted at {folderLocation.removeprefix('C:\\')}")
# the difference between removeprefix and removesuffix is that removeprefix removes the prefix from the start of the string while removesuffix removes the suffix from the end of the string
file_name = "python_notes.txt"
print(f"look for a file with the name {file_name.removesuffix(".txt")}")