#!/bin/bash

## References:
## * https://stackoverflow.com/questions/9839083/git-number-of-commits-per-author-on-all-branches


# git shortlog -s -n -e --all --no-merges  --since="01 Oct 2022"
git shortlog -s -n --all --no-merges  --since="01 Oct 2022"

git shortlog -s -n --all --no-merges  --before="01 Dec 2022"
git shortlog -s -n --all --no-merges  --since="01 Dec 2022"
git shortlog -s -n --all --no-merges  --since="01 Dec 2022" --before="29 Dec 2022"

git shortlog -s -n --all --no-merges  --since="01 Dec 2022" --before="07 Dec 2022"
git shortlog -s -n --all --no-merges  --since="08 Dec 2022" --before="14 Dec 2022"
git shortlog -s -n --all --no-merges  --since="15 Dec 2022" --before="29 Dec 2022"

git shortlog -s -n --all --no-merges  --since="01 Dec 2022" --before="07 Dec 2022"

git shortlog -s -n --all --no-merges  --since="01 Nov 2022" --before="01 Dec 2022"
git shortlog -s -n --all --no-merges  --since="01 Oct 2022" --before="01 Nov 2022"
git shortlog -s -n --all --no-merges  --since="01 Sep 2022" --before="01 Oct 2022"
