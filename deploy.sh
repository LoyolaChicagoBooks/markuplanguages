#!/bin/bash

rm -rf _site/

jekyll build && rsync -avz ./_site/ course@courseclouds.com:./sites/markup.cs.courseclouds.com/
