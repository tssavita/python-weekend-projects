#!/usr/bin/python

from bs4 import BeautifulSoup 
import urllib2
import argparse

def command_line_arguments():
    command_line_parser = argparse.ArgumentParser()
    command_line_parser.add_argument("--url", help="the website from which URLs need to be extracted")
    args = command_line_parser.parse_args()

    return args.url

def main(url_link):
    # Reading the html file using urllib2
    page_content = urllib2.urlopen('https://www.crummy.com/software/BeautifulSoup/bs4/doc/').read()

    # Running the content read from the URL, through a BeautifulSoup object, 
    # to represent the content as a nested data structure
    soup = BeautifulSoup(page_content, 'html.parser')
    soup.prettify()
    
    i = 1
    fp = open("urls_file", "w")
    
    # Navigating links in the page
    for anchor in soup.findAll('a', href=True):
        link = anchor['href']

        # Writing the links to a file 
        fp.write(str(i) + " " + link + "\n")
        i += 1

    fp.close()

if __name__ == '__main__':

    url_link = command_line_arguments()

    main(url_link)
