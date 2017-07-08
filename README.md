# PagerankElastic
Implementation of the Page Rank algorithm to compute Page Rank on various Topics.

CS6200 Information Retrieval
Homework4: Web graph computation

Objective:
    Compute link graph measures for each page crawled using the adjacency matrix. While you have to use the merged team
    index, this assignment is individual (can compare with teammates the results)

Page Rank - crawl
    Compute the PageRank of every page in your crawl (merged team index). You can use any of the methods described in class: random walks (slow), transition matrix, algebraic solution etc. List the top 500 pages by the PageRank score. You can take a look at this PageRank pseudocode (for basic iteration method) to get an idea

Page Rank - other graph
    Get the graph linked by the in-links in file resources/wt2g_inlinks.txt.zip
    Compute the PageRank of every page. List the top 500 pages by the PageRank score.
