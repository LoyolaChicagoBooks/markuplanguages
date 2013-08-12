#!/bin/bash

echo "<<< $(date) >>>"
echo
hg incoming && hg pull && hg update --clean && \
	jekyll build && \
	rsync -av --delete --exclude .htaccess \
	./_site/ \
	course@courseclouds.com:./sites/markup.cs.courseclouds.com/
echo
