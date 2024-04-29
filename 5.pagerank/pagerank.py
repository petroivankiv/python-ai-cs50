import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    # if len(sys.argv) != 2:
    #     sys.exit("Usage: python pagerank.py corpus")

    corpus = crawl('5.pagerank/corpus0')
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")

    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")

    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")

    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue

        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    page_count = get_page_number(corpus)
    ranks = dict()

    for item in corpus:
        ranks[item] = (1 - damping_factor) / page_count

    for item in corpus:
        if item == page:
            for link in corpus[item]:
                ranks[link] += damping_factor / len(corpus[item])

    return ranks


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page = random.choice([*corpus.keys()])
    ranks = dict()
    samples = dict()
    
    for item in corpus:
        samples[item] = 0

    for i in range(n):
        next_state = transition_model(corpus, page, damping_factor)
        page = random.choices([*next_state.keys()], [*next_state.values()])[0]
        samples[page] += 1
        
    for sample in samples:
        ranks[sample] = samples[sample] / n

    return ranks


def get_page_number(items):
    count = set()

    for item in items:
        count.add(item)
        count.update(items[item])

    return len(count)


def get_linked_pages(corpus, page):
    linked = set()

    for item in corpus:
        if page in corpus[item]:
            linked.add(item)

    return linked


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    page_count = get_page_number(corpus)
    ranks = dict()

    # set initial random rank
    for page in corpus:
        ranks[page] = random.random()

    iter = True

    while iter:
        for page in corpus:
            linked = get_linked_pages(corpus, page)

            sum = 0

            # sum all pages that link to current page
            for link in linked:
                sum += ranks[link] / len(corpus[link])

            new_rank = (1 - damping_factor) / page_count + damping_factor * sum

            # stop iteration if rank is not changing
            if abs(ranks[page] - new_rank) <= 0.001:
                iter = False

            ranks[page] = new_rank

    return ranks


if __name__ == "__main__":
    main()
