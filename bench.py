import click
import subprocess
import os
import sys
import time
import statistics
import threading


class RepeatingTimer(threading._Timer):
    def run(self):
        while True:
            self.finished.wait(self.interval)
            if self.finished.is_set():
                return
            else:
                self.function(*self.args, **self.kwargs)


def status():
    for i in range(10000):
        print("In progress : {0} seconds passed".format(i))
        sys.stdout.write("\033[F")
        time.sleep(1)


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
            timer = RepeatingTimer(1.0, status)
            timer.daemon = True  # Allows program to exit if only the thread is alive
            timer.start()
            process = subprocess.Popen(
                "scrapy crawl followall -o items.csv",
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            process.wait()
            timer.cancel()

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
            timer = RepeatingTimer(1.0, status)
            timer.daemon = True  # Allows program to exit if only the thread is alive
            timer.start()
            process = subprocess.Popen(
                arg,
                shell=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE)
            process.wait()
            timer.cancel()
        else:
            process = subprocess.Popen(arg, shell=True)
            process.wait()

        with open('AvSpeed.txt') as f:
            w = [float(x) for x in next(f).split()]

    click.secho(
        "\nThe results of the benchmark are (all speeds in items/sec) : \n",
        fg='white',
        bold=True)
    click.secho(
        "\nTest = 'Normal Benchmarking' Iterations = '{0}'\n".format(long),
        fg='white',
        bold=True)
    click.secho(
        "\nMean : {0} Median : {1} Std Dev : {2}\n".format(
            statistics.mean(w),
            statistics.median(w),
            statistics.pstdev(w)),
        fg='white',
        bold=True)
    os.remove('AvSpeed.txt')
    os.remove('items.csv')
