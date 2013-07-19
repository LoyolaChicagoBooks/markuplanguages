#!/bin/bash

rm -rf _site/
jekyll build && rsync -av --delete _site/ thiruvathukal.com:./sites/markuplanguages/
