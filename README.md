# CollatzSequenceAnalyzerlar
This is an interesting concept. Collatz sequence, sometimes called “the simplest impossible math problem.”

## From Mr. Wiki
The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half the previous term. Otherwise, the next term is 3 times the previous term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

### Objective:
- Confirm that collatz sequence exists with deep analyzis (also trying to figure out whether there is a possible way to break this code)

### Example:
***The Collatz Sequence***
- Write a function named collatz() that has one parameter named number. If number is even, then collatz() should print number // 2 and return this value. If number is odd, then collatz() should print and return 3 * number + 1. Then write a program that lets the user type in an integer and that keeps calling collatz() on that number until the function returns the value 1. (Amazingly enough, this sequence actually works for any integer—sooner or later, using this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why. Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”)
- The output of this program could look something like this:

Enter number:
3  <br />
10 <br />
5  <br />
16 <br />
8  <br />
4  <br />
2  <br />
1  <br />
