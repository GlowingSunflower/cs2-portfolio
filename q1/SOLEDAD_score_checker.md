# Clean Decision Code Makeover: Student Score Checker
**Name:** Jessie Marie B. Soledad
**Section:** Dahlia

# Part 1 - Analyze the Logic: 
## Input: 
_What information does the program need?_
> <ins> The student's score. </ins>

## Boundary: 
_What is the minimum valid score?_
> <ins> 0 </ins>

## Boundary: 
_What is the maximum valid score?_
> <ins> 100 </ins>

## Possible Outputs: 
_What outcomes can the program produce?_

> <ins> 1. Invalid Score. </ins>

> <ins> 2. Needs Improvement </ins>

> <ins> 3. Your score is Satisfactory. </ins>

> <ins> 4. Your score is Very Satisfactory. </ins>

> <ins> 5. Your score is Outstanding! </ins>

## Selection Pattern: 
_Which part uses a boundary condition?_
> <ins> The score validation: student_score < 0 or student_score > 100 </ins>

## Selection Pattern: 
_Which part uses multiple decision paths?_
> <ins> The if-elif-else statements that classify the score as Outstanding, Very Satisfactory, Satisfactory, or Needs Improvement.
 </ins>

# Part 2 - Create the Flowchart
## Flowchart:
![SOLEDAD - SCORE CHECKER FLOWCHART](./q1/SOLEDAD_score_checker_FLOWCHART)

# Part 3 - Write the Pseudocode 
```
Function Main

    Declare Integer studentscore

    Input studentscore
    If studentscore < 0 or studentscore > 100
        Output "Invalid score."
    Else
        If studentscore >= 90
            Output "Your score is Outstanding!"
        Else
            If studentscore >= 80
                Output "Your score is Very Satisfactory."
            Else
                If studentscore >= 75
                    Output "Your score is Satisfactory."
                Else
                    Output "Needs Improvement."
                End
            End
        End
    End
End
```

# Part 4 - Clean Code Implementation
## 
![SOLEDAD - Score Checker.py](./q1/Soledad_score_checker.py)

## Part 5

<img width="570" height="443" alt="image" src="https://github.com/user-attachments/assets/a98dfbab-962a-4f05-a0cc-03a440d9cbf9" />

