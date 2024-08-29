%%pyspark
%pip install cairosvg

import requests, tarfile, os, cairosvg
from notebookutils import mssparkutils

# Source: https://www.npmjs.com/package/@fabric-msft/svg-icons

# Parameters
convert_to_png = True  # PNG conversion (True | False)
png_output_height = 512  # PNG height in pixels. Aspect ratio is maintained. Higher numbers materially impact execution time.
lakehouse_base = "/lakehouse/default/Files/Icons/Fabric"  # Location to extract contents

# Fetch latest npm version
response = requests.get(f"https://registry.npmjs.org/@fabric-msft/svg-icons").json()
latest_version = response["dist-tags"]["latest"]

# Define paths
lakehouse_destination = os.path.join(lakehouse_base, f"v{latest_version}")
tgz_url = response["versions"][latest_version]["dist"]["tarball"]
tgz_local_path = os.path.join(lakehouse_destination, os.path.basename(tgz_url))
svg_dir = os.path.join(lakehouse_destination, "package/dist/svg/")
png_dir = os.path.join(lakehouse_destination, "package/dist/png/")

# DELETE & recreate lakehouse_destination
if mssparkutils.fs.exists(f"file:{lakehouse_destination}"):
    mssparkutils.fs.rm(f"file:{lakehouse_destination}", True)
mssparkutils.fs.mkdirs(f"file:{lakehouse_destination}")

# Download & save .tgz
with open(f"{tgz_local_path}", "wb") as file:
    file.write(requests.get(tgz_url).content)

# Extract .tgz
with tarfile.open(f"{tgz_local_path}", "r:gz") as tar:
    tar.extractall(f"{lakehouse_destination}")

# Convert SVGs to PNGs
if convert_to_png:
    mssparkutils.fs.mkdirs(f"file:{png_dir}")
    svg_files = [f.name for f in mssparkutils.fs.ls(f"file:{svg_dir}") if f.name.endswith('.svg')]
    for svg_filename in svg_files:
        cairosvg.svg2png(url=os.path.join(f"{svg_dir}", svg_filename),
                         write_to=os.path.join(f"{png_dir}", f"{os.path.splitext(svg_filename)[0]}.png"),
                         output_height=png_output_height)
    print(f"{len(svg_files)} icons converted to PNG with {png_output_height}px")

print(f"Files extracted to {lakehouse_destination}")
