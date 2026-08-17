# Competitive Programming Bootcamp Summer 2026

Managed by Sonya Allin and Ryan Pelchat

## Daily Structure

|Time|Duration|Activities|
|---|---|---|
|10:00|1h30min|"Difficulty (Price) is Right" game. Discussion of previous day's solution. (First day is an introduction, orientation, icebreaker and teambuilding)|
|11:30|1h30min|Instruction/Discussion of concepts|
|13:00|30min|Lunch|
|13:30|3h|Practice contest with targeted problems|
|16:30|0|End of day|

## Notes

- Each practice contest will contain 5-6 problems with a distribution close to the following:
  - 1 super easy
  - 2 easy
  - 1 medium
  - 1 hard
- Homework:
  - Students finish contest with their team members or on their own
  - Students read the textbook and summary for the material relevant to the next day

## Resources

- [CSC148 UofT](https://www.teach.cs.toronto.edu/~csc148h/notes/index.html)

## Outline

|Day|Slides|Speaker Notes|Summary|Kattis|Topics|
|---|---|---|---|---|---|
|0|[Slides](slides/day0_slides.pptx)|[Notes](slides/day0_notes.md)|[Summary](slides/day0_summary.pdf)||- What is ICPC <br> - ICPC Rules <br> - Skills needed to perform <br> - Teambuilding/Ice breaker|
|1|[Slides](slides/day1_slides.pptx)|[Notes](slides/day1_notes.md)|[Summary](slides/day1_summary.pdf)||- 1.3.3 Introduction to Algorithm Analysis <br> - 2.2 Linear DS with Built-in Libraries <br> &emsp; - 2.2.1 Array <br> &emsp; - 2.2.3 Bitmask <br> &emsp; - 2.2.5 Linked Data Structures <br> - 2.3 Non-Linear DS with Built-in Libraries <br> &emsp; - 2.3.1 Binary Heap (Priority Queue) <br> &emsp; - 2.3.2 Hash Table <br> &emsp; - 2.3.3 Balanced Binary Search Tree (bBST) <br> - 2.4 DS with Our Own Libraries <br> &emsp; - 2.4.1 Graph <br> &emsp; - 2.4.2 Union-Find Disjoint Sets <br> &emsp; - 2.4.3 Fenwick (Binary Indexed) Tree| 
|2|[Slides](slides/day2_slides.pptx)|[Notes](slides/day2_notes.md)|[Summary](slides/day2_summary.pdf)||- 3.2 Complete Search <br> &emsp; - 3.2.1 Iterative Complete Search <br> &emsp; - 3.2.2 Recursive Complete Search <br> &emsp; - 3.2.3 Complete Search Tips <br> - 3.3 Divide and Conquer <br> &emsp; - 3.3.2 Ternary Search|
|3|[Slides](slides/day3_slides.pptx)|[Notes](slides/day3_notes.md)|[Summary](slides/day3_summary.pdf)||- 3.4 Greedy <br> &emsp; - 3.4.1 Examples <br> - 3.5 Dynamic Programming <br> &emsp; - 3.5.1 DP Illustration <br> &emsp; - 3.5.2 Classical Examples <br> &emsp; - 3.5.3 Non-Classical Examples|
|4|[Slides](slides/day4_slides.pptx)|[Notes](slides/day4_notes.md)|[Summary](slides/day4_summary.pdf)||- 4.2 Graph Traversal <br> &emsp; - 4.2.2 Depth First Search (DFS) <br> &emsp; - 4.2.3 Breadth First Search (BFS) <br> &emsp; - 4.2.5 Flood Fill (Implicit 2D Grid Graph) <br> - 4.3 Minimum Spanning Tree <br> &emsp; - 4.3.1 Overview and Motivation <br> &emsp; - 4.3.2 Kruskal's Algorithm <br> - 4.4 Single-Source Shortest Paths (SSSP) <br> &emsp; - 4.4.1 Overview and Motivation <br> &emsp; - 4.4.3 On Weighted Graph: Dijkstra's|
|5|[Slides](slides/day5_slides.pptx)|[Notes](slides/day5_notes.md)|[Summary](slides/day5_summary.pdf)||- 5.3 Number Theory <br> &emsp; - 5.3.1 Prime Numbers <br> &emsp; - 5.3.3 Finding Prime Factors with Optimized Trial Divisions <br> &emsp; - 5.3.6 Greatest Common Divisor & Least Common Multiple <br> &emsp; - 5.3.9 Modular Arithmetic <br> - 7.2 Basic Geometry Objects with Libraries <br> &emsp; - 7.2.1 0D Objects: Points <br> &emsp; - 7.2.2 1D Objects: Lines <br> &emsp; - 7.2.3 2D Objects: Circles <br> &emsp; - 7.2.4 2D Objects: Triangles <br> &emsp; - 7.2.5 2D Objects: Quadrilaterals <br> - 7.3 Algorithms on Polygon with Libraries <br> &emsp; - 7.3.1 Polygon Representation <br> &emsp; - 7.3.3 Area of a Polygon <br> &emsp; - 7.3.4 Checking if a Polygon is Convex <br> &emsp; - 7.3.5 Checking if a Point is Inside a Polygon <br> &emsp; - 7.3.6 Cutting Polygon with a Straight Line|


## Contest Problems

### Day 1

|Section|Diffifulty|Problem|Solution|Hints|Slides|
|---|---|---|---|---|---|
|2.2 d. Array Manipulation, Harder|Medium|[flagquiz](https://open.kattis.com/problems/flagquiz)|[Solution](practice_contests/day_1/flagquiz.py)|array of array of strings; be careful; duplicates may exists|[Slides](practice_contests/day_1/slides/flagquiz_solution_slides.pdf)|
|2.2 j. Stack|Easy|[Pairing Socks](https://open.kattis.com/problems/pairingsocks)|[Solution](practice_contests/day_1/pairingsocks.py)|(simulation using two stacks; just do as asked)|[Slides](practice_contests/day_1/slides/pairingsocks_solution_slides.pdf)|
|2.2 h. Bit Manipulation|Easy|[snapperhard](https://open.kattis.com/problems/snapperhard)|[Solution](practice_contests/day_1/snapperhard.py)|(bit manipulation; find the pattern; the easier version is also available at Kattis - snappereasy *)|[Slides](practice_contests/day_1/slides/snapperhard_solution_slides.pdf)|
|2.3 f. Hash Table (map), Harder|Medium|[snowflakes](https://open.kattis.com/problems/snowflakes)|[Solution](practice_contests/day_1/snowflakes.py)|no hints available|[Slides](practice_contests/day_1/slides/snowflakes_solution_slides.pdf)|
|2.4 b. Union-Find Disjoint Sets|Easy|[Union-Find](https://open.kattis.com/problems/unionfind)|[Solution](practice_contests/day_1/unionfind.py)|(basic UFDS; similar to UVa 00793)|[Slides](practice_contests/day_1/slides/unionfind_solution_slides.pdf)|
|2.4 c. Tree-related Data Structures|Medium|[fenwick](https://open.kattis.com/problems/fenwick)|[Solution](practice_contests/day_1/fenwick.py)|(basic Fenwick Tree; use long long)|[Slides](practice_contests/day_1/slides/fenwick_solution_slides.pdf)|

### Day 2

|Section|Diffifulty|Problem|Solution|Hints|Slides|
|---|---|---|---|---|---|
|3.2 e. Iterative (Permutation)|Easy|[Veci](https://open.kattis.com/problems/veci)|[Solution](practice_contests/day_2/veci.py)|(try all permutations; get the one that is larger than X)|[Slides](practice_contests/day_2/slides/veci_solution_slides.pdf)|
|3.2 i. Mathematical Simulation (Complete Search), Harder|Easy|[Thanos The Hero](https://open.kattis.com/problems/thanosthehero)|[Solution](practice_contests/day_2/thanosthehero.py)|(for-loop from backwards)|[Slides](practice_contests/day_2/slides/thanosthehero_solution_slides.pdf)|
|3.2 l. Recursive Backtracking (Harder)|Medium|[dobra](https://open.kattis.com/problems/dobra)|[Solution](practice_contests/day_2/dobra.py)|(try all possible 3n changes of ‘ ’ (to a vowel, an ‘L’, or other consonant not ‘L’); prune invalid states; count valid states)|[Slides](practice_contests/day_2/slides/dobra_solution_slides.pdf)|
|3.3 a. Binary Search|Easy|[firefly](https://open.kattis.com/problems/firefly)|[Solution](practice_contests/day_2/firefly.py)|(sort stalactites vs stalagmites separately; brute force height; binary search the obstacles hit)|[Slides](practice_contests/day_2/slides/firefly_solution_slides.pdf)|
|3.3 c. Ternary Search and Others|Easy|[ceiling](https://open.kattis.com/problems/ceiling)|[Solution](practice_contests/day_2/ceiling.py)|(LA 7578 - WorldFinals Phuket16; BST insertion+tree equality check; also available at UVa 01738 - Ceiling Function)|[Slides](practice_contests/day_2/slides/ceiling_solution_slides.pdf)|

### Day 3

|Section|Diffifulty|Problem|Solution|Hints|Slides|
|---|---|---|---|---|---|
|3.4 a. Classical|Medium|[classrooms](https://open.kattis.com/problems/classrooms)|[Solution](practice_contests/day_3/classrooms.py)|(variant of interval covering; multiple rooms)|[Slides](practice_contests/day_3/slides/classrooms_solution_slides.pdf)|
|3.4 e. Non Classical, Easier|Easy|[ants](https://open.kattis.com/problems/ants)|[Solution](practice_contests/day_3/ants.py)|(also available at UVa 10714 - Ants)|[Slides](practice_contests/day_3/slides/ants_solution_slides.pdf)|
|3.5 c. Knapsack (Subset-Sum)| Medium| [knapsack](https://open.kattis.com/problems/knapsack)|[Solution](practice_contests/day_3/knapsack.py)|(basic DP Knapsack; print the solution)|[Slides](practice_contests/day_3/slides/knapsack_solution_slides.pdf)|
|3.5 e. Traveling-Salesman-Problem (TSP)|Medium|[beepers](https://open.kattis.com/problems/beepers)|[Solution](practice_contests/day_3/beepers.py)|(DP or recursive backtracking with sufficient pruning; also available at UVa 10496 - Collecting Beepers)|[Slides](practice_contests/day_3/slides/beepers_solution_slides.pdf)|
|3.5 f. DP level 1|Easy|[spiderman](https://open.kattis.com/problems/spiderman)|[Solution](practice_contests/day_3/spiderman.py)|(simple DP; go up or down; print solution)|[Slides](practice_contests/day_3/slides/spiderman_solution_slides.pdf)|
|3.5 g. DP level 2|Medium|[walrusweights](https://open.kattis.com/problems/walrusweights)|[Solution](practice_contests/day_3/walrusweights.py)|(backtracking with memoization)|[Slides](practice_contests/day_3/slides/walrusweights_solution_slides.pdf)|

### Day 4

|Section|Diffifulty|Problem|Solution|Hints|Slides|
|---|---|---|---|---|---|
|4.2 c. Flood Fill, Harder|Easy|[10kindsofpeople](https://open.kattis.com/problems/10kindsofpeople)|[Solution](practice_contests/day_4/10kindsofpeople.py)|(intelligent flood fill; just run once to avoid TLE as there are many queries)|[Slides](practice_contests/day_4/slides/10kindsofpeople_solution_slides.pdf)|
|4.3 a. Minimum Spanning Tree (MST) Standard|Easy|[Lost Map](https://open.kattis.com/problems/lostmap)|[Solution](practice_contests/day_4/lostmap.py)|(actually just a standard MST problem)|[Slides](practice_contests/day_4/slides/lostmap_solution_slides.pdf)|
|4.4 a. On Unweighted Graph: BFS, Easier|Easy|[grid](https://open.kattis.com/problems/grid)|[Solution](practice_contests/day_4/grid.py)|(modified BFS with step size multiplier)|[Slides](practice_contests/day_4/slides/grid_solution_slides.pdf)|
|4.4 d. On Weighted Graph: Dijkstra's, Easier|Medium|[texassummers](https://open.kattis.com/problems/texassummers)|[Solution](practice_contests/day_4/texassummers.py)|(Dijkstra’s; complete weighted graph; print path)|[Slides](practice_contests/day_4/slides/texassummers_solution_slides.pdf)|
|4.4 d. On Weighted Graph: Dijkstra’s, Easier|Easy|[shortestpath1](https://open.kattis.com/problems/shortestpath1)|[Solution](practice_contests/day_4/shortestpath1.py)| (very standard Dijkstra’s problem)|[Slides](practice_contests/day_4/slides/shortestpath1_solution_slides.pdf)|


### Day 5

|Section|Diffifulty|Problem|Solution|Hints|Slides|
|---|---|---|---|---|---|
|5.3 a. Prime Numbers|Easy|[enlarginghashtables](https://open.kattis.com/problems/enlarginghashtables)|[Solution](practice_contests/day_5/enlarginghashtables.py)|(use sieve up to 40 000; prime test numbers greater than 2n; check primality of n itself)|[Slides](practice_contests/day_5/slides/enlarginghashtables_solution_slides.pdf)|
|5.3 a. Prime Numbers|Easy|[reseto](https://open.kattis.com/problems/reseto)|[Solution](practice_contests/day_5/reseto.py)|(sieve of Eratosthenes until the k-th crossing)|[Slides](practice_contests/day_5/slides/reseto_solution_slides.pdf)|
|5.3 f. GCD and/or LCM|Easy|[smallestmultiple](https://open.kattis.com/problems/smallestmultiple)|[Solution](practice_contests/day_5/smallestmultiple.py)|(simple LCMs of all numbers; use Java BigInteger to be safe)|[Slides](practice_contests/day_5/slides/smallestmultiple_solution_slides.pdf)|
|5.3 i. Modular Arithmetic|Easy|[anothercandies](https://open.kattis.com/problems/anothercandies)|[Solution](practice_contests/day_5/anothercandies.py)|(simple modular arithmetic)|[Slides](practice_contests/day_5/slides/anothercandies_solution_slides.pdf)|
|7.2 a. Points|Medium|[imperfectgps](https://open.kattis.com/problems/imperfectgps)|[Solution](practice_contests/day_5/imperfectgps.py)|(Euclidean dist; simulation)|[Slides](practice_contests/day_5/slides/imperfectgps_solution_slides.pdf)|
|7.2 b. Lines|Medium|[hurricanedanger](https://open.kattis.com/problems/hurricanedanger)|[Solution](practice_contests/day_5/hurricanedanger.py)|(distance from point to line (not vector); be careful of precision error; work with integers)|[Slides](practice_contests/day_5/slides/hurricanedanger_solution_slides.pdf)|
|7.3 a. Polygon Easier|Easy|[convexpolygonearea](https://open.kattis.com/problems/convexpolygonarea)|[Solution](practice_contests/day_5/convexpolygonearea.py)|(even more basic problem about area of polygon than Kattis - polygonarea)|[Slides](practice_contests/day_5/slides/convexpolygonarea_solution_slides.pdf)|
