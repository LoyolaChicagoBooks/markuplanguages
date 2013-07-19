#!/usr/bin/env python

# A script to create a blog posting page. Not done yet.

import sys
import argparse

parser = argparse.ArgumentParser(description='Create a new Jekyll blog posting.')


parser.add_argument("--tag", action="append")
parser.add_argument("--category")
parser.add_argument("TITLE", action="append")

if len(sys.argv) < 1:
   parser.print_help()
   sys.exit(1)

args = parser.parse_args()
print args
sys.exit(2)

from time import strftime, localtime

today = strftime( "%Y-%m-%d", localtime())

yaml="""
---
title: %(title)s
layout: post
category %(category)s:
tags : %(tags)s
---
"""

filename = "%s-%s.md" % (today, "-".join(title))
filename = filename.lower()
filename = filename.strip()

f = open("%s-%s.md" % (today, "-".join(title)), "w")
f.write(yaml)
f.close()

