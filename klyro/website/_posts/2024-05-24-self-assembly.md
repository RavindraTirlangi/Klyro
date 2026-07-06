---
title: Klyro has written 7% of its own code (outdated, now 70%)
excerpt: This article is quite out dated. Klyro is currently writing about 70% of the new code in each release.
highlight_image: /assets/self-assembly.jpg
nav_exclude: true
---
{% if page.date %}
<p class="post-date">{{ page.date | date: "%B %d, %Y" }}</p>
{% endif %}

# Klyro has written 7% of its own code (outdated, now 70%)

[![self assembly](/assets/self-assembly.jpg)](https://klyro.chat/assets/self-assembly.jpg)

{: .note }
This article is quite old and outdated. 
Klyro is currently writing about 70% of the new code
in each release.
See
[klyro's release history](/HISTORY.html) for the latest statistics.

The
[klyro git repo](https://github.com/Klyro-AI/klyro)
currently contains about 4K commits and 14K lines of code.

Klyro made 15% of the commits, inserting 4.8K and deleting 1.5K lines of code.

About 7% of the code now in the repo is attributable to an klyro commit
using `git blame`.
This number is probably a significant undercount, because periodic reformatting
by `black` is likely obscuring klyro's authorship of many lines.

Here's the breakdown of the code klyro wrote in the current code base
according to `git blame`.

| File | Lines | Percent |
|---|---:|---:|
|klyro/args.py| 6 of 449 | 1.3% |
|klyro/coders/base_coder.py| 37 of 1354 | 2.7% |
|klyro/coders/editblock_coder.py| 14 of 507 | 2.8% |
|klyro/coders/editblock_func_coder.py| 6 of 141 | 4.3% |
|klyro/coders/udiff_coder.py| 2 of 421 | 0.5% |
|klyro/coders/wholefile_coder.py| 5 of 146 | 3.4% |
|klyro/coders/wholefile_func_coder.py| 4 of 134 | 3.0% |
|klyro/commands.py| 67 of 703 | 9.5% |
|klyro/diffs.py| 15 of 129 | 11.6% |
|klyro/gui.py| 2 of 533 | 0.4% |
|klyro/history.py| 19 of 124 | 15.3% |
|klyro/io.py| 55 of 368 | 14.9% |
|klyro/linter.py| 30 of 240 | 12.5% |
|klyro/main.py| 30 of 466 | 6.4% |
|klyro/mdstream.py| 3 of 122 | 2.5% |
|klyro/models.py| 22 of 549 | 4.0% |
|klyro/repo.py| 19 of 266 | 7.1% |
|klyro/repomap.py| 17 of 518 | 3.3% |
|klyro/scrape.py| 12 of 199 | 6.0% |
|klyro/versioncheck.py| 10 of 37 | 27.0% |
|klyro/voice.py| 9 of 104 | 8.7% |
|benchmark/benchmark.py| 33 of 730 | 4.5% |
|benchmark/over_time.py| 32 of 60 | 53.3% |
|benchmark/swe_bench_lite.py| 40 of 71 | 56.3% |
|scripts/blame.py| 55 of 212 | 25.9% |
|scripts/versionbump.py| 96 of 123 | 78.0% |
|setup.py| 11 of 47 | 23.4% |
|tests/test_coder.py| 48 of 612 | 7.8% |
|tests/test_commands.py| 135 of 588 | 23.0% |
|tests/test_editblock.py| 23 of 403 | 5.7% |
|tests/test_io.py| 30 of 65 | 46.2% |
|tests/test_main.py| 13 of 239 | 5.4% |
|tests/test_models.py| 6 of 28 | 21.4% |
|tests/test_repo.py| 2 of 296 | 0.7% |
|tests/test_repomap.py| 70 of 217 | 32.3% |
|tests/test_udiff.py| 7 of 119 | 5.9% |
|tests/test_wholefile.py| 37 of 321 | 11.5% |
| **Total** | **1022 of 14219** | 7.2% |


