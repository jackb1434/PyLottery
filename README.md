# PyLottery

### School Project :)

##### Dependencies:
Colorama - colored console text
tqdm - loading bar

```
pip install colorama
```
```
pip install tqdm
```

## or

```
pip3 install colorama
```
```
pip3 install tqdm
```

### How does it work?

When you start the program you are greeted with a the main menu. From there you can choose a selection to navigate to other menus. The following selections include:

[1]: Game Info
[2]: Generate a lottery ticket
[3]: Check your balance ($)
[4]: Exit the program


When you generate a ticket, the program will generate a 7 length list of integers and then
generate a new ticket called temp_ticket which will compare your ticket to the temp_ticket. 
If they match, you win a cash prize from $0-999999. Winning is determined by generating 2 random
numbers, and if they match, you win. The odds are out of 9.