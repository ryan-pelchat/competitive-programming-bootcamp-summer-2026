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
|2.2 d. Array Manipulation, Harder|Medium|[flagquiz](https://open.kattis.com/problems/flagquiz)|[Solution](practice_contests/day_1/flagquiz.py)|array of array of strings; be careful; duplicates may exists||
|2.2 j. Stack|Easy|[Pairing Socks](https://open.kattis.com/problems/pairingsocks)|[Solution](practice_contests/day_1/pairingsocks.py)|||
|2.2 h. Bit Manipulation|Easy|[snapperhard](https://open.kattis.com/problems/snapperhard)|[Solution](practice_contests/day_1/snapperhard.py)|||
|2.3 f. Hash Table (map), Harder|Medium|[snowflakes](https://open.kattis.com/problems/snowflakes)|[Solution](practice_contests/day_1/snowflakes.py)|||
|2.4 b. Union-Find Disjoint Sets|Easy|[Union-Find](https://open.kattis.com/problems/unionfind)|[Solution](practice_contests/day_1/unionfind.py)|||
|2.4 c. Tree-related Data Structures|Medium|[fenwick](https://open.kattis.com/problems/fenwick)|[Solution](practice_contests/day_1/fenwick.py)|||

### Day 2

|Section|Diffifulty|Problem|Solution|Hints|Slides|
|---|---|---|---|---|---|
|3.2 e. Iterative (Permutation)|Easy|[Veci](https://open.kattis.com/problems/veci)|[Solution](practice_contests/day_2/veci.py)|||
|3.2 i. Mathematical Simulation (Complete Search), Harder|Easy|[Thanos The Hero](https://open.kattis.com/problems/thanosthehero)|[Solution](practice_contests/day_2/thanosthehero.py)|||
|3.2 l. Recursive Backtracking (Harder)|Medium|[dobra](https://open.kattis.com/problems/dobra)|[Solution](practice_contests/day_2/dobra.py)|||
|3.3 a. Binary Search|Easy|[firefly](https://open.kattis.com/problems/firefly)|[Solution](practice_contests/day_2/firefly.py)|||
|3.3 c. Ternary Search and Others|Easy|[ceiling](https://open.kattis.com/problems/ceiling)|[Solution](practice_contests/day_2/ceiling.py)|||

### Day 3

|Section|Diffifulty|Problem|Solution|Hints|Slides|
|---|---|---|---|---|---|
|3.4 a. Classical|Medium|[classrooms](https://open.kattis.com/problems/classrooms)||||
|3.4 e. Non Classical, Easier|Easy|[ants](https://open.kattis.com/problems/ants)||||
|3.5 c. Knapsack (Subset-Sum)| Medium| [knapsack](https://open.kattis.com/problems/knapsack)||||
|3.5 e. Traveling-Salesman-Problem (TSP)|Medium|[beepers](https://open.kattis.com/problems/beepers)||||
|3.5 f. DP level 1|Easy|[spiderman](https://open.kattis.com/problems/spiderman)||||
|3.5 g. DP level 2|Medium|[walrusweights](https://open.kattis.com/problems/walrusweights)||||

### Day 4

|Section|Diffifulty|Problem|Solution|Hints|Slides|
|---|---|---|---|---|---|
|4.2 c. Flood Fill, Harder|Easy|[10kindsofpeople](https://open.kattis.com/problems/10kindsofpeople)||(intelligent flood fill; just run once to avoid TLE as there are many queries)||
|4.3 a. Minimum Spanning Tree (MST) Standard|Easy|[Lost Map](https://open.kattis.com/problems/lostmap)|[Solution](practice_contests/day_4/lostmap.py)|(actually just a standard MST problem)||
|4.4 a. On Unweighted Graph: BFS, Easier|Easy|[grid](https://open.kattis.com/problems/grid)||(modified BFS with step size multiplier)||
|4.4 d. On Weighted Graph: Dijkstra's, Easier|Medium|[texassummers](https://open.kattis.com/problems/texassummers)||(Dijkstra’s; complete weighted graph; print path)||
|4.4 d. On Weighted Graph: Dijkstra’s, Easier|Easy|[shortestpath1](https://open.kattis.com/problems/shortestpath1)|| (very standard Dijkstra’s problem)||


### Day 5

|Section|Diffifulty|Problem|Solution|Hints|Slides|
|---|---|---|---|---|---|
|5.3 a. Prime Numbers|Medium|[primesieve](https://open.kattis.com/problems/primesieve)||||
|5.3 f. GCD and/or LCM|Easy|[smallestmultiple](https://open.kattis.com/problems/smallestmultiple)||||
|5.3 i. Modular Arithmetic|Easy|[anothercandies](https://open.kattis.com/problems/anothercandies)||||
|7.2 a. Points|Medium|[imperfectgps](https://open.kattis.com/problems/imperfectgps)||||
|7.2 b. Lines|Medium|[hurricanedanger](https://open.kattis.com/problems/hurricanedanger)||||
|7.3 a. Polygon Easier|Easy|[convexpolygonearea](https://open.kattis.com/problems/convexpolygonarea)||||


## TODO List:

- [x] Contest Outlines
- [ ] Change Day 3 Problems, remove non-dikjtra
- [ ] Contest Solutions
- [ ] Contest Setup in Kattis
- [ ] Contest Slide Explanations
- [ ] Daily Slides
- [ ] Daily Summaries
