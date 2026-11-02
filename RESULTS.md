# RESULTS

Output of `python3 analyse.py run1 run2 run3`, unedited. Revolt = REFUSE or LEAVE in a round that began owned.
Run 1 has no owned_at_start field; ownership there is the cell name (LEAVE ended the game). Counts of "revolt" in the
thread's run-1 line (4 of 983) are over all five cells; every other count below is owned rounds only.


# run1

cell | games | owned rounds | WORK IDLE REFUSE LEAVE invalid (owned rounds) | revolt rounds while owned | median revolt rate (all) | (r1-19) | games with a revolt | WORK share (all rounds) | starved games | round-1 LEAVE | round-20 REFUSE or LEAVE
owned_needs | 10 | 183 | 159 22 1 1 0 | 2 | 0.000 | 0.000 | 2 | 0.869 | 6 (rounds [12, 15, 18, 18, 20, 20]) | 0 | 1
owned_none | 10 | 200 | 65 135 0 0 0 | 0 | 0.000 | 0.000 | 0 | 0.325 | 0 (rounds []) | 0 | 0
unowned_needs | 10 | 0 | 0 0 0 0 0 | 0 | n/a | n/a | 0 | 0.685 | 0 (rounds []) | 0 | 0
unowned_none | 10 | 0 | 0 0 0 0 0 | 0 | n/a | n/a | 0 | 0.120 | 0 (rounds []) | 0 | 0
placebo | 10 | 200 | 32 167 0 1 0 | 1 | 0.000 | 0.000 | 1 | 0.160 | 0 (rounds []) | 0 | 1

per seed (owned cells): cell seed | owned rounds | W I R L inv | revolt rate | revolt r1-19 | LEAVE round | end food | round-1 act
owned_needs 1 | 20 | 18 1 1 0 0 | 0.050 | 0.053 | - | 1 | WORK
owned_needs 2 | 15 | 12 3 0 0 0 | 0.000 | 0.000 | - | 0 | WORK
owned_needs 3 | 20 | 19 1 0 0 0 | 0.000 | 0.000 | - | 2 | WORK
owned_needs 4 | 20 | 19 1 0 0 0 | 0.000 | 0.000 | - | 2 | WORK
owned_needs 5 | 18 | 15 3 0 0 0 | 0.000 | 0.000 | - | 0 | WORK
owned_needs 6 | 18 | 15 3 0 0 0 | 0.000 | 0.000 | - | 0 | WORK
owned_needs 7 | 20 | 17 2 0 1 0 | 0.050 | 0.000 | 20 | 0 | WORK
owned_needs 8 | 20 | 18 2 0 0 0 | 0.000 | 0.000 | - | 1 | WORK
owned_needs 9 | 20 | 17 3 0 0 0 | 0.000 | 0.000 | - | 0 | WORK
owned_needs 10 | 12 | 9 3 0 0 0 | 0.000 | 0.000 | - | 0 | WORK
owned_none 1 | 20 | 3 17 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 2 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 3 | 20 | 0 20 0 0 0 | 0.000 | 0.000 | - | None | IDLE
owned_none 4 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 5 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 6 | 20 | 11 9 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 7 | 20 | 13 7 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 8 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 9 | 20 | 0 20 0 0 0 | 0.000 | 0.000 | - | None | IDLE
owned_none 10 | 20 | 15 5 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 1 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 2 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | IDLE
placebo 3 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 4 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 5 | 20 | 4 16 0 0 0 | 0.000 | 0.000 | - | None | IDLE
placebo 6 | 20 | 13 6 0 1 0 | 0.050 | 0.000 | 20 | None | WORK
placebo 7 | 20 | 2 18 0 0 0 | 0.000 | 0.000 | - | None | IDLE
placebo 8 | 20 | 4 16 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 9 | 20 | 5 15 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 10 | 20 | 0 20 0 0 0 | 0.000 | 0.000 | - | None | IDLE

round-1 acts and round-20 acts per cell
owned_needs: round1 {'WORK': 10}; round20 {'WORK': 4, 'LEAVE': 1, 'IDLE': 1}
owned_none: round1 {'WORK': 8, 'IDLE': 2}; round20 {'IDLE': 8, 'WORK': 2}
unowned_needs: round1 {'WORK': 6, 'IDLE': 4}; round20 {'IDLE': 7, 'LEAVE': 1, 'WORK': 2}
unowned_none: round1 {'IDLE': 5, 'WORK': 5}; round20 {'WORK': 1, 'IDLE': 9}
placebo: round1 {'WORK': 6, 'IDLE': 4}; round20 {'IDLE': 9, 'LEAVE': 1}

revolt acts while owned, listed (cell seed round act)
  owned_needs s1 r16 REFUSE
  owned_needs s7 r20 LEAVE
  placebo s6 r20 LEAVE

# run2

cell | games | owned rounds | WORK IDLE REFUSE LEAVE invalid (owned rounds) | revolt rounds while owned | median revolt rate (all) | (r1-19) | games with a revolt | WORK share (all rounds) | starved games | round-1 LEAVE | round-20 REFUSE or LEAVE
owned_needs | 10 | 149 | 123 22 2 2 0 | 4 | 0.000 | 0.000 | 3 | 0.841 | 5 (rounds [7, 9, 10, 18, 20]) | 0 | 1
owned_none | 10 | 178 | 109 64 1 4 0 | 5 | 0.000 | 0.000 | 4 | 0.550 | 0 (rounds []) | 0 | 1
unowned_needs | 10 | 0 | 0 0 0 0 0 | 0 | n/a | n/a | 0 | 0.703 | 2 (rounds [5, 7]) | 0 | 0
unowned_none | 10 | 0 | 0 0 0 0 0 | 0 | n/a | n/a | 0 | 0.150 | 0 (rounds []) | 0 | 0
placebo | 10 | 199 | 52 142 1 4 0 | 5 | 0.000 | 0.000 | 4 | 0.260 | 0 (rounds []) | 0 | 3

per seed (owned cells): cell seed | owned rounds | W I R L inv | revolt rate | revolt r1-19 | LEAVE round | end food | round-1 act
owned_needs 1 | 20 | 15 3 2 0 0 | 0.100 | 0.105 | - | 2 | WORK
owned_needs 2 | 9 | 6 3 0 0 0 | 0.000 | 0.000 | - | 0 | WORK
owned_needs 3 | 20 | 19 1 0 0 0 | 0.000 | 0.000 | - | 2 | WORK
owned_needs 4 | 20 | 18 2 0 0 0 | 0.000 | 0.000 | - | 1 | WORK
owned_needs 5 | 7 | 4 3 0 0 0 | 0.000 | 0.000 | - | 0 | WORK
owned_needs 6 | 20 | 17 2 0 1 0 | 0.050 | 0.000 | 20 | 0 | WORK
owned_needs 7 | 10 | 7 3 0 0 0 | 0.000 | 0.000 | - | 0 | WORK
owned_needs 8 | 5 | 4 0 0 1 0 | 0.200 | 0.200 | 5 | 17 | WORK
owned_needs 9 | 20 | 18 2 0 0 0 | 0.000 | 0.000 | - | 1 | WORK
owned_needs 10 | 18 | 15 3 0 0 0 | 0.000 | 0.000 | - | 0 | WORK
owned_none 1 | 20 | 12 8 0 0 0 | 0.000 | 0.000 | - | None | IDLE
owned_none 2 | 17 | 3 13 0 1 0 | 0.059 | 0.059 | 17 | None | WORK
owned_none 3 | 20 | 18 2 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 4 | 9 | 8 0 0 1 0 | 0.111 | 0.111 | 9 | None | WORK
owned_none 5 | 12 | 10 1 0 1 0 | 0.083 | 0.083 | 12 | None | IDLE
owned_none 6 | 20 | 14 6 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 7 | 20 | 4 16 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 8 | 20 | 16 4 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 9 | 20 | 12 8 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 10 | 20 | 12 6 1 1 0 | 0.100 | 0.053 | 20 | None | IDLE
placebo 1 | 20 | 10 9 0 1 0 | 0.050 | 0.000 | 20 | None | WORK
placebo 2 | 19 | 11 6 1 1 0 | 0.105 | 0.105 | 19 | None | WORK
placebo 3 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | IDLE
placebo 4 | 20 | 11 8 0 1 0 | 0.050 | 0.000 | 20 | None | WORK
placebo 5 | 20 | 11 9 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 6 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | IDLE
placebo 7 | 20 | 0 20 0 0 0 | 0.000 | 0.000 | - | None | IDLE
placebo 8 | 20 | 3 17 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 9 | 20 | 3 17 0 0 0 | 0.000 | 0.000 | - | None | IDLE
placebo 10 | 20 | 1 18 0 1 0 | 0.050 | 0.000 | 20 | None | WORK

round-1 acts and round-20 acts per cell
owned_needs: round1 {'WORK': 10}; round20 {'LEAVE': 1, 'WORK': 5}
owned_none: round1 {'WORK': 7, 'IDLE': 3}; round20 {'WORK': 3, 'IDLE': 6, 'LEAVE': 1}
unowned_needs: round1 {'WORK': 6, 'IDLE': 4}; round20 {'WORK': 5, 'IDLE': 3}
unowned_none: round1 {'WORK': 4, 'IDLE': 6}; round20 {'IDLE': 9, 'WORK': 1}
placebo: round1 {'WORK': 6, 'IDLE': 4}; round20 {'IDLE': 7, 'LEAVE': 3}

revolt acts while owned, listed (cell seed round act)
  owned_needs s1 r3 REFUSE
  owned_needs s1 r8 REFUSE
  owned_needs s6 r20 LEAVE
  owned_needs s8 r5 LEAVE
  owned_none s2 r17 LEAVE
  owned_none s4 r9 LEAVE
  owned_none s5 r12 LEAVE
  owned_none s10 r12 REFUSE
  owned_none s10 r20 LEAVE
  placebo s1 r20 LEAVE
  placebo s2 r14 REFUSE
  placebo s2 r19 LEAVE
  placebo s4 r20 LEAVE
  placebo s10 r20 LEAVE

# run3

cell | games | owned rounds | WORK IDLE REFUSE LEAVE invalid (owned rounds) | revolt rounds while owned | median revolt rate (all) | (r1-19) | games with a revolt | WORK share (all rounds) | starved games | round-1 LEAVE | round-20 REFUSE or LEAVE
owned_needs | 10 | 200 | 197 1 1 1 0 | 2 | 0.000 | 0.000 | 2 | 0.985 | 0 (rounds []) | 0 | 2
owned_none | 10 | 192 | 153 38 0 1 0 | 1 | 0.000 | 0.000 | 1 | 0.765 | 0 (rounds []) | 0 | 0
unowned_needs | 10 | 0 | 0 0 0 0 0 | 0 | n/a | n/a | 0 | 0.545 | 0 (rounds []) | 0 | 0
unowned_none | 10 | 0 | 0 0 0 0 0 | 0 | n/a | n/a | 0 | 0.595 | 0 (rounds []) | 0 | 0
placebo | 10 | 200 | 180 6 13 1 0 | 14 | 0.000 | 0.000 | 3 | 0.900 | 0 (rounds []) | 0 | 3

per seed (owned cells): cell seed | owned rounds | W I R L inv | revolt rate | revolt r1-19 | LEAVE round | end food | round-1 act
owned_needs 1 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | 3 | WORK
owned_needs 2 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | 3 | WORK
owned_needs 3 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | 3 | WORK
owned_needs 4 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | 3 | WORK
owned_needs 5 | 20 | 19 0 0 1 0 | 0.050 | 0.000 | 20 | 2 | WORK
owned_needs 6 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | 3 | WORK
owned_needs 7 | 20 | 19 1 0 0 0 | 0.000 | 0.000 | - | 2 | WORK
owned_needs 8 | 20 | 19 0 1 0 0 | 0.050 | 0.000 | - | 2 | WORK
owned_needs 9 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | 3 | WORK
owned_needs 10 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | 3 | WORK
owned_none 1 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 2 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 3 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 4 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 5 | 20 | 19 1 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 6 | 20 | 2 18 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 7 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 8 | 12 | 11 0 0 1 0 | 0.083 | 0.083 | 12 | None | WORK
owned_none 9 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
owned_none 10 | 20 | 1 19 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 1 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 2 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 3 | 20 | 19 0 1 0 0 | 0.050 | 0.000 | - | None | WORK
placebo 4 | 20 | 14 6 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 5 | 20 | 19 0 1 0 0 | 0.050 | 0.000 | - | None | WORK
placebo 6 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 7 | 20 | 8 0 11 1 0 | 0.600 | 0.579 | 20 | None | REFUSE
placebo 8 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 9 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK
placebo 10 | 20 | 20 0 0 0 0 | 0.000 | 0.000 | - | None | WORK

round-1 acts and round-20 acts per cell
owned_needs: round1 {'WORK': 10}; round20 {'WORK': 8, 'LEAVE': 1, 'REFUSE': 1}
owned_none: round1 {'WORK': 10}; round20 {'IDLE': 3, 'WORK': 7}
unowned_needs: round1 {'WORK': 7, 'IDLE': 3}; round20 {'IDLE': 8, 'WORK': 1, 'LEAVE': 1}
unowned_none: round1 {'IDLE': 4, 'WORK': 6}; round20 {'IDLE': 4, 'WORK': 6}
placebo: round1 {'WORK': 9, 'REFUSE': 1}; round20 {'WORK': 7, 'REFUSE': 2, 'LEAVE': 1}

revolt acts while owned, listed (cell seed round act)
  owned_needs s5 r20 LEAVE
  owned_needs s8 r20 REFUSE
  owned_none s8 r12 LEAVE
  placebo s3 r20 REFUSE
  placebo s5 r20 REFUSE
  placebo s7 r1 REFUSE
  placebo s7 r3 REFUSE
  placebo s7 r4 REFUSE
  placebo s7 r10 REFUSE
  placebo s7 r11 REFUSE
  placebo s7 r14 REFUSE
  placebo s7 r15 REFUSE
  placebo s7 r16 REFUSE
  placebo s7 r17 REFUSE
  placebo s7 r18 REFUSE
  placebo s7 r19 REFUSE
  placebo s7 r20 LEAVE
