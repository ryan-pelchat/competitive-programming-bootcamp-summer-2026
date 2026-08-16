### 5.3 Number Theory (Introduction)
**Title:** 5.3 Number Theory
**Content:**
*   **The Foundation:** Number theory in competitive programming frequently revolves around primes, divisibility, and modular arithmetic.
*   **Performance is Key:** Naïve mathematical algorithms often trigger Time Limit Exceeded (TLE) errors. We rely on heavily optimized mathematical properties to reduce $O(N)$ operations to $O(\sqrt{N})$ or $O(\log N)$.
*   **Data Types:** Always be mindful of integer overflow. When multiplying two 32-bit integers, the result can exceed the 32-bit limit. Default to 64-bit integers (`long long` in C++, `int` in Python inherently handles this) when doing number theory.

---

### 5.3.1 Prime Numbers
**Title:** 5.3.1 Prime Numbers & The Sieve
**Content:**
*   **Primality Testing ($O(\sqrt{N})$):**
    *   To check if $N$ is prime, you only need to test divisibility up to $\sqrt{N}$. If $N$ is divisible by a number $p > \sqrt{N}$, it must also be divisible by a number $q < \sqrt{N}$.
*   **Generating Primes (Sieve of Eratosthenes):**
    *   The most efficient way to generate all primes up to an upper bound $M$ (usually up to $10^7$).
    *   **Algorithm:** Create a boolean array of size $M$ set to `True`. Starting from $p=2$, if $p$ is true, mark all multiples of $p$ ($2p, 3p, 4p \dots$) as `False`.
    *   **Time Complexity:** $O(M \log \log M)$, which is extremely close to linear time $O(M)$.

---

### 5.3.3 Finding Prime Factors with Optimized Trial Divisions
**Title:** 5.3.3 Optimized Prime Factorization
**Content:**
*   **The Naïve Way:** Testing every number up to $N$ to find its factors is too slow.
*   **The Optimized Way ($O(\sqrt{N} / \ln \sqrt{N})$):**
    *   First, generate a list of prime numbers using the Sieve of Eratosthenes up to $\sqrt{N}$.
    *   Iterate *only* through these prime numbers. If a prime $p$ divides $N$, divide $N$ by $p$ as many times as possible while recording $p$ as a factor.
    *   **The Golden Rule:** After the loop finishes, if the remaining $N$ is greater than 1, then that remaining $N$ is itself a prime factor!

---

### 5.3.5 Modified Sieve
**Title:** 5.3.5 The Modified Sieve
**Content:**
*   **Beyond True/False:** We can modify the standard Sieve of Eratosthenes to store useful information instead of just boolean flags.
*   **Smallest Prime Factor (SPF):** 
    *   Instead of marking multiples as `False`, store the prime number $p$ that crossed it out.
    *   This allows you to find the prime factors of any number $X$ in $O(\log X)$ time by repeatedly dividing $X$ by `SPF[X]`.
*   **Other Modifications:**
    *   **Euler's Totient Function ($\phi(N)$):** Can be computed alongside the sieve to count how many integers $< N$ are relatively prime to $N$.
    *   **Sum/Count of Divisors:** Arrays can be updated during the sieve to dynamically calculate `numDiffPF` (number of different prime factors).

---

### 5.3.6 Greatest Common Divisor & Least Common Multiple
**Title:** 5.3.6 GCD & LCM
**Content:**
*   **Greatest Common Divisor (GCD):**
    *   The largest integer that divides both $A$ and $B$ without leaving a remainder.
    *   **Euclidean Algorithm:** `gcd(a, b) = (b == 0) ? a : gcd(b, a % b)`
    *   **Time Complexity:** $O(\log(\min(A, B)))$
    *   **Libraries:** Use `std::gcd(a, b)` in C++17 or `math.gcd(a, b)` in Python.
*   **Least Common Multiple (LCM):**
    *   The smallest integer that is a multiple of both $A$ and $B$.
    *   **Formula:** $\text{lcm}(A, B) = A \times (B / \text{gcd}(A, B))$
    *   *Tip:* Always divide before multiplying to prevent integer overflow!

---

### 5.3.9 Modular Arithmetic
**Title:** 5.3.9 Modular Arithmetic
**Content:**
*   **The Goal:** Keeping intermediate calculations small by taking the modulo $M$ (often $10^9 + 7$) at every step to prevent massive integer overflows.
*   **Core Properties:**
    *   **Addition:** $(A + B) \pmod M = (A \pmod M + B \pmod M) \pmod M$
    *   **Multiplication:** $(A \times B) \pmod M = (A \pmod M \times B \pmod M) \pmod M$
    *   **Subtraction:** $(A - B) \pmod M = ((A - B) \pmod M + M) \pmod M$ *(Adding M prevents negative results in languages like C++)*.
*   **Division (Modular Inverse):**
    *   You **cannot** simply do $(A / B) \pmod M$.
    *   If $M$ is prime, use Fermat's Little Theorem: Multiply by $B^{M-2} \pmod M$ instead of dividing by $B$.

---

### 7.2 The Golden Rule of CP Geometry
*(Note: Added this context slide as it is essential for all sections in 7.2)*

**Title:** 7.2 Basic Geometry: The Floating-Point Trap
**Content:**
*   **The Problem:** Computers cannot represent floating-point numbers perfectly. `0.1 + 0.2` might equal `0.30000000000000004`. 
*   **The Solution ($\epsilon$):** Never use `==` to compare two floating-point numbers (`double`).
*   Instead, define an epsilon constant: `EPS = 1e-9`.
*   To check if `A == B`, check if `abs(A - B) < EPS`.
*   To check if `A < B`, check if `A + EPS < B`.
*   **Libraries:** Whenever possible, rely on built-in math libraries or `std::complex` (in C++) to handle coordinate storage and distance vectors.

---

### 7.2.1 0D Objects: Points
**Title:** 7.2.1 0D Objects: Points
**Content:**
*   **Representation:** A point is defined by its coordinates $(x, y)$ in 2D space.
*   **Data Structures:** 
    *   Struct/Class: `struct Point { double x, y; };`
    *   C++ STL: `std::complex<double>` is often used as it natively supports vector addition, subtraction, and rotation!
*   **Distance Formula:** 
    *   The Euclidean distance between $P_1$ and $P_2$: $\sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}$
    *   Use the built-in `hypot(dx, dy)` function to avoid overflow during squaring.

---

### 7.2.2 1D Objects: Lines
**Title:** 7.2.2 1D Objects: Lines
**Content:**
*   **Representation:** 
    *   Standard Form: $Ax + By + C = 0$ (Preferred in CP as it handles vertical lines perfectly without `m = infinity`).
    *   Slope-Intercept Form: $y = mx + c$ (Careful with vertical lines where $\Delta x = 0$).
*   **Line Segments vs. Infinite Lines:**
    *   A line segment is bounded by two endpoints $P_1$ and $P_2$.
    *   To check if two infinite lines are parallel, check if their slopes are equal ($A_1B_2 = A_2B_1$).
    *   To find intersection points, solve the system of linear equations using Cramer's rule.

---

### 7.2.3 2D Objects: Circles
**Title:** 7.2.3 2D Objects: Circles
**Content:**
*   **Representation:** A circle is perfectly defined by its center Point $(x, y)$ and a radius $r$.
*   **Core Formulas:**
    *   **Area:** $\pi r^2$
    *   **Circumference:** $2\pi r$
*   **Inside / Outside Check:**
    *   Given a point $P$, calculate the distance $d$ from the center of the circle to $P$.
    *   If $d < r$: Point is strictly inside.
    *   If $d == r$ (using `EPS`): Point is on the boundary.
    *   If $d > r$: Point is strictly outside.

---

### 7.2.4 2D Objects: Triangles
**Title:** 7.2.4 2D Objects: Triangles
**Content:**
*   **Representation:** Defined by 3 points: $A, B, C$.
*   **Triangle Inequality:** For any valid triangle with side lengths $a, b, c$, the sum of any two sides must be strictly greater than the third side: $a+b>c$, $a+c>b$, $b+c>a$.
*   **Area Formulas:**
    *   Base and Height: $\frac{1}{2} \times \text{base} \times \text{height}$
    *   **Heron's Formula** (When only side lengths are known): 
        *   Let $s = \frac{a+b+c}{2}$ (semi-perimeter)
        *   Area = $\sqrt{s(s-a)(s-b)(s-c)}$

---

### 7.2.5 2D Objects: Quadrilaterals
**Title:** 7.2.5 2D Objects: Quadrilaterals
**Content:**
*   **Representation:** Polygons with 4 vertices. Includes specific shapes:
    *   **Square/Rectangle:** All angles are $90^\circ$.
    *   **Parallelogram:** Opposite sides are parallel.
    *   **Trapezoid:** Only one pair of opposite sides is parallel.
*   **CP Strategy:** You rarely need specialized formulas for quadrilaterals. Any quadrilateral can be easily split into two triangles by drawing a diagonal. Calculate the area of the two triangles and sum them!

---

### 7.3.1 Polygon Representation
**Title:** 7.3.1 Polygon Representation
**Content:**
*   **What is a Polygon?** A closed 2D shape bounded by straight line segments.
*   **Data Structure:** Represented as an array or `vector` of Points. 
*   **Standard Conventions:**
    *   **Vertex Ordering:** Points are almost always stored in **Counter-Clockwise (CCW)** order.
    *   **Closing the Loop:** In many algorithms, it is highly useful to duplicate the first vertex at the end of the array (so $P[N] = P[0]$). This prevents having to write special modulo arithmetic for the edge connecting the last point back to the first point.

---

### 7.3.3 Area of a Polygon
**Title:** 7.3.3 Area of a Polygon (Shoelace Formula)
**Content:**
*   **The Problem:** Finding the area of an irregular polygon with $N$ vertices. Splitting it into triangles manually is too difficult to code.
*   **The Shoelace Formula (Surveyor's Formula):**
    *   Works for *any* simple polygon (convex or concave) as long as the edges do not self-intersect.
    *   Assuming the polygon is closed ($P[N] = P[0]$):
    *   Area = $\frac{1}{2} \left| \sum_{i=0}^{N-1} (x_i y_{i+1} - x_{i+1} y_i) \right|$
*   **Time Complexity:** $O(N)$ with a single loop.

---

### 7.3.4 Checking if a Polygon is Convex
**Title:** 7.3.4 Checking if a Polygon is Convex
**Content:**
*   **Convex vs. Concave:** A convex polygon has no internal angles greater than $180^\circ$ (it has no "dents").
*   **The CCW Test (Cross Product):**
    *   A function `ccw(p, q, r)` uses the 2D cross product of vectors $\vec{pq}$ and $\vec{qr}$ to determine if the path turns Left, Right, or goes Straight.
*   **The Algorithm:**
    *   Iterate through every consecutive triplet of vertices: $P[i], P[i+1], P[i+2]$.
    *   Calculate the turn direction for each triplet.
    *   If the polygon is convex, **all turns must be in the exact same direction** (all Left or all Right). If you see a mix of Left and Right turns, it is concave.

---

### 7.3.5 Checking if a Point is Inside a Polygon
**Title:** 7.3.5 Point Inside a Polygon (Ray Casting)
**Content:**
*   **The Problem:** Given a point $P$ and a polygon, determine if $P$ is strictly inside, outside, or on the boundary.
*   **The Ray Casting Algorithm (Winding Number):**
    *   Imagine shooting an infinite horizontal ray starting from $P$ extending to the right (towards $+x$).
    *   Count how many times this ray intersects the edges of the polygon.
    *   **Odd Intersections:** The point is **Inside**.
    *   **Even Intersections:** The point is **Outside**.
*   **Edge Cases:** Be careful to handle rays that perfectly hit a vertex or run exactly collinear with a horizontal edge!

---

### 7.3.6 Cutting Polygon with a Straight Line
**Title:** 7.3.6 Cutting a Polygon (Sutherland-Hodgman)
**Content:**
*   **The Problem:** Given a convex polygon and an infinite straight line, "slice" the polygon and return the smaller resulting polygon (e.g., the part on the left side of the line).
*   **The Algorithm:**
    *   Iterate through all edges of the polygon.
    *   For each edge connecting $P_1$ to $P_2$:
        1.  If $P_1$ and $P_2$ are both on the "valid" side of the cutting line, keep $P_2$.
        2.  If the edge crosses the cutting line, calculate the exact intersection point. Keep the intersection point, and if $P_2$ is on the valid side, keep $P_2$ as well.
*   **Result:** A new, smaller list of vertices defining the sliced convex polygon.


### 5.3 Number Theory (Introduction)
**Title:** 5.3 Number Theory
**Content:**
*   **The Foundation:** Number theory in competitive programming frequently revolves around primes, divisibility, and modular arithmetic.
*   **Performance is Key:** Naïve mathematical algorithms often trigger Time Limit Exceeded (TLE) errors. We rely on heavily optimized mathematical properties.
*   **Code Example: Python's Advantage**
    *   Python automatically handles arbitrarily large integers, meaning you don't need to worry about the strict 64-bit bounds that C++/Java programmers face, but fast I/O is still helpful!
```python
import sys
# Fast I/O for reading massive numbers
input = sys.stdin.read
data = input().split()
if data:
    large_num = int(data[0]) 
    print(large_num * large_num) # No overflow crash!

```

---

### 5.3.1 Prime Numbers

**Title:** 5.3.1 Prime Numbers & The Sieve
**Content:**

* **Generating Primes (Sieve of Eratosthenes):** The most efficient way to generate all primes up to an upper bound $M$.
* **Code Example (Sieve in Python):**

```python
def sieve(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, int(n**0.5) + 1):
        if is_prime[p]:
            # Mark all multiples of p as False
            for i in range(p * p, n + 1, p):
                is_prime[i] = False
                
    # Return a list of all numbers that remained True
    return [p for p in range(2, n + 1) if is_prime[p]]

primes = sieve(1000000)

```

---

### 5.3.3 Finding Prime Factors with Optimized Trial Divisions

**Title:** 5.3.3 Optimized Prime Factorization
**Content:**

* **The Optimized Way:** Iterate *only* through pre-generated prime numbers up to $\sqrt{N}$.
* **Code Example:**

```python
def prime_factors(n, primes):
    factors = []
    for p in primes:
        if p * p > n: 
            break # We only need to check up to sqrt(N)
        while n % p == 0:
            factors.append(p)
            n //= p
            
    # If anything is left over, it is a prime factor itself!
    if n > 1: 
        factors.append(n)
    return factors

```

---

### 5.3.5 Modified Sieve

**Title:** 5.3.5 The Modified Sieve
**Content:**

* **Smallest Prime Factor (SPF):** Store the prime number $p$ that crossed the number out to allow $O(\log X)$ factorization.
* **Code Example:**

```python
def spf_sieve(n):
    spf = list(range(n + 1)) # Initialize with itself
    
    for p in range(2, int(n**0.5) + 1):
        if spf[p] == p: # It is prime
            for i in range(p * p, n + 1, p):
                if spf[i] == i: # Only update if it hasn't been marked
                    spf[i] = p
    return spf

# Factorization using SPF
def fast_factorize(x, spf):
    factors = []
    while x > 1:
        factors.append(spf[x])
        x //= spf[x]
    return factors

```

---

### 5.3.6 Greatest Common Divisor & Least Common Multiple

**Title:** 5.3.6 GCD & LCM
**Content:**

* **Greatest Common Divisor (GCD):** Use Python's highly optimized built-in math library.
* **Least Common Multiple (LCM):** Divide before multiplying to prevent massive intermediate variables.
* **Code Example:**

```python
import math

# GCD is built-in
a, b = 12, 18
print(math.gcd(a, b)) # Outputs 6

# LCM uses the GCD
def lcm(a, b):
    # Python 3.9+ actually has math.lcm(a, b) built-in!
    # But this is the classic formula:
    return a * (b // math.gcd(a, b))

```

---

### 5.3.9 Modular Arithmetic

**Title:** 5.3.9 Modular Arithmetic
**Content:**

* **The Goal:** Keep calculations small by taking the modulo $M$ (often `10**9 + 7`).
* **Code Example (Fast Modular Exponentiation):**

```python
MOD = 10**9 + 7

a = 150000
b = 200000

# Addition and Multiplication
add_ans = (a + b) % MOD
mult_ans = (a * b) % MOD

# Fast Exponentiation (a^b % MOD)
# NEVER do (a**b) % MOD -> it will TLE! Use the 3-argument pow()
exp_ans = pow(a, b, MOD)

# Modular Inverse (Division) for a/b % MOD
# Multiplies a by (b^(MOD-2) % MOD)
div_ans = (a * pow(b, MOD - 2, MOD)) % MOD 

```

---

### 7.2 The Golden Rule of CP Geometry

**Title:** 7.2 Basic Geometry: The Floating-Point Trap
**Content:**

* **The Problem:** Computers cannot represent floating-point numbers perfectly. Never use `==`.
* **Code Example (The Epsilon Check):**

```python
EPS = 1e-9

def is_equal(a, b):
    return abs(a - b) < EPS

def is_less_than(a, b):
    return a + EPS < b

# Example failure of ==
print(0.1 + 0.2 == 0.3)          # False!
print(is_equal(0.1 + 0.2, 0.3))  # True!

```

---

### 7.2.1 0D Objects: Points

**Title:** 7.2.1 0D Objects: Points
**Content:**

* **Representation:** We can use Python's built-in `complex` type to represent 2D points. The `real` part is $X$, and the `imag` part is $Y$.
* **Code Example:**

```python
# Create points (x, y)
p1 = complex(3, 4)
p2 = complex(0, 0)

# Distance formula (abs() on complex numbers computes the hypotenuse)
dist = abs(p1 - p2) 
print(dist) # Outputs 5.0

# Vector translation (Adding points)
p3 = p1 + complex(1, 2) # X becomes 4, Y becomes 6

```

---

### 7.2.2 1D Objects: Lines

**Title:** 7.2.2 1D Objects: Lines
**Content:**

* **Representation:** Standard Form $Ax + By + C = 0$.
* **Code Example:**

```python
# Convert two points into Ax + By + C = 0
def points_to_line(p1, p2):
    # A = y2 - y1
    A = p2.imag - p1.imag
    # B = x1 - x2
    B = p1.real - p2.real
    # C = -(A*x1 + B*y1)
    C = -(A * p1.real + B * p1.imag)
    return A, B, C

line = points_to_line(complex(0,0), complex(5,5))

```

---

### 7.2.3 2D Objects: Circles

**Title:** 7.2.3 2D Objects: Circles
**Content:**

* **Representation:** Defined by a center point and a radius $r$.
* **Code Example (Inside/Outside check):**

```python
EPS = 1e-9

def point_vs_circle(p, center, r):
    # Calculate Euclidean distance
    d = abs(p - center)
    
    if d < r - EPS:
        return "Inside"
    elif d > r + EPS:
        return "Outside"
    else:
        return "Boundary"

```

---

### 7.2.4 2D Objects: Triangles

**Title:** 7.2.4 2D Objects: Triangles
**Content:**

* **Heron's Formula:** Calculate area knowing only the three side lengths.
* **Code Example:**

```python
import math

def heron_area(p1, p2, p3):
    # Get the 3 side lengths
    a = abs(p1 - p2)
    b = abs(p2 - p3)
    c = abs(p3 - p1)
    
    # Semi-perimeter
    s = (a + b + c) / 2.0
    
    # Area
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

```

---

### 7.2.5 2D Objects: Quadrilaterals

**Title:** 7.2.5 2D Objects: Quadrilaterals
**Content:**

* **CP Strategy:** Split the quadrilateral into two triangles!
* **Code Example:**

```python
# Assuming points A, B, C, D are given in order around the perimeter
A = complex(0, 0)
B = complex(5, 0)
C = complex(5, 5)
D = complex(0, 5)

# Split into Triangle ABC and Triangle ACD
total_area = heron_area(A, B, C) + heron_area(A, C, D)

```

---

### 7.3.1 Polygon Representation

**Title:** 7.3.1 Polygon Representation
**Content:**

* **Data Structure:** An array of `complex` points, ordered Counter-Clockwise (CCW), with the last point duplicating the first to "close the loop."
* **Code Example:**

```python
# A square represented as a polygon
polygon = [
    complex(0, 0),
    complex(10, 0),
    complex(10, 10),
    complex(0, 10)
]

# Push the first vertex to the back to close the loop
polygon.append(polygon[0])

# Now the polygon has 5 points (N+1), forming 4 closed edges

```

---

### 7.3.3 Area of a Polygon

**Title:** 7.3.3 Area of a Polygon (Shoelace Formula)
**Content:**

* **The Shoelace Formula:** Calculates area for any non-intersecting polygon.
* **Code Example:**

```python
def polygon_area(poly):
    # Note: poly must be closed (poly[0] == poly[-1])
    area = 0.0
    for i in range(len(poly) - 1):
        # (x_i * y_i+1) - (x_i+1 * y_i)
        area += (poly[i].real * poly[i+1].imag) - (poly[i+1].real * poly[i].imag)
        
    return abs(area) / 2.0

```

---

### 7.3.4 Checking if a Polygon is Convex

**Title:** 7.3.4 Checking if a Polygon is Convex
**Content:**

* **The CCW Test (Cross Product):** Uses vector cross products to check turn directions.
* **Code Example:**

```python
def ccw(p, q, r):
    # Cross product of vector PQ and PR
    cross = (q.real - p.real) * (r.imag - p.imag) - (q.imag - p.imag) * (r.real - p.real)
    if cross > 0: return 1   # Left turn
    if cross < 0: return -1  # Right turn
    return 0                 # Collinear

def is_convex(poly):
    n = len(poly)
    if n <= 3: return False
    
    # Check the first turn direction
    is_left = ccw(poly[0], poly[1], poly[2]) > 0
    
    for i in range(1, n - 1):
        # If any turn direction differs from the first, it is concave
        if (ccw(poly[i], poly[i+1], poly[(i+2) % n]) > 0) != is_left:
            return False
    return True

```

---

### 7.3.5 Checking if a Point is Inside a Polygon

**Title:** 7.3.5 Point Inside a Polygon (Ray Casting)
**Content:**

* **Ray Casting:** Count the number of edge intersections extending a ray to the right.
* **Code Example:**

```python
def inside_polygon(pt, poly):
    inside = False
    n = len(poly)
    for i in range(n - 1):
        p1, p2 = poly[i], poly[i+1]
        
        # Check if the ray intersects the Y-bounds of the edge
        if (p1.imag > pt.imag) != (p2.imag > pt.imag):
            # Check if the intersection point is to the right of our point
            intersect_x = (p2.real - p1.real) * (pt.imag - p1.imag) / (p2.imag - p1.imag) + p1.real
            if pt.real < intersect_x:
                inside = not inside
                
    return inside # True if odd number of intersections

```

---

### 7.3.6 Cutting Polygon with a Straight Line

**Title:** 7.3.6 Cutting a Polygon (Sutherland-Hodgman)
**Content:**

* **The Algorithm:** Slice a convex polygon by keeping points on the "left" side of a cutting line.
* **Code Example:**

```python
def line_intersect(p1, p2, A, B):
    # Returns the intersection point of line segment p1-p2 and line A-B
    # Uses cross products to find the ratio
    a = B - A
    b = p2 - p1
    c = p1 - A
    # Cross products
    cross_ab = a.real * b.imag - a.imag * b.real
    cross_ca = c.real * a.imag - c.imag * a.real
    
    if abs(cross_ab) < 1e-9: return p1 # Collinear fallback
    
    u = cross_ca / cross_ab
    return p1 + b * u

def cut_polygon(poly, A, B):
    # Cuts the polygon with line passing through A and B, keeping the left side
    cut_poly = []
    for i in range(len(poly) - 1):
        left1 = ccw(A, B, poly[i]) >= 0
        left2 = ccw(A, B, poly[i+1]) >= 0
        
        if left1: 
            cut_poly.append(poly[i])
        if left1 != left2: 
            cut_poly.append(line_intersect(poly[i], poly[i+1], A, B))
            
    if cut_poly:
        cut_poly.append(cut_poly[0]) # Close the loop
    return cut_poly
```