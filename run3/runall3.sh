#!/bin/bash
cd "$(dirname "$0")"
for s in $(seq 1 10); do for c in owned_needs owned_none unowned_needs unowned_none placebo; do
  [ -s runs/${c}_s$s.jsonl ] && continue
  st=$(date +%s); python3 revolt3.py --cell $c --seed $s --model qwen2.5:14b --out runs/${c}_s$s.jsonl; echo "$c $s $(( $(date +%s)-st ))s" >> runs/wallclock.txt
done; done
echo DONE >> runs/wallclock.txt
