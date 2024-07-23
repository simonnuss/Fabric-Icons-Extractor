%%pyspark

import requests, tarfile, os, shutil

latest_npm_version      = requests.get("https://registry.npmjs.org/@fabric-msft/svg-icons").json()["dist-tags"]["latest"]
lakehouse_destination   = f"/lakehouse/default/Files/Icons/Fabric/v{latest_npm_version}"
tgz_url                 = f"https://registry.npmjs.org/@fabric-msft/svg-icons/-/svg-icons-{latest_npm_version}.tgz"
tgz_local_path          = os.path.join(lakehouse_destination, "svg-icons.tgz")

# DELETE & recreate lakehouse_destination
shutil.rmtree(lakehouse_destination, ignore_errors=True)
os.makedirs(lakehouse_destination)

# Download & save .tgz
with open(tgz_local_path, "wb") as file:
    file.write(requests.get(tgz_url).content)

# Extract .tgz
with tarfile.open(tgz_local_path, "r:gz") as tar:
    tar.extractall(lakehouse_destination)

print(f"Package contents saved to {lakehouse_destination}")