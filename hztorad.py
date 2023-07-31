import os
import re

# Walk through all directories and files recursively
for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        # Only process .html files
        if filename.endswith(".html"):
            filepath = os.path.join(dirpath, filename)
            
            # Open and read the file
            with open(filepath, "r", encoding='utf-8') as file:
                filedata = file.read()

            # Get the hz value from the filename and form the canonical url
            hz_value = filename.replace("hz-to-rads.html", "")
            canonical_url = f"{hz_value}hz-to-rads.html"
            
            # Replace the old canonical url with the new one
            filedata = re.sub(r'<link rel="canonical" href=".*">', f'<link rel="canonical" href="{canonical_url}">', filedata)

            # Write the modified data back to the file
            with open(filepath, "w", encoding='utf-8') as file:
                file.write(filedata)
