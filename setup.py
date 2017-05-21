from setuptools import setup

setup(
	name='Bench',
	version='1.0',
	py_modules=['bench'],
	install_requires=[
	'Click',
	],
	entry_points='''
		[console_scripts]
		bench=bench:cli
		''',
)		