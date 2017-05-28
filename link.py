from scrapy.linkextractors import LinkExtractor
from scrapy.http import HtmlResponse, TextResponse, Response
from six.moves.urllib.parse import urlparse
import glob
from timeit import default_timer as timer
import click


def main():
    start = timer()

    url = 'http://scrapinghub.com/'
    link_extractor = LinkExtractor()
    total = 0
    #r1 = TextResponse(url)
    #r2 =Response(url)
    for files in glob.glob('sites/index*'):

        f = (open(files, "r"))
        html = "'''" + f.read() + "'''"
        # print html

        r3 = HtmlResponse(url=url, body=html, encoding='utf8')
        links = link_extractor.extract_links(r3)
        total = total + len(links)
    end = timer()
    print("\nTotal number of links extracted = {0}".format(total))
    print ("Time taken = {0}".format(end - start))
    click.secho("Rate of link extraction : {0} links/second\n".format(
        float(total / (end - start))), bold=True)

    g = open("Stats.txt", 'a')
    g.write(" {0}".format((float(total / (end - start)))))


if __name__ == "__main__":
    main()
