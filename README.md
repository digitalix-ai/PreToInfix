# PreToInfix
A Python program for transforming expressions from prefix to infix notation

When run, the program prompts the user to provide an expression in prefix notation. Then it transforms the expression to infix notation, while printing on a new line each step of the process. The prefix expression is being read in reversed order and appended to a list. The algorithm used in the program deals with the numbers (or their abstract representation by letters), the symbols, and adds brackets as necessary. The final result is a string containing the corresponding infix expression.

The program requires a valid prefix notation expression to work properly. Otherwise, unexpected result might be displayed. 
Here is an example of valid prefix expression, with the letters being abstract representations of numbers - variables: *-A/BC-/AKL
which will evaluate to: (A-(B/C))*((A/K)-L)
