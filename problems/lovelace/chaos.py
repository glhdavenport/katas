from typing import List
# x_n+1 = r(x_n)(1-x_n)
# 0 < r < 4
# x_0 = 0.5
# define logistic_map(r) which returns a list of x_n for 50 values of n

def logistic_map(r: int, generations: int = 51, x_0: float = 0.5) -> List:
    results = []
    results.append(x_0)
    for _ in range(generations-1):
        x_n = results[-1]
        x_next = r * x_n * (1 - x_n)
        results.append(x_next)
    return results

if __name__ == "__main__":
    import sys
    from matplotlib import pyplot as plt
    generations = 51
    r = 3.88
    x_0 = 0.5
    if len(sys.argv) > 1:
        r = float(sys.argv[1]) if sys.argv[1] else r
        generations = int(sys.argv[2]) if sys.argv[2] else generations
        x_0 = float(sys.argv[3]) if sys.argv[3] else x_0
    
    plt.plot([x for x in range(generations)], logistic_map(r, generations, x_0))
    plt.show()