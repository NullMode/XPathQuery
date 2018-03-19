#!/usr/bin/env python

import argparse
import os
import sys


try:
    from lxml import etree
except ImportError:
    print("Failed to import lxml - have you installed it? (see README.md)")
    sys.exit(1)


def load_xml(xml_file_path):
    try:
        tree = etree.parse(xml_file_path)
        root = tree.getroot()
    except IOError:
        print("Failed to parse file '{0}', does the file exist?".format(xml_file_path))
        sys.exit(1)
    return root

def query(root, query):
    try:
        results = root.xpath(query)
    except etree.XPathEvalError as e:
        print("Invalid XPath expression!")
        print("Error: " + e.message)
        sys.exit(1)

    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("xml_file")
    parser.add_argument("xpath_query")

    args = parser.parse_args()

    # Load XML
    xml_root = load_xml(args.xml_file)

    # Perform query
    results = query(xml_root, args.xpath_query)

    # Print results
    for i in results:
        print(etree.tostring(i, pretty_print=True))
