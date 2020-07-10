![](https://github.com/uribench/spell-check/workflows/Test/badge.svg)

# Spell Check

This repository demonstrates how to integrate spell checking of various types of files in GitHub CI pipeline.

It uses PySpelling on top of GNU Aspell to spell check the following types of files:

- Markdown
- Python
- JavaScript
- XML
- Text

This repository includes also a workaround to a performance issue with PySpelling when spell checking XML files.

The next sections cover the following subjects in more details:

- [Typical Usage Workflow](#typical-usage-workflow)
- [Why PySpelling](#why-pyspelling)
- [PySpelling Installation](#pyspelling-installation)
- [PySpelling Configuration and Use](#pyspelling-configuration-and-use)
- [XML Spell Checking - Performance Issue Workaround](#xml-spell-checking-performance-issue-workaround)
- [CI Pipeline Configuration](#ci-pipeline-configuration)
- [Use a Docker Container or Not?](#use-a-docker-container-or-not)

## Typical Usage Workflow

The following steps are a **quick summary** of the typical usage workflow and each step is described in more details in the sections that follows:

1. One Time: Install PySpelling and its dependencies locally on your computer. See [PySpelling Installation](#pyspelling-installation) for details.
2. After any change in the source files requiring spell checking: 

- a. Run the following commands (assuming also XML files are included, otherwise execute only the second command):
```bash
$ ./src/extract_text_from_xml.py
$ pyspelling
```
- b. If there are misspelled words found, append the relevant misspelled words (i.e., non-English words) to the custom dictionary selectively, and fix those words that are truly misspelled (i.e., English words). This can be done by reviewing the found misspelled words before or after appending them to the custom dictionary. The following command appends the misspelled words to the custom dictionary, in a non-selective manner:
```bash
$ pyspelling >> custom-dictionary.txt
```
- c. Now run again PySpelling to make sure all source files are passing cleanly the spell checking.
- d. Commit the changes locally and push them to the remote origin. This will trigger the CI pipeline workflow on GitHub that includes spell checking.
- e. Check that the tests of this push have passed successfully (i.e., visit GitHub and view the `Actions` page of the respective branch). See [CI Pipeline Configuration](#ci-pipeline-configuration) for details.

## Why PySpelling

There are several tools available for spell checking of various types of files. [PySpelling][1] by facelessuser was selected. It is a Python wrapper around [Gnu Aspell][5] that simplifies automation. See the [`Spell Checkers Comparison`][6] document for details on the selection criteria.

## PySpelling Installation

Use the following commands to install PySpelling and its dependencies on Linux:

```bash
$ sudo apt-get install aspell aspell-en
$ pip install pyspelling --user
```
For more details on PySpelling installation see the [Installation chapter][7] on the official documentations, which includes also a section on [how to use PySpelling under Windows][8].

## PySpelling Configuration and Use

[PySpelling][1] Useful Links:

1. [Documentations][2]
2. [Spell Checker Options][3]
3. [Included filters][4]

### PySpelling Configuration

Configuration of PySpelling is specified in a [`.pyspelling.yml`][9] file placed in the root of the repository.

Notes:

- The PySpelling configuration file defines several spelling tasks along with their individual filters and options. 
- All of the tasks are contained under the keyword `matrix` and are organized in a YAML list. 
- Each task requires, at the very least, a `name` and `sources` to search.
- The double asterisk in the list of `sources` indicates a [`glob pattern`][10], which is usually used to indicate any number of sub-directories.
- Each of the above tasks defines, in the list of `wordlists`, the custom dictionaries to be used. Here we use a common custom dictionary and we place it in the root of the repository. But separate custom dictionaries that are placed elsewhere is possible (e.g., each custom dictionary can be placed next to each type of files).
- The `markdown` filter of PySpelling can be used in its simple form. However, in order to gain more control on what parts of the Markdown file to ignore in the spell checking, it can be combined with the `html` filter in a PySpelling `pipeline`, as in the included PySpelling configuration file. This is based on the fact that the `markdown` filter of PySpelling converts the Markdown source file into HTML. 
- The `xml` task has been commented because of the performance issue mention in the section below on [XML Spell Checking - Performance Issue Workaround](#xml-spell-checking-performance-issue-workaround) for additional details. Instead, the `text` task is used. 

### Local Use of PySpelling

The PySpelling can be executed with all the tasks specified in its `.pyspelling.yml` configuration file using the following command:

```bash
$ pyspelling
```

It can also executed with a specific named task as follows:

```bash
$ pyspelling -n task_name

# Example:
$ pyspelling -n markdown
```

To run a more verbose output, use the `-v` flag. 

```bash
pyspelling -v
```

You can increase verbosity level by including more `v` chars (e.g., `-vv`, `-vvvv`). Currently, you can go up to four levels.

In case PySpelling is used also with XML files, it is recommended to use the included pre-processing script prior to executing PySpelling. The following commands can be used locally for that:

```bash
$ ./src/extract_text_from_xml.py
$ pyspelling
```

See the section below on [XML Spell Checking - Performance Issue Workaround](#xml-spell-checking-performance-issue-workaround) for additional details.

### Managing the Custom Dictionaries

**Do not forget** to populate the custom dictionaries appropriately. 

To populate the custom dictionary with all the exceptions found by all the tasks in the PySpelling configuration file use (i.e., as mentioned earlier, here we use one common custom dictionary):

```bash
$ pyspelling >> custom-dictionary.txt
```

This will append the new misspelled words to the `custom-dictionary.txt` file for use in the next execution of PySpelling. However, note that this is a "blind" append, and the added words, as well as the removal of duplicated words (i.e., not necessary), have to be done manually by reviewing and amending the `custom-dictionary.txt` file.

As mentioned in the previous section, PySpelling can be executed with a specific task and this can be used also to populate the custom dictionary with misspelled words form a specific task selectively as follows:

```bash
$ pyspelling -n task_name >> custom-dictionary.txt
```

As discussed in the [next section](#xml-spell-checking-performance-issue-workaround), spell checking of XML files can be accelerated using the included pre-processing script prior to executing PySpelling. The following commands can be used locally to populate the custom dictionary:

```bash
$ ./src/extract_text_from_xml.py
$ pyspelling >> custom-dictionary.txt
```

## XML Spell Checking - Performance Issue Workaround

Due to an issue with PySpelling or the underlying GNU Aspell, spell checking of large XML files takes very long time. For instance, spell checking included XML example files (about 10K lines in total) takes about 30-50 min.

To handle this limitation a work around has been implemented in the form of Python script for pre-processing the XML files to extract plain text from relevant XML nodes, and then using PySpelling to spell check only the plain text.

Note that **this approach takes less than 1 sec compared to about 30-50 min** with the XML filter of PySpelling. 

For more details on this work around see the [`XML Spell Checking Workaround`][11] document.

In order to locally execute the pre-processing script followed by PySpelling, use the following commands:

```bash
$ ./src/extract_text_from_xml.py
$ pyspelling
```

This will put all the text extracted from the XML files in the `extracted_text_from_xml.txt` temporary file under the `xml-files` folder.

## CI Pipeline Configuration

For a quick introduction to GitHub workflow and actions see the following documents:

1. [About GitHub Actions][12]
2. [Core concepts for GitHub Actions][13]
3. [Configuring a workflow][14]

The spell check is integrated in the GitHub CI pipeline automation, which includes setting of the GitHub-Hosted Runner virtual machine and all the required dependencies. After that, the PySpelling is executed.

The [`.github/workflows/test.yml`][15] file includes the workflow configuration for all the tests of this GitHub repository. In this demonstration repository, it refers only to the spell checking test. 

On its simplest mode, on any push to your repository, GitHub will look for the existing workflow files and start the specified jobs on Runners according to the contents of the file, for that commit.

Note: `.github/workflows/test.yml` is a YAML file so you have to pay extra attention to indentation. Always use spaces, **not tabs**.

## Use a Docker Container or Not?

The [`Docker or Not`][16] document discusses the preferred way of executing the GitHub Workflow steps that are included in the spell-check job. More specifically, it compares the main two alternative of directly executing them on GitHub-Hosted Runner VM or in a Docker Container.

## Linting and Testing the Code

Pylint is used to lint all relevant Python scripts. Pylint is integrated in the GitHub CI pipeline. 

To run Pylint locally use the following command from the root of the repository:

```bash
$ pylint ./src/*py ./tests/*.py
```

The Python pre-processing script that extract text from XML files is tested using test scripts, helper, and fixture files under `./tests` folder. The tests were written for [Pytest][17]. Pytest is an open source framework for testing Python code. It is a no-boilerplate alternative to Python’s standard `unittest` module.

The tests are integrated in the GitHub CI pipeline.

To run the tests locally use the following command from the root of the repository:

```bash
$ pytest
```

---

[1]: https://github.com/facelessuser/pyspelling
[2]: http://facelessuser.github.io/pyspelling/
[3]: https://facelessuser.github.io/pyspelling/configuration/#spell-checker-options
[4]: https://facelessuser.github.io/pyspelling/pipeline/#filter
[5]: http://aspell.net/
[6]: ./docs/Spell%20Checkers%20Comparison.md
[7]: https://facelessuser.github.io/pyspelling/#installing
[8]: https://facelessuser.github.io/pyspelling/#usage-in-windows
[9]: ./.pyspelling.yml
[10]: https://facelessuser.github.io/wcmatch/glob/
[11]: ./docs/XML%20Spell%20Checking%20Workaround.md
[12]: https://help.github.com/en/actions/getting-started-with-github-actions/about-github-actions
[13]: https://help.github.com/en/actions/getting-started-with-github-actions/core-concepts-for-github-actions
[14]: https://help.github.com/en/actions/configuring-and-managing-workflows/configuring-a-workflow
[15]: ./.github/workflows/test.yml
[16]: ./docs/Docker%20or%20Not.md
[17]: https://pytest.org/
