## Description
Using a Fabric notebook to execute `download_fabric_icons.py` will download and extract the latest [Fabric SVG icons](https://www.npmjs.com/package/@fabric-msft/svg-icons) to `Files/Icons/Fabric/v{latest_version}` in your Lakehouse.

#### Usage
To use this script in Microsoft Fabric:

1. Copy the code from `download_fabric_icons.py`.
2. Using a notebook with an attached Lakehouse, paste the code into a cell.
3. Optional: define parameters convert_to_png and png_output_height.
4. Run the cell.
5. Optional: Access the icons locally using [OneLake File Explorer](https://learn.microsoft.com/en-us/fabric/onelake/onelake-file-explorer) or [Azure Storage Explorer](https://learn.microsoft.com/en-us/fabric/onelake/onelake-azure-storage-explorer).

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
