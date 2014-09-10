---
layout: page
title: JSON and XPath
---

# JSON

* JSON spec: <http://json.org/>
* json2.js: <https://github.com/douglascrockford/JSON-js/blob/master/json2.js>

Evaluating JSON strings:
<pre>
var tree = eval('({"type": "addition", "children": [{"type": "integer", "val": 5}, {"type": "multipliction", "children": [{"type": "integer", "val": 3}, {"type": "integer", "val": 2}]}]})');
</pre>

Just a javascript object:
<pre>
{
    "type": "addition", 
    "children": [
        {
            "type": "integer", 
            "val": 5
        }, 
        {
            "type": "multipliction", 
            "children": [
                {
                    "type": "integer", 
                    "val": 3
                }, 
                {
                    "type": "integer", 
                    "val": 2
                }
            ]
        }
    ]
}
</pre>


Finding items in the tree:
<pre>
tree.children[1].children[0].type
</pre>

It's just javascript, but we'll see that finding items in trees is a common problem. Now let's look at some techniques for doing this in XML.

# XPath
* Book Slides <http://www.brics.dk/ixwt/xpath.pdf>
* Suggested Reading: Chapter 3
