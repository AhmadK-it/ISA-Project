# ISA-Project
main architecture for ISA project 
## Main Architectur for the project 
### Game Class (in game.py module)
the class is created for initiating the game logic and initiating the game base status (init the state)
#### Atributs 
- init is the based file that have the board main state 
- test1 / test2 contains the files for other tests 
- board is the initiated play board based on the data provided by the file and assigned using initBoard function 
- initState is the main state constructed by using the State constructer which takes the play board as argument 
#### Methods
I) the constructer (__init__) 
- initiat the board using the initBoard method 
- initiat the start state (initState)

II) initBoard function takes file and num of rows (n = 4 as default value) and the num of columns (m = 7 as default)
The aime for this function is to read the data for the game board and initiat the board (path - mail points delevery / reseve - truck)
- reads special data from the file provided then merge it with the default data on the board 
- return the board created

III) UCS and A_Star fucntions needed 

### Cell Class (in board.py module)
#### Atributs 
- row is the x axis position for the Cell
- col is the y axis position for the Cell
- struct is the structur in which we will have assigned the Truck or Delevery point or Post point - assigned using the Struct constructer which takes the row and col as arguments 
#### Methods
I) the constructer (__init__) 
- initiat the Cell using the passed params 
- initiat the struct using the Struct constructer

### Struct Class (in board.py module)
#### Atributs 
- row is the x axis position for the Struct in the play board
- col is the y axis position for the Struct in the play board
- mail is the number of mails in at that structer (for the first time it is =0 by default regardless of the type )
- type defines the structer type  (Truck -> 'T ' or Delevery point -> 'D ' or Post point 'P ' or {Path -> '. ' as default})
#### Methods
I) the constructer (__init__) 
- initiat the structer's axis using the passed params 
- initiat the struct type and mail for the first time using the default params

II) setMail function -> never used 

### State Class (in state.py module)
the class is created for keep track of the changes based on the game logic 

#### Atributs 
- board is a local copy of the current play board  
- n is the number of rows (by default =4 assigned using the params in the structer )
- m is the number of columns (by default =7 assigned using the params in the structer )
- parent = None by default to keep track for the parent node of our state for further use in algos
- resM is a list used to store a copy of Post points before any update on the board (to solve passing over issue without losing any data)
- delevM is a list used to store a copy of Delivery points before any update on the board (to solve passing over issue without losing any data)
- cost = 1 the cost for the current state (for using in algo)
- carried =0 is a counter that stores the value of the current carried mails by the truck
- waited =0 is a that stores the value of undelivered mails 

#### Methods
I) the constructer (__init__) 
- initiat all values based on the passed params

II) printBoard function used for visual representation for the board on the console

III) move function
- takes Cell coordinates and list (listStates) to append the new next created states 
- based on the type of the Cell the algo starts the movement - it starts from all possible positions (all Cells without Truck and Building positions)
- then check for keeping within the board coordinates
- define the type of movement and call the right fuction 
- append the new state created by the function to the list passed 

IV) vMove / hMove function
- Move the truck towards the specific free spot 
- keep track of the types and save special structes before making changes to the right list
- rebind the saved structers with the current board state before returning the final board state (adding the removed structers while moving)
- return the final board

V) nextState function
- makes a deep copy of the current passed state 
- finde the new next States from the current state by calling the move method 
- returns the new next states list

VI) checkPoints function
- helper function for saving the passed over Post / Delevery points 
- takes current struct's cell type (type) and cureent state (state) and valid lists 
- append to specific values 

VII) setCarriedMail function
- count the un delevers mails and the only one that reseved by the truck ( mails carried by the truck subtracted from it the delvered mails to the delevered points)
- takes state , struct and truck as params 

VIII) setWaitedMail function
- count the un delevers mails ( contains ones that not reseved by the truck) and ones also reseved by the truck ( mails carried by the truck subtracted from it the delvered mails to the delevered points)
- make locale changes for each state alone based on the current board
- takes state , struct and truck as params 

IX) setDelevMail function
- takes state , struct and truck as params 
- make some local changes on the carried and waited lists and also set the right valus for the mail counter on the specific truck

X) setParent
- set the passed state as parent to the current state 

XI) getRows / getCols
- get the current board coordinates

XII) isGoal 
- meet the end state -> not done 
