from ES import ES
import math
f = lambda x: -x**2 + 1

if __name__ == "__main__":
    es = ES(f, min_range=-5.12, max_range=5.12)
    es.start()
    es.print()