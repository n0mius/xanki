# xanki
**xanki** is a simple, terminal-based flashcard program inspired by Anki.

## Flashcard Format
xanki reads a structured `.txt` file where each flashcard follows this format:
```
#F
1+1=?

#A
2

#END
```
- Each flashcard starts with `#F`, followed by the question.
- The answer is placed below `#A`.
- The flashcard is terminated with `#END`.
