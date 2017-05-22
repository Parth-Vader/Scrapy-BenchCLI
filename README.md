# Benchmarking CLI for Scrapy
(The project is still in development.)


>A command-line interface for benchmarking Scrapy, that reflects real-world usage.

## Why?

* Currently, the `scrapy bench` option present just spawns a spider which aggresively crawls randomly generated links at a high speed. 
* The speed thus obtained, which maybe useful for comparisons, does not actually reflects a real-world scenario.
* The actual speed varies with the python version and scrapy version.

## Current Features 
* Spawns a CPU-intensive spider which follows a fixed number of links of a static snapshot of the site [Books to Scrape](http://books.toscrape.com/index.html).
* Follows a real-world scenario where various information of the books is extracted, and stored in a `.csv` file.
* Has a `--long` option for perfoming more than one iteration of spider to improve the precision.
* Has a `--only_results` option for viewing the results only.
