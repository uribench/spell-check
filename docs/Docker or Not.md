# Docker Container or Not?

## Introduction

This document discusses the preferred way of executing the GitHub Workflow steps that are included in the spell-check job. More specifically, it compares the main two alternatives of directly executing them on GitHub-Hosted Runner VM or in a Docker Container.

As mentioned by GitHub in [here][1]:

>A GitHub-hosted runner is a virtual machine hosted by GitHub with the GitHub Actions runner application installed. GitHub offers runners with Linux, Windows, and macOS operating systems...You can run workflows directly on the virtual machine or in a Docker container.

Note that since GitHub has moved to their new [GitHub actions][2], most of the existing GitHub Actions are running directly on the **GitHub-hosted runner virtual machine and not in a Docker container**.

## Best Practice

### Alternatives

The following are the main use-cases for running workflows in a Docker container:

1. **Legacy** - Using an existing action that is already using a Docker container and it is not worth the efforts for migration.
2. **Canned Complexity** - Using a workflow step that is complex or requires a complex environment setup, and an invariant and standalone step is required to be run on different environments (e.g., a test step).

For a simple dependency installation, such as the two commands for installing Aspell and PySpelling, there is no such justification to run the PySpelling in a Docker container. Moreover, the PySpelling dependencies installation takes only about 30 sec when done directly on the VM. Moving that to run in a Docker container will have a significant hit on performance.

The possibility of moving the entire spell checking workflow step into a Docker container, either as explicit workflow commands or wrapped in a Docker image is also hard to justify.

Take for instance the approach taken by [`spellcheck-github-actions` by rojopolis][3] that is not only setting the dependencies, but also executing the PySpelling in a Docker image that is set as a GitHub Action and placed on the [GitHub Actions Marketplace][4]. This approach dictates several conventions on the configuration of PySpelling that may be limiting some use-cases. For instance, [`spellcheck-github-actions` by sbates130272][5] forked this action and modified it for his needs, because, as he said [here][6]:

>That repo is python centric and was not working for us so we made this fork.

Note that both versions of `spellcheck-github-actions` are not certified by GitHub. Each is provided by a third-party and is governed by separate terms of service, privacy policy, and support documentation.

In general, project specific configuration has to be passed to the Docker container dynamically. For the complex project specific configuration of PySpelling (e.g., filters, flags, paths, custom dictionaries, ...) there is no justification for passing a complex configuration (e.g., YAML based) that replicates the native configuration just in order to preserve expressibility. 

### Preferred Approach

There is still another alternative that does not involve a Docker container but simplifies the re-use:

- Create a custom `setup-pyspelling` Action, like the [`steup-python`][7] Action, dealing only with the dependency installation directly on the GitHub-hosted runner virtual machine.

Currently, converting two simply dependency installation commands into a GitHub Action is still too complex. The existing JavaScript based GitHub Actions are cumbersome. There is a [pending request][8] submitted to GitHub to support simpler shell script (i.e., Bash flavor) based GitHub Actions.

---

[1]: https://help.github.com/en/actions/reference/virtual-environments-for-github-hosted-runners
[2]: https://github.com/actions
[3]: https://github.com/rojopolis/spellcheck-github-actions
[4]: https://github.com/marketplace?type=actions
[5]: https://github.com/sbates130272/spellcheck-github-actions
[6]: https://github.com/marketplace/actions/check-spelling-js-vue-html-markdown-text
[7]: https://github.com/actions/setup-python
[8]: https://github.community/t/feature-request-shell-script-as-type-of-action/16165/6
