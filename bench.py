import click
import subprocess
import os
import sys
import time
import statistics


@click.command()
@click.option(
    '--long',
    default=1,
    help="Take multiple readings for the benchmark.")
@click.option('--only_result', is_flag=True, help="Display the results only.")
def cli(long, only_result):
    """A tool for benchmarking your scrapy."""

    if long == 1:
        if only_result:
            process = subprocess.Popen(
                "scrapy crawl followall -o items.csv",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            process.wait()

        else:
            process = subprocess.Popen(
                "scrapy crawl followall -o items.csv", shell=True)
            process.wait()
        with open('AvSpeed.txt') as f:
            w = [float(x) for x in next(f).split()]

    elif long > 1:
        arg = "for i in `seq 1 " + \
            str(long) + " `; do scrapy crawl followall -o items.csv; done"
        if only_result:
            process = subprocess.Popen(
                arg,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            process.wait()
        else:
            process = subprocess.Popen(arg, shell=True)
            process.wait()

        with open('AvSpeed.txt') as f:
            w = [float(x) for x in next(f).split()]

    click.secho(
        "\nThe results of the benchmark are (all speeds in items/sec) : \n",
        bold=True)
    click.secho(
        "\nTest = 'Normal Benchmarking' Iterations = '{0}'\n".format(long),
        bold=True)
    click.secho(
        "\nMean : {0} Median : {1} Std Dev : {2}\n".format(
            statistics.mean(w),
            statistics.median(w),
            statistics.pstdev(w)),
        bold=True)
    os.remove('AvSpeed.txt')
    os.remove('items.csv')
