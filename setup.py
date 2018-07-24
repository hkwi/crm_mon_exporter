from setuptools import setup

setup(name="crm_mon_exporter",
	version="0.1.0",
	description="Pacemaker crm_mon prometheus exporter",
	author="Hiroaki Kawai",
	author_email="hiroaki.kawai@gmail.com",
	url="https://github.com/hkwi/crm_mon_exporter",
	py_modules = ["crm_mon_exporter"],
	entry_points={
		"console_scripts": [
			"crm_mon_exporter=crm_mon_exporter:cli"
		]
	},
	install_requires=["flask"]
)
