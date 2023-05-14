# Import Tkinter
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import scrolledtext

# Initialize App
app = Tk()  

# Initialize Stored Variables

crustOptions = [
    "Hand Tossed",
    "Thin Crust",
    "Pan Pizza"
]

crustPrices = {
   "Hand Tossed": 1,
   "Thin Crust": 1,
   "Pan Pizza": 2,
}

sauceOptions = [
    "Tasty Classic",
    "Bold Marinara Sauce",
    "Sweet Tomato Sauce",
    "BBQ Sauce",
    "Ranch Sauce"
]

saucePrices = {
   "Tasty Classic": 0.50,
   "Bold Marinara Sauce": 0.50,
   "Sweet Tomato Sauce": 0.50,
   "BBQ Sauce": 0.50,
   "Ranch Sauce": 0.50
}

cheeseOptions = [
    "Less Cheese",
    "Normal Cheese",
    "Extra Cheese"
]

cheesePrices = {
   "Less Cheese": 1,
   "Normal Cheese": 1,
   "Extra Cheese": 1.50
}

sizeOptions = [
    "Mini Pizza 8 Inch",
    "Small Pizza 10 Inch",
    "Medium Pizza 12 Inch",
    "Large Pizza 14 Inch",
    "Extra Large Pizza 16 Inch"
]

sizePrices = {
    "Mini Pizza 8 Inch": 2,
    "Small Pizza 10 Inch": 3,
    "Medium Pizza 12 Inch": 4,
    "Large Pizza 14 Inch": 6,
    "Extra Large Pizza 16 Inch": 10
}

toppingOptions = [
    "Pepperoni",
    "Sausage",
    "Ham",
    "Onions",
    "Peppers",
    "Mushrooms",
    "Pineapple",
    "Banana Pepper"
]

toppingPrices = {
    "None":0,
    "Pepperoni":1,
    "Sausage":1,
    "Ham":1,
    "Onions":1,
    "Peppers":1,
    "Mushrooms":1,
    "Pineapple":1,
    "Banana Pepper":1
}

# Set Up Menu Listbox Values

menuListValues = ['Cheese Pizza','Pepperoni Pizza','Deluxe Pizza','Vegetable Pizza','Sausage Pizza','Custom Pizza']
list1 = tk.StringVar(value=menuListValues)

# Set Up List Storage of Cart
itemCart = []
crustCart = []
sauceCart = []
cheeseCart = []
sizeCart = []
top1Cart = []
top2Cart = []

# Define Generate Ticket Function

def generate_ticket():
    output = ''
    x = 0
    for i in itemCart:
        output = output + "Item: " + itemCart[x] + "\n"
        output = output + "Crust Choice: " + crustCart[x] + " - $" + str(crustPrices[crustCart[x]]) + "\n"
        output = output + "Sauce Choice: " + sauceCart[x] + " - $" + str(saucePrices[sauceCart[x]]) + "\n"
        output = output + "Cheese Choice: " + cheeseCart[x] + " - $" + str(cheesePrices[cheeseCart[x]]) + "\n"
        output = output + "Size Choice: " + sizeCart[x] + " - $" + str(sizePrices[sizeCart[x]]) + "\n"
        output = output + "Topping 1 Choice: " + top1Cart[x] + " - $" + str(toppingPrices[top1Cart[x]]) + "\n"
        output = output + "Topping 2 Choice: " + top2Cart[x] + " - $" + str(toppingPrices[top2Cart[x]]) + "\n\n"
        output = output + "Total : $" + str(round(crustPrices[crustCart[x]]+saucePrices[sauceCart[x]]+cheesePrices[cheeseCart[x]]+sizePrices[sizeCart[x]]+toppingPrices[top1Cart[x]]+toppingPrices[top2Cart[x]],2)) + "\n\n"
        x = x + 1
    print(output)
    return output

# Define Add Order to Cart Function

def add_to_cart():
    if pizzaText.cget("text") != 'Customize Order':
        itemCart.append(pizzaText.cget("text"))
        crustCart.append(crustClicked.get())
        sauceCart.append(sauceClicked.get())
        cheeseCart.append(cheeseClicked.get())
        sizeCart.append(sizeClicked.get())
        top1Cart.append(topping1Clicked.get())
        top2Cart.append(topping2Clicked.get())
        cartListB.insert('end',pizzaText.cget("text"))
        print(itemCart,crustCart,sauceCart,cheeseCart,sizeCart,top1Cart,top2Cart)

# Define New Window Function

def open_ticket_window():
     
    # Define Ticket Window
    ticketWindow = Toplevel(app)
 
    # Set Ticket Window Title
    ticketWindow.title("Order Ticket")
 
    # Set Geometry of Ticket Window
    ticketWindow.geometry("500x300")

    # Create Text Area to Display Ticket
    text_area = scrolledtext.ScrolledText(ticketWindow,width = 500,height = 300,font = ("Times New Roman",12))
 
    text_area.pack()

    text_area.insert(END, generate_ticket())

def clear_order():
    itemCart.clear()
    crustCart.clear()
    sauceCart.clear()
    cheeseCart.clear()
    sizeCart.clear()
    top1Cart.clear()
    top2Cart.clear()
    cartListB.delete(0,END)

def quit_app():
    app.destroy()


# Datatype of Dropdown Menu Text

crustClicked = StringVar()
sauceClicked = StringVar()
cheeseClicked = StringVar()
sizeClicked = StringVar()
topping1Clicked = StringVar()
topping2Clicked = StringVar()
  
# Set Initial Dropdown Menu Text

crustClicked.set('Select Crust')
sauceClicked.set('Select Sauce')
cheeseClicked.set('Select Cheese')
sizeClicked.set('Select Size')
topping1Clicked.set('Select Topping 1')
topping2Clicked.set('Select Topping 2')

# App Title
app.title("Welcome to Pizza Order")

# Construct Frame 1
frame1 = PanedWindow(orient ='vertical')

# Displaying the frame1 in row 0 and column 0
frame1.grid(row=0, column=0)

# Constructing Customize Order Text
quickPickText = Label(frame1, text="Quick Pick Order")

# Constructing Add to Order Button
addOrderB = Button(frame1, text="Add to Order", command= add_to_cart)

# Constructing Quit Button
quitB = Button(frame1, text="Exit Application", command= quit_app)

# Constructing Menu Listbox
menuListB = Listbox(frame1,listvariable=list1)

# Displaying The Widgets in Frame 1
menuListB.pack()
quickPickText.pack()
addOrderB.pack()
quitB.pack()

# Construct Frame 2
frame2 = PanedWindow(orient ='vertical')

# Displaying the Frame 2 in Row 0 Column 1
frame2.grid(row=0, column=1)

# Constructing Widgets in Frame 2
b2 = Button(frame2, text="Tomato")
pizzaText = Label(frame2, text="Customize Order")

# Construct Option Menu Widgets in Frame 2
crustDrop = OptionMenu( frame2 , crustClicked , *crustOptions )
sauceDrop = OptionMenu( frame2 , sauceClicked , *sauceOptions )
cheeseDrop = OptionMenu( frame2 , cheeseClicked , *cheeseOptions )
sizeDrop = OptionMenu( frame2 , sizeClicked , *sizeOptions )
topping1Drop = OptionMenu( frame2 , topping1Clicked , *toppingOptions )
topping2Drop = OptionMenu( frame2 , topping2Clicked , *toppingOptions )

imgLogo = ImageTk.PhotoImage(Image.open("order.png"))
logoImgLabel = Label(frame2, image=imgLogo) 

imgPizza = ImageTk.PhotoImage(Image.open("pizza.png"))
pizzaImgLabel = Label(frame2, image=imgPizza) 

# Displaying the Widgets in Frame 2
logoImgLabel.pack()
pizzaText.pack()
crustDrop.pack()
sauceDrop.pack()
cheeseDrop.pack()
sizeDrop.pack()
topping1Drop.pack()
topping2Drop.pack()
pizzaImgLabel.pack()

# Construct Frame 3
frame3 = PanedWindow(orient ='vertical')

# Displaying the Frame 2 in Row 0 Column 2
frame3.grid(row=0, column=2)

# Constructing Cart List Box in frame3
cartListB = Listbox(frame3)

# Constructing Review Order Text
reviewText = Label(frame3, text="Review Order")

# Constructing the Generate Ticket Button in Frame 3
b3 = Button(frame3, text="Generate Ticket", command = open_ticket_window)

# Constructing the Clear Button in Frame 3
clearB = Button(frame3, text="Clear", command = clear_order)

# Displaying the Widgets in Frame 3
cartListB.pack()
reviewText.pack()
b3.pack()
clearB.pack()

# Set Quick Pick Orders When Selected

def selected_item(item):
    for i in menuListB.curselection():
        pizzaText.configure(text=menuListB.get(i))
        if menuListB.get(i) == 'Cheese Pizza':
            crustClicked.set('Hand Tossed')
            sauceClicked.set('Tasty Classic')
            cheeseClicked.set('Extra Cheese')
            sizeClicked.set('Medium Pizza 12 Inch')
            topping1Clicked.set('None')
            topping2Clicked.set('None')
        if menuListB.get(i) == 'Pepperoni Pizza':
            crustClicked.set('Hand Tossed')
            sauceClicked.set('Bold Marinara Sauce')
            cheeseClicked.set('Normal Cheese')
            sizeClicked.set('Medium Pizza 12 Inch')
            topping1Clicked.set('Pepperoni')
            topping2Clicked.set('None')
        if menuListB.get(i) == 'Sausage Pizza':
            crustClicked.set('Hand Tossed')
            sauceClicked.set('Bold Marinara Sauce')
            cheeseClicked.set('Normal Cheese')
            sizeClicked.set('Medium Pizza 12 Inch')
            topping1Clicked.set('Sausage')
            topping2Clicked.set('None')
        if menuListB.get(i) == 'Deluxe Pizza':
            crustClicked.set('Pan Pizza')
            sauceClicked.set('Tasty Classic')
            cheeseClicked.set('Extra Cheese')
            sizeClicked.set('Large Pizza 14 Inch')
            topping1Clicked.set('Pepperoni')
            topping2Clicked.set('Sausage')
        if menuListB.get(i) == 'Vegetable Pizza':
            crustClicked.set('Hand Tossed')
            sauceClicked.set('Sweet Tomato Sauce')
            cheeseClicked.set('Normal Cheese')
            sizeClicked.set('Medium Pizza 12 Inch')
            topping1Clicked.set('Onions')
            topping2Clicked.set('Peppers')
        if menuListB.get(i) == 'Custom Pizza':
            crustClicked.set('Hand Tossed')
            sauceClicked.set('Sweet Tomato Sauce')
            cheeseClicked.set('Normal Cheese')
            sizeClicked.set('Medium Pizza 12 Inch')
            topping1Clicked.set('None')
            topping2Clicked.set('None')


# Bind List Box Selection to Selected Item Function
menuListB.bind("<<ListboxSelect>>", selected_item)

# Make the App Window a Fixed Size

app.resizable(0, 0)

# Make the Main Loop

app.mainloop()