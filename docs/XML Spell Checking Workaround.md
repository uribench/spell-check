# XML Spell Checking Workaround

Due to an issue with PySpelling v2.6 or the underlying GNU Aspell, spell-checking of large XML files takes very long time. For instance, spell-checking included XML example files (about 10K lines in total) takes about 30-50 min.

To handle this limitation the following work around has been implemented:

1. A Python script using [SAX (Simple API for XML) parser][1] is included. SAX parses the XML files and generates a temporary file with the content of all the relevant XML nodes. Both the Python script and the generated temporary file are stored under `./spell-check/` folder.
2. Unlike other XML parsers that hold the entire XML in memory, SAX digests the XML files element by element, line by line. SAX emits several events as it goes step by step through the file. We subscribe and handle the following SAX events: `startElement`, `characters`, and `endElement`.
3. SAX was originally a Java-only API. [Here][2] you can find a list of supported languages other than Java. See [this][3] to learn more about SAX for Python.
4. The GitHub workflow has been changed to run the pre-processing Python script before the PySpelling is launched.
5. PySpelling configuration has been changed to spell-check the pre-processing output file as a plain text.

Note that **this approach takes less than 1 sec compared to about 30-50 min** with the XML filter of PySpelling. 


---

[1]: http://www.saxproject.org/
[2]: http://www.saxproject.org/langs.html
[3]: https://wiki.python.org/moin/Sax
