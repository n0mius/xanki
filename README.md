# xanki
![image](https://github.com/user-attachments/assets/2c6b972a-ae62-4ffe-ab20-9facc431fd02)
xanki is a simple, terminal-based flashcard program inspired by Anki. I wanted a lightweight alternative for the terminal and used it as an excuse to code something in Python.

## Flashcard Format
xanki reads a structured `.txt` file where each flashcard follows this format:
```
#Q
What is the purpose of the subnet mask in conjunction with an IP address? \n\
    A) to uniquely identify a host on a network \n\
    B) to identify whether the address is public or private \n\
    C) to determine the subnet to which the host belongs \n\
    D) to mask the IP address to outsiders \n\
#A
c
#END
```
- Each flashcard starts with `#Q`, followed by the question.
- The answer is placed below `#A`.
- The flashcard is terminated with `#END`
