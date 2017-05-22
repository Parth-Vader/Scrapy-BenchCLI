import click
import subprocess,os
import statistics

@click.command()
@click.option('--long',default = 1,help="Take multiple readings for the benchmark.")
@click.option('--only_result',is_flag=True,help="Display the results only.")
def cli(long,only_result):
	"""A tool for benchmarking your scrapy."""
	if long == 1:
		#subprocess.Popen(["/home/parth/gsoc/cli/venv/bin/scrapy" ,"crawl" ,"followall","&&","cat","AvSpeed.txt"], shell=True)
		if only_result==True:
			process = subprocess.Popen("/home/parth/gsoc/cli/venv/bin/scrapy crawl followall -o items.csv",shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		else:
			process = subprocess.Popen("/home/parth/gsoc/cli/venv/bin/scrapy crawl followall -o items.csv",shell=True)

		process.communicate()
		with open('AvSpeed.txt') as f:
			w = [float(x) for x in next(f).split()]
		

	elif long >1:
		arg = "for i in `seq 1 " + str(long) +" `; do scrapy crawl followall -o items.csv; done"
		if only_result==True:
			process = subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		else:
			process = subprocess.Popen(arg,shell=True)
		output, error = process.communicate()
		with open('AvSpeed.txt') as f:
			w = [float(x) for x in next(f).split()]
        
	click.secho("\nThe results of the benchmark are (all speeds in items/sec) : \n", fg='white',bold=True)
	click.secho("\nTest = 'Normal Benchmarking' Iterations : '{0}'\n".format(long), fg='white',bold=True)
	click.secho("\nMean : {0} Median : {1} Std Dev : {2}\n".format(statistics.mean(w),statistics.median(w),statistics.pstdev(w)), fg='white',bold=True)
	os.remove('AvSpeed.txt')
	os.remove('items.csv')      