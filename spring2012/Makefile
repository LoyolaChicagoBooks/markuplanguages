syllabus.html: syllabus.hdr syllabus.md
	sed -e 's/=/-/g' syllabus.hdr >> /tmp/syllabus1.html
	pandoc syllabus.md -o /tmp/syllabus2.html
	cat /tmp/syllabus[12].html > syllabus.html
	rm -f /tmp/syllabus?.html
