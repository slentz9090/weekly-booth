"""Build the chunk plan for the javascript_tool publish route (window may be minimized).
Usage: python3 gen2/mkchunks.py <outdir> <dir1> [<dir2> ...]
For each repo directory, every listed file (tracked-modified or untracked, passed via DIRFILES)
becomes gzip+base64, split into 12000-char chunks with sha256 per chunk and per file.
"""
import base64, gzip, hashlib, json, os, sys

CHUNK = 12000
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def sha(b):
    return hashlib.sha256(b).hexdigest()


def main():
    outdir = sys.argv[1]
    os.makedirs(outdir, exist_ok=True)
    spec = json.loads(sys.argv[2])  # {"docs/dlffl": ["week-8.html"], ...}
    plan = {}
    for d, names in spec.items():
        files = []
        for n in names:
            raw = open(os.path.join(ROOT, d, n), "rb").read()
            gz = base64.b64encode(gzip.compress(raw, 9)).decode()
            chunks = [gz[i:i + CHUNK] for i in range(0, len(gz), CHUNK)]
            files.append({"name": n, "sha": sha(raw), "len": len(raw), "gzlen": len(gz),
                          "chunks": [{"i": i, "sha": sha(c.encode()), "text": c} for i, c in enumerate(chunks)]})
        plan[d] = files
        with open(os.path.join(outdir, d.replace("/", "__") + ".json"), "w") as f:
            json.dump({"dir": d, "files": files}, f)
        print(d, [(x["name"], x["len"], len(x["chunks"])) for x in files])
    with open(os.path.join(outdir, "summary.json"), "w") as f:
        json.dump({d: [{"name": x["name"], "sha": x["sha"], "len": x["len"], "n": len(x["chunks"]), "chunkSha": [c["sha"] for c in x["chunks"]]} for x in fs] for d, fs in plan.items()}, f, indent=1)


if __name__ == "__main__":
    main()
