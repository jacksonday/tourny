## Running the program

To run the the older Functional Programming version, pass the file name or contents to initial_submission.py
```
> python initial_submission.py scores.txt

```

After writing my initial submission, my feedback was to solve the problem using OOP. This is my adaptation.

Simply pass the file name or contents you want to read to the main.py file. For example:
```
> python main.py scores.txt

// OR

> cat scores.txt | python main.py
```


## Code Challenge
Due to a growth in corruption when it comes to scorekeeping, you've been tasked with building a tool for your local soccer league to help keep track of scores for the upcoming tournament. Scores are kept track in a text file where each line represents a tournament match. The scores of the match are stored with the name of the team followed by the score. The tournament uses a point scoring system to determine the overall winner of the tournament:
 
 1. The winner of a match receives 3 tournament points while the loser receives 0.
 2. In the event of a match draw, both teams receive 1 Tournament point.
 3. If any teams are tied at the end of the tournament, whichever team has a higher cumulative score from tournament games will receive a higher ranking.
    * If the cumulative score for both teams is the same, a simple coin flip will determine the higher ranking team.
    
  For example, given the following scores
  ```
  Falcons 3, Tornados 1
  Gophers 4, Falcons 1
  Knights 2, Gophers 1
  Tornados 1, Knights 1
  ```
  
 
 The final ranking would be
 ```
 1. Gophers 4 (5)
 2. Falcons 4 (4)
 3. Knights 4 (3)
 3. Tornados 2 (2)
 ```
 
 * Your program should take a file input of raw match scores via file name or stdin and output via stdout the teams in order of ranking in the format of 
 ```
    <Rank>. <Team Name> <Tournament Points>(<Overall Score)
 ```
 * An example from last year's tournament scores and the final rankings can be found in the examples folder of the project
 * You may use whichever language you are most comfortable with
 * Please include instructions for using your program from installation to execution. It can be assumed a standard environment is already set up (i.e. node + npm/ruby installed).
 * Your code should be production ready and resilient
