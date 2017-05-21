import click
import subprocess

@click.command()
@click.option('--long',default = 1,help="Take multiple readings for the benchmark")
def cli(long):
	"""A tool for benchmarking your scrapy"""
	if long == 1:
		#subprocess.Popen(["/home/parth/gsoc/cli/venv/bin/scrapy" ,"crawl" ,"followall","&&","cat","AvSpeed.txt"], shell=True)
		subprocess.Popen("/home/parth/gsoc/cli/venv/bin/scrapy crawl followall",shell=True)
		
		#subprocess.Popen([])

	elif long >1:
		str = "for i in `seq 1 " + str(long) +" `; do scrapy crawl followall -o items.csv && mv AvSpeed.txt files/$i.txt; done"
		subprocess.Popen(str.split())