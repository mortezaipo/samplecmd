# samplecmd
Prepare sample command usages

### Install

```shell
$ pip install samplecmd
```

> **NOTE:** this project developed for `python3`.

### Example

```bash
$ samplecmd grep -l 2
```

Result:

```
1: Show files containing "foo" and "bar" and "baz"
   grep -l 'baz' $(grep -l 'bar' $(grep -lr 'foo' *) )
2: Search git logs (case-insensitive)
   git log -i --grep='needle'
```

### Arguments

Command input structure: `samplecmd <COMMAND NAME> [EXTRA OPTIONS]`

| Description              | Argument | Value  |
| ------------------------ | -------- | ------ |
| Show command description | -d       |        |
| Show command source link | -s       |        |
| Limit results            | -l       | number |

### Add Extra Sites
To add extra sites, just do these steps:

```shell
$ mkdir ~/.samplecmd/sites/ -p
```

Then create your site file with `.ini` extension and fill required variables.

This is configuration file of `BashOneLiners` site (HTML):

```ini
[GENERAL]
# Enable to be search
enable = yes

[SITE INFO]
# General site info
site_name = BashOneLiners
site_url = http://www.bashoneliners.com/
site_search_url = http://www.bashoneliners.com/oneliners/search/?query={}

[CONTENT INFO]
# Site content type (html or json)
site_content_type = html
# How to get content of request (get or post)
site_content_action = get

[CONTENT PATTERN]
# These variables should be "xpath" or "json key" based on the site returned content
parent = //div[contains(@class, 'oneliner oneliner-')]
title = h3[@class='summary']/a
command = pre[@class='line']/span[@class='oneliner-line']
description = div[@class='explanation']//p
```

This is configuration file of of `CommandLineFu` site (JSON):

```ini
[GENERAL]
# Enable to be search
enable = yes

[SITE INFO]
# General site info
site_name = CommandLineFu
site_url = http://www.commandlinefu.com/
site_search_url = http://www.commandlinefu.com/commands/tagged/163/{}/json

[CONTENT INFO]
# Site content type (html or json)
site_content_type = json
# How to get content of request (get or post)
site_content_action = get

[CONTENT PATTERN]
# These variables should be "xpath" or "json key" based on the site returned content
# parent tag could contain "/" like: parent/sub_parent
parent =
title = summary
command = command
description =
```

> **NOTE:** if your sites returns HTML, then fill `CONTENT PATTERN` section with xpath format, otherwise if it returns JSON, then fill this section with JSON key names.