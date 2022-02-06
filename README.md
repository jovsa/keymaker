# keymaker

> where 🔑s get made

## Goal

* There are some really great code ecosystems that are being built.
* There are a few {engineers, patterns, systems} that are critical to these ecosystems.
* There is too much volume to keep a track of.
* Hence, it'll be good to have a tool that can help monitor this.

## Ideal functionality

* Get statistics on repos Something like: `make <repo-name(s)>`
  * Get `repo:contributor` statistics
  * Get `contributor:system` statistics
  * Identify all the sub-topics in a repo/ecosystem.
  * Link a user to subtopic.
* I'm assuming some of the repos are private, hence, we might want to dump statistics in an `/output` folder and not commit stuff that's private.
* Should be easily extended to add new reports/metrics/outputs

## Setup
1. If this is your first time cloning the repo, run `make environment` which will set up the python virtual environment and install all python packages in requirements.txt
2. Run `source .venv/bin/activate` in order to set up the python virtual environment


## Some useful links

* [Sourcegraph](https://about.sourcegraph.com/): A code search tool. Mainly centered around finding code not so much so the commiters.
* [pydriller](https://pydriller.readthedocs.io/en/latest/intro.html): A good python library that we can build on/extend.

Logo options (we should pick one):

![keymaker-image-1](https://user-images.githubusercontent.com/1289023/152268269-f1c7cb3c-a2dc-4c78-9458-64d68d17d7f3.png)

![keymaker-image-2](https://user-images.githubusercontent.com/1289023/152269293-8824cc23-daf0-4857-ae0c-157b3a6dc532.png)
