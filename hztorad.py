import os

for dirpath, dirnames, filenames in os.walk("."):
    for filename in filenames:
        if filename.endswith(".html"):
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "r") as file:
                filedata = file.read()
                
            filedata = filedata.replace("index.html", "https://hztorad.com")

            with open(filepath, "w") as file:
                file.write(filedata)
