from setuptools import setup

setup(
	name='Bench',
	version='1.0',
	py_modules=['scrapy-bench'],
	install_requires=[
	'Click',
	'scrapy',
	'subprocess',
	'os',
	'sys',
	'time'
	'statistics'
    'threading',
    're',
    'six',
    'datetime'
	],
	entry_points='''
		[console_scripts]
		scrapy-bench=bench:cli
		''',
)		