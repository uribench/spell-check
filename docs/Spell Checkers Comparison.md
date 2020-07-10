# Spell Checkers Comparison

## Needs

- A reliable spell checker.
- One that can be executed locally (preferably under Linux).
- One that can be integrated in a CI pipeline (e.g., Travis CI).
- It has to be highly configurable to support multiple languages (e.g., Markdown, Python, JavaScript).
- It has to support complex filters (e.g., skip code blocks in markdown, or check only docstrings in 
  Python code).
- It has to support custom dictionaries.

## PySpelling by Isaac Muse (aka, facelessuser)

> [PySpelling][1] is a module to help with automating spell checking in a project with [Aspell][8] 
> or [Hunspell][10]. It is essentially a wrapper around the command line utility of these two spell  
> checking tools, and allows you to setup different spelling tasks for different file types. You can  
> apply specific and different filters and options to each task. PySpelling can also be used in CI 
> environments to fail the build if there are misspelled words.
>
> Aspell and Hunspell are very good spell checking tools. Aspell particularly comes with a couple of 
> filters, but the filters are limited in types and aren't extremely flexible. PySpelling was 
> created to work around Aspell's and Hunspell's filtering shortcomings by creating a wrapper 
> around them that could be extended to handle more kinds of file formats and provide more advanced 
> filtering. If you need to filter out specific HTML tags with specific IDs or class names, 
> PySpelling can do it. If you want to scan Python files for docstrings, but also avoid specific 
> content within the docstring, you can do that as well. If PySpelling doesn't have a filter you 
> need, with access to so many available Python modules, you can easily write your own.

A [comparison between Aspell and Hunspell][11] shows that Aspell is superior, but it is not been 
maintained since 2011, and it has a more restricting license (LGPL) compared to Hunspell licenses 
(GPL/LGPL/MPL). That is why Hunspell is so common (e.g., LibreOffice, Firefox, Thunderbird and 
Chrome).

> Aspell was, and still is, a superior spell checker (at least for English dictionaries and my 
> personal use cases). However, it’s also an example at how something that might have better 
> performance, even in the open source world, can still fail to thrive. With Hunspell being, not 
> only the default, but the only spell checker, in so many tools, many people struggle and are 
> unaware that there are better alternatives available. Factors like licensing and maintainership 
> have left this really amazing library in an evolutionary dead end.

It is Python based. Documentations are found [here][2].

Depending on your setup, you may need to set the `dictionary` to use as well. Each spell checker 
specifies their dictionary/language differently which is covered in more details in 
[Spell Checker Options][3].

You can also add your own custom `wordlists` to extend the `dictionary`.

The list of included filters is provided [here][4]. It includes, Markdown, Python, JavaScript, HTML, 
and more.

Looks promising!!!

See also [GNU Aspell](#gnu-aspell) below.

## markdown-spell-check by Drc0w

> This [markdown-spell-check project][5] is designed in order to spell-check Markdown files. This 
> project has been written in Python3 and is based on the Python library Pyenchant.

Note: [Enchant][6] by AbiWord is written in C and C++, and its only external dependency is glib. 
AbiWord provides enchant bindings for C and C++; there are third-party bindings for Python, Ruby, 
and Go.

The [Pyenchant][7] are the Python bindings for enchant by Ryan Kelly, which are no longer maintained.

## Pyenchant by Ryan Kelly (rfk)

> This [Pyenchant][7] package provides a set of Python language bindings for the Python enchant 
> spell checking library.

As of February 2018, this project is no longer actively maintained by Ryan Kelly.

## GNU Aspell

> [GNU Aspell][8] is a Free and Open Source spell checker designed to eventually replace Ispell. It 
> can either be used as a library or as an independent spell checker. Its main feature is that it 
> does a superior job of suggesting possible replacements for a misspelled word than just about any 
> other spell checker out there for the English language. Unlike Ispell, Aspell can also easily  
> check documents in UTF-8 without having to use a special dictionary. Aspell will also do its best 
> to respect the current locale setting. Other advantages over Ispell include support for using 
> multiple dictionaries at once and intelligently handling personal dictionaries when more than one 
> Aspell process is open at once.

Latest Stable Version: GNU Aspell 0.60.6.1 (Released July, 2011)
Next Stable Version: 0.60.7-rc1 (Release Candidate 1, Jan 29, 2017)

Looks promising, but can it handle complex filtering of input to skip code blocks in markdown, or 
check only docstrings in Python code, etc.?

There ready wrappers of aspell for various purposes. One such wrapper is 
[PySpelling by facelessuser](#pyspelling-by-facelessuser)

## markdown-spellcheck

The [markdown-spellcheck][9] is a JavaScript project.  It is dedicated for spell checking Markdown 
files.

The markdown-spellcheck is based on the [Hunspell Spellchecker][10] in JavaScript. The Aspell is
not supported by markdown-spellcheck.

A [comparison between Aspell and Hunspell][11] shows that Aspell is superior.

The Hunspell Spellchecker pre-parses Hunspell dictionary to JSON.

It supports custom dictionaries. They are making use of a configuration file called .spelling with 
global dictionary at the start, file overrides afterwards.

It has no filters for spell checking certain parts other types files, such as line comments, block 
comments, or docstrings in code files (e.g., Python, JavaScript).

It has a CLI support with two modes: Interactive and Report.

---

[1]: https://github.com/facelessuser/pyspelling
[2]: http://facelessuser.github.io/pyspelling/
[3]: https://facelessuser.github.io/pyspelling/configuration/#spell-checker-options
[4]: https://facelessuser.github.io/pyspelling/pipeline/#filter
[5]: https://github.com/Drc0w/markdown-spell-check
[6]: https://github.com/AbiWord/enchant
[7]: https://github.com/rfk/pyenchant
[8]: http://aspell.net/
[9]: https://www.npmjs.com/package/markdown-spellcheck
[10]: https://www.npmjs.com/package/hunspell-spellchecker
[11]: https://penguindreams.org/blog/aspell-and-hunspell-a-tale-of-two-spell-checkers/
