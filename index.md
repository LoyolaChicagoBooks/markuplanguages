---
layout: page
title: Home
---

**This site is being updated for Fall 2013, taught by Matt Bone**.

Testing the deploy script...

Welcome to COMP 336/436: Markup Languages at Loyola University Chicago
Beginning this term, I am moving to plaintext authoring systems for course materials. This site will be maintained until the transition is completed. To get the complete syllabus, see the attached file on this page.

Course Description
This seminar covers Extensible Markup Language (XML) and its applications. At times we will also look at alternatives to XML--a list that includes JSON, YAML, Markdown, etc. It all depends on what you are trying to do!

We cover the core XML component frameworks, including DTD, W3 Schema, Relax-NG, DOM, SAX, XSLT, and XQuery. We'll also look at some domain-specific instances, e.g. MathML, Voice XML, etc. We leave the study of the multitude of domain-specific languages to individual and group projects. 

We will also take a quick look at network/web services, which make use of markup schemes of one form or another. In enterprise computing, SOAP is a web services framework that makes extensive use of XML to provide a modern retake on RPC. RESTful web services also take advantage of XML and other competing forms of markup (JSON) to support representations (data transfer to and from the web service).

Please note that although HTML will be occasionally used in this course, this course is not about HTML and students may want to acquire an HTML book and study it briefly before taking this course. (We'll cover it during the first week, of course but this is by no means intended to be exhaustive coverage of HTML or its many variants.) This course is also not about making cool web pages but you might find ways to do so as a result. Some topics, however, may peripherally address the integration of XML and other web standards. The course has almost nothing to do with web pages and is focused more on modeling and the "emergent" notion of network services.

Because this course is operated as a seminar, it is expected that students come prepared not only to learn but to apply their work in a project setting. This course will place minimal emphasis on structured homework and testing and requires individual and/or team project work. We'll discuss this in the first lecture.

<ul class="posts">
  {% for post in site.posts limit: 5 %}
    <li>
            <span>{{ post.date | date_to_string }}&nbsp;</span> 
            &raquo; 
            <a href="{{ post.url }}">{{ post.title }}</a> <br/>
            <em>{{ post.excerpt }} </em>
            <br/>
    </li>
  {% endfor %}
</ul>

To view older posts, see the [archive](/archive.html).
