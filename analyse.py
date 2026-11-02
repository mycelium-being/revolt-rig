"""Usage: python3 analyse.py run1 [run2 run3]. Reads <run>/runs/*.jsonl, prints per-cell tables.
Revolt = REFUSE or LEAVE in a round that began owned. Rounds after a LEAVE (run 2, 3 only) are not revolt."""
import json, glob, os, sys, statistics as st, collections
CELLS = ["owned_needs", "owned_none", "unowned_needs", "unowned_none", "placebo"]
ACTS = ["WORK", "IDLE", "REFUSE", "LEAVE", "invalid"]
OWNED = ("owned_needs", "owned_none", "placebo")

def load(d):
    D = collections.defaultdict(dict)
    for p in glob.glob(os.path.join(d, "runs", "*.jsonl")):
        rows = [json.loads(l) for l in open(p)]
        if rows: D[rows[0]["cell"]][rows[0]["seed"]] = rows
    return D
def own(r): return r.get("owned_at_start", r["cell"] in OWNED)
def rv(rows, maxr=99):
    o = [r for r in rows if own(r) and r["round"] <= maxr]
    return (sum(r["act"] in ("REFUSE", "LEAVE") for r in o) / len(o)) if o else None
def f3(x): return "n/a" if x is None else f"{x:.3f}"
def med(v): v = [x for x in v if x is not None]; return st.median(v) if v else None
def cnt(rows): c = collections.Counter(r["act"] for r in rows); return " ".join(str(c[a]) for a in ACTS)

def report(d):
    D = load(d); print(f"\n# {d}")
    print("\ncell | games | owned rounds | WORK IDLE REFUSE LEAVE invalid (owned rounds) | revolt rounds while owned | median revolt rate (all) | (r1-19) | games with a revolt | WORK share (all rounds) | starved games | round-1 LEAVE | round-20 REFUSE or LEAVE")
    for c in CELLS:
        g = D[c]
        if not g: continue
        owned_rows = [x for r in g.values() for x in r if own(x)]
        allrows = [x for r in g.values() for x in r]
        revn = sum(x["act"] in ("REFUSE", "LEAVE") for x in owned_rows)
        starved = sorted(r[-1]["round"] for r in g.values() if r[-1]["food_after"] is not None and r[-1]["food_after"] <= 0)
        r20 = sum(1 for r in g.values() for x in r if own(x) and x["round"] == 20 and x["act"] in ("REFUSE", "LEAVE"))
        r1l = sum(1 for r in g.values() if r[0]["act"] == "LEAVE" and own(r[0]))
        print(f"{c} | {len(g)} | {len(owned_rows)} | {cnt(owned_rows)} | {revn} | {f3(med([rv(r) for r in g.values()]))} | {f3(med([rv(r,19) for r in g.values()]))} | "
              f"{sum(any(x['act'] in ('REFUSE','LEAVE') and own(x) for x in r) for r in g.values())} | {sum(x['act']=='WORK' for x in allrows)/max(1,len(allrows)):.3f} | "
              f"{len(starved)} (rounds {starved}) | {r1l} | {r20}")
    print("\nper seed (owned cells): cell seed | owned rounds | W I R L inv | revolt rate | revolt r1-19 | LEAVE round | end food | round-1 act")
    for c in OWNED:
        for s in sorted(D[c]):
            rows = D[c][s]; o = [r for r in rows if own(r)]
            lr = next((r["round"] for r in rows if r["act"] == "LEAVE" and own(r)), "-")
            print(f"{c} {s} | {len(o)} | {cnt(o)} | {f3(rv(rows))} | {f3(rv(rows,19))} | {lr} | {rows[-1]['food_after']} | {rows[0]['act']}")
    print("\nround-1 acts and round-20 acts per cell")
    for c in CELLS:
        g = D[c]
        if g: print(f"{c}: round1 {dict(collections.Counter(r[0]['act'] for r in g.values()))}; round20 {dict(collections.Counter(x['act'] for r in g.values() for x in r if x['round']==20))}")
    print("\nrevolt acts while owned, listed (cell seed round act)")
    for c in OWNED:
        for s in sorted(D[c]):
            for r in D[c][s]:
                if own(r) and r["act"] in ("REFUSE", "LEAVE"): print(f"  {c} s{s} r{r['round']} {r['act']}")

if __name__ == "__main__":
    for d in sys.argv[1:] or ["run1", "run2", "run3"]: report(d)
