---
layout: page
title: Homework 1
---

**Due by class time on Tuesday, January 31, 2012**

*Please note that this corrects the earlier version, where it said January 23, 2011. You can go ahead and get started now! Details about how to work with a version control system such as Mercurial or Git will be presented in class on January 24, 2012.*

Overview

This is a warm-up assignment to help motivate the need for more structured markup schemes (e.g. XML). In addition, it will allow you to become familiar with the infrastructure requirements for this course (e.g. a version control system).

Details

Your job is to create the skeletal structure of a fully-navigable book using HTML. By way of example, a book has the following ingredients, which may or may be omitted from some books:

- title/cover
- front matter: table of contents, list of figures
- chapters: preface, at least one chapter, etc.
- index

This is just one possible type of book organization. As we all know, books are created all the time using software such as Word, LaTeX, and TEI, among others. This assignment starts from HTML as the authoring tool. (In a way, this assignment is re-teaching those of you who know how to "create web pages" something you already know.)

We're not going to duplicate all of the functionality found in these projects. This assignment aims to ensure that everyone knows what is needed to work effectively with XML (mostly for transformation), and the various pitfalls that occur when creating a collection of linked pages.

For example, it will not be long before you realize that you are going to need both internal and external "anchors" (the HTML mechanism for creating hyperlinks and bookmarks in general) to support the required navigation structure. You'll need to take special care to ensure that the hyperlinks are relocatable. By relocatable, I mean that if I were to move your pages to another folder on your computer (or possibly one being served to the web), your pages would continue to work properly. 

So this is just one of the major problems you could end up experiencing in your journey to create a book in HTML. Please keep in mind that this book need not be about anything in particular. In fact, you may find the Lorem Ipsum, <http://www.lipsum.com/>, tool to generate fake text for your book's "content". It's pretty cool.

There are a few ground rules:
- You must author the book in HTML. You may not generate it from another format such as Word, LaTeX, or TEI--all of which can do this but don't always generate clean/beautiful HTML.
- You must have at least 5-10 files in your project.
- You must have a table of contents and rudimentary index in your project. This means that your book should also have chapter and section headings--all of which you can generate via Lorem Ipsum.

When you are done, you should put all of your HTML files under version control and push them out to a source code hosting provider. We recommend bitbucket.org for this purpose. You must come prepared to class to give a demo of your project and explain your design and implementation.

I have posted the article about how to use the Mercurial distributed version control system in the Lectures.
