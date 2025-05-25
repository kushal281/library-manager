import argparse
import subprocess
import json

"""
Custom Python Library Manager using pip
This script provides a command-line interface to manage Python packages using pip.
It allows users to install, uninstall, list, update packages, and check for outdated packages.
"""

class CustomLibraryfunctions:
    """Custom functions to manage Python packages using pip."""

    def install_package(self, package_name):
        """Install a package using pip."""
        try:
            result = subprocess.run(
                ["pip", "install", package_name],
                capture_output=True, text=True, check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error installing package '{package_name}':\n{e.stderr}")

    def uninstall_package(self, package_name):
        """Uninstall a package using pip."""
        try:
            result = subprocess.run(
                ["pip", "uninstall", "-y", package_name],
                capture_output=True, text=True, check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error uninstalling package '{package_name}':\n{e.stderr}")

    def list_packages(self):
        """List all installed packages."""
        try:
            result = subprocess.run(
                ["pip", "list"],
                capture_output=True, text=True, check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error listing packages:\n{e.stderr}")

    def update_package(self, package_name):
        """Update a package to the latest version."""
        try:
            result = subprocess.run(
                ["pip", "install", "--upgrade", package_name],
                capture_output=True, text=True, check=True
            )
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"Error updating package '{package_name}':\n{e.stderr}")

    def update_all_packages(self):
        """Update all outdated packages."""
        try:
            result = subprocess.run(
                ["pip", "list", "--outdated", "--format=json"],
                capture_output=True, text=True, check=True
            )
            packages = json.loads(result.stdout)
            for pkg in packages:
                print(f"Updating {pkg['name']}...")
                subprocess.run(["pip", "install", "--upgrade", pkg["name"]])
        except subprocess.CalledProcessError as e:
            print(f"Error updating packages:\n{e.stderr}")

    def outdated_packages(self):
        """List outdated packages."""
        try:
            result = subprocess.run(
                ["pip", "list", "--outdated"],
                capture_output=True, text=True, check=True
            )
            if not result.stdout.strip():
                print("All packages are up to date.")
                return
            print("The following packages are outdated:")
            print(result.stdout)
            i=input("Do you want to update all outdated packages? (yes/no): ").strip().lower()
            if i == 'yes':
                self.update_all_packages()
        except subprocess.CalledProcessError as e:
            print(f"Error checking outdated packages:\n{e.stderr}")



def main():
    parser = argparse.ArgumentParser(description="Custom Python Library Manager")
    parser.add_argument(
        "action",
        choices=["install", "uninstall", "list", "update", "outdated", "update_all"],
        help="Action to perform"
    )
    parser.add_argument(
        "package",
        nargs="?",
        help="Package name (required for install, uninstall, update)"
    )

    args = parser.parse_args()
    lib_manager = CustomLibraryfunctions()

    if args.action == "install" and args.package:
        lib_manager.install_package(args.package)
    elif args.action == "uninstall" and args.package:
        lib_manager.uninstall_package(args.package)
    elif args.action == "list":
        lib_manager.list_packages()
    elif args.action == "update" and args.package:
        lib_manager.update_package(args.package)
    elif args.action == "outdated":
        lib_manager.outdated_packages()
    elif args.action == "update_all":
        lib_manager.update_all_packages()
    else:
        print("Invalid usage. Please provide the correct arguments.")

if __name__ == "__main__":
    main()