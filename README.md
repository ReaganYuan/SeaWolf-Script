# Seawolf Script: Original Programming language

### Overview

Seawolf Script is an original programming language that was done as an exercise using [Ply](http://www.dabeaz.com/ply/). It was an assignment in Stony Brook University's CSE 307 - Principles of Programming Languages course. Below you will find the project description.

### Description

##### Our Language:

* Data Types: our language has three data types:
    * **Numbers** = Integer/Real = should be implemented using the equivalent Python integer/real type.
    * **List** = can be implemented using a Python list.
    * **String** = should be implemented using the equivalent Python String type.

##### Each type has a literal representation:
* **Integer** (simplified: only decimals). An integer is represented by one or more digits (0-9). For example, 42 is an integer literal.
* **Real**  (simplified: no exponents). A real is represented by zero or more digits (0-9) followed by the decimal point "." and zero or more digits (0-9). For example, 3.14159 is a real literal.
* **String** A string literal starts with a double quote. This may be followed by zero or more non-double-quote characters. The string ends with a double-quote. The value of the string literal should not include the starting and ending quotes. An example string literal is "Hello SeaWolf.".
* **List** A list literal consists of a square bracket, followed by a comma-separated list of zero or more expressions. For example, [ 307, 130, 100+3 ] is a list literal.

#### Operators: the following operators are listed in precedence order, from highest to lowest (all associative operators are left-associative):


|   Operator 	|   Description	|
|---:	        |---	|
|  `literal`        | The literals given above. |
|  `( expression )` | A parenthesized expression.|
|  `a [ b ]`	    | Indexing. B may be any expression.  	|
|  `a * b, a / b`  	| Multiplication and division (integer and real).|
|  `a % b`      	| Modulus (divides left hand operand by right hand operand and returns remainder). |
|  `a ** b` 	    | Exponent Performs exponential (power) calculation on operators = a to the power b.  	|
|  `a // b` 	    | Floor Division - The division of operands where the result is the quotient in which the digits after the decimal point are removed.  	|
|  `a + b, a - b` 	| Addition and subtraction.	|
|  `a in b` 	    | Evaluates to true if it finds a variable in the specified sequence and false otherwise. |
|  `a < b, a <= b, a == b, a <> b, a > b, a >= b` 	|  Comparison. 	|
|  `not a`  	    | Boolean NOT. |
|  `a and b`        | Boolean AND. |
|  `a or b`         | Boolean OR.  |

##### The operators have the following semantics:

* **Indexing**: B must be an integer, a must be either a string or a list. If a is a string, returns the b-th character of the string as a string. If a is a list, returns the b-th element of the list (whatever type it has). The index is zero-based, so the first element is at index 0. If the index is out of bounds, it is a semantic error.
* **Addition**: A and B must be either both numbers, both strings or both lists. If they are integers or reals, then addition (with standard semantics) is performed. If they are both strings, than string concatenation is performed. If they are both lists, then concatenation of the lists is performed.
* **Multiplication, Division and Subtraction**: A and B must be integers or reals. For division only, B must not be 0. These are performed using standard multiplication semantics.
* **Comparison**: A and B must be integers. The two integers are compared, and the result is 1 if the comparison is true, and 0 if the comparison is false.
* **Boolean AND, OR, NOT**: A and, if present, B must be integers. If the integer is 0, then it is considered false. All other integers are true. The boolean operation is performed. If its true, the result of the expression is the integer 1, otherwise it is the integer 0.

Your program will be called with a single argument. This argument will be a file containing expressions, with one expression per line. You should process each expression and print one of three possible outputs:

* If the line contains a syntax error, you should print out: `SYNTAX ERROR`.
* A semantic error occurs when the line does not contain a syntax error, but one of the "must" conditions given above is violated when evaluating it. If the line contains a semantic error, you should print out: `SEMANTIC ERROR`.
Otherwise, you should evaluate the expression, and print the result using Python's `repr` function.

An example input file might look like:
```
1 - 2 + 3
1 2 3
42 + "Red"
1 - (2 + 3)
"Hello" + " " + "SeaWolf."
[1, 2, 3][0] + 40
```

The output from this file should look like:
```
2
SYNTAX ERROR
SEMANTIC ERROR
-4
'Hello SeaWolf'
41
```

This will be the first of several projects that uses this code, so it will do you well to make sure your code is reusable.
You should create an abstract syntax tree, and use that, rather than using parser actions to evaluate expressions directly.
Future projects will require you to add to your parser and your abstract syntax tree.

Your program will be run with a command like:
`python hw3.py input1.txt`

Your program must take input from the file specified on the command line.
You should include your name and ID as the first line (commented out) in your python file.
<font color='red'>Your program must not use any feature of python that can evaluate code.
This includes the exec statement, the eval function, the execfile function, or the compiler module.</font color='red'>
Your program must not produce spurious output.
