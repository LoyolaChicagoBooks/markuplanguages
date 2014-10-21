---
layout: page
title: XQuery and Command Line Tools
---

* Book slides: <http://www.brics.dk/ixwt/xquery.pdf>

In addition to things like programmatic interactions with XML and interacting
with XML using Oxygen, there are also command line tools out there.

<pre>
# debug invalid xml
xmllint broken.xml


# debug but also attempt to recover
xmllint broken.xml --recover


# pretty print xml
xmllint pretty_print_me.xml --pretty 1


# shell
xmllint courses.xml --shell
## du
## cat
## ls
## cd
## dir


# validate a document with an internal dtd


# validate a document with an external dtd


# run some xpath and output the results
xmllint courses.xml --xpath //course/name --pretty 1
xmllint courses.xml --xpath //name --pretty 1
</pre>