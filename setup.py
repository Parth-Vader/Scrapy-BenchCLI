from setuptools import setup

setup(
	name='Bench',
	version='1.0',
	py_modules=['scrapy-bench'],
	install_requires=[
	'Click',
	'scrapy',
	'statistics',
    'six',
    'datetime',
	],
	entry_points='''
		[console_scripts]
		scrapy-bench=bench:cli
		''',
)		