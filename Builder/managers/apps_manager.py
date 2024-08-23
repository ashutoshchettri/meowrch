import os
import time
import glob
import shutil
import traceback
import subprocess
from loguru import logger

from .package_manager import PackageManager


class AppsManager:
	@staticmethod
	def configure_code() -> str:
		try:
			result = subprocess.run(['code', '--version'], capture_output=True, text=True)
			code_exists = result.returncode == 0
		except FileNotFoundError:
			code_exists = False 

		if not code_exists:
			PackageManager.install_packages(packages_list=["code"])

		try:
			subprocess.run(['code', '--install-extension', './misc/apps/vscode/meowrch-theme-1.0.0.vsix'], check=True)
		except Exception:
			logger.error(f"Error installing Visual Studio Code extension: {traceback.format_exc()}")
	
	def configure_firefox(self) -> None:
		logger.info("Start installing Firefox")

		try:
			subprocess.Popen(['timeout', '2', 'firefox', '--headless'])
			time.sleep(3)
			path_profile = glob.glob(os.path.expanduser('~/.mozilla/firefox/*.default-release'))[0]
			shutil.copytree('./misc/apps/firefox/firefox-profile', path_profile, dirs_exist_ok=True)
		except Exception:
			logger.error(f"Error installing firefox: {traceback.format_exc()}")

		logger.success("Firefox has been successfully installed!")
		
	def configure_sddm(self) -> None:
		logger.info("Starting the SDDM installation process")
		theme_name = "meowrch"
		sddm_config_file = "/etc/sddm.conf"
		temp_sddm_config_path = "/tmp/sddm.conf"
		path_to_theme = f"/usr/share/sddm/themes{theme_name}"

		if os.path.exists(sddm_config_file):
			new_lines = []

			with open(sddm_config_file, 'r') as file:
				lines = file.readlines()

			for line in lines:
				if line.startswith("Current="):
					line = f"Current={theme_name}"

				new_lines.append(line)
			
			with open(temp_sddm_config_path, 'w') as file:
				file.writelines(new_lines)

			try:
				subprocess.run(["sudo", "mv", temp_sddm_config_path, sddm_config_file], check=True)
				subprocess.run(["sudo", "mv", "./misc/sddm_theme", path_to_theme], check=True)
				logger.success("The SDDM theme has been successfully installed!")
			except Exception:
				logger.error(f"The installation of the SDDM theme failed: {traceback.format_exc()}")	
		else:
			logger.warning("SDDM configuration skipped... (file not found)")

	def configure_grub(self) -> None:
		logger.info("Starting the GRUB installation process")
		grub_config_file = "/etc/default/grub"
		temp_grub_config_path = "/tmp/grub"
		path_to_theme = "/boot/default/grub/themes/meowrch"
		grub_theme_setting = f"GRUB_THEME={path_to_theme}/theme.txt\n"

		if os.path.exists(grub_config_file):
			logger.error("GRUB is not installed. Skipping theme installation.")
			return 

		with open(grub_config_file, 'r') as file:
			grub_config = [line for line in file.readlines() if not line.startswith("GRUB_THEME")]

		grub_config.append(grub_theme_setting)

		with open(temp_grub_config_path, 'w') as file:
			file.writelines(grub_config)

		try:
			subprocess.run(["sudo", "mv", "./misc/grub_theme", path_to_theme], check=True)
			subprocess.run(["sudo", "mv", temp_grub_config_path, grub_config_file], check=True)
			subprocess.run(["sudo", "update-grub"], check=True)
			logger.success("The GRUB theme has been successfully installed!")
		except Exception:
			logger.error(f"The installation of the grub theme failed: {traceback.format_exc()}")
