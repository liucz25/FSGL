import tkinter
from tkinter import ttk

root = tkinter.Tk()
root.title("Change Counter")

ttk.Separator(root).grid(row=3, columnspan=5, sticky="ew")

dollarCoins = tkinter.IntVar()
halfDollars = tkinter.IntVar()
quarters = tkinter.IntVar()
dimes = tkinter.IntVar()
nickels = tkinter.IntVar()
pennies = tkinter.IntVar()

dollarCoinsTotal = tkinter.DoubleVar()
halfDollarTotal = tkinter.DoubleVar()
quartersTotal = tkinter.DoubleVar()
dimesTotal = tkinter.DoubleVar()
nickelsTotal = tkinter.DoubleVar()
penniesTotal = tkinter.DoubleVar()

titleLabel = tkinter.Label(root, text = "Change Counter")
titleLabel.grid(row=1, column=1, columnspan = 4)

def Totals():
    dollarCoinsTotal.set (float(dollarCoins.get()))
    halfDollarTotal.set(float(halfDollars.get()* 0.50))
    quartersTotal.set(float(quarters.get()* 0.25))
    dimesTotal.set(float(dimes.get()* 0.10))
    nickelsTotal.set(float(nickels.get()* 0.05))
    penniesTotal.set(float(pennies.get()* 0.01))

titleLabel = tkinter.Label(root, text = "Enter the number of each coin type and hit compute")
titleLabel.grid(row=2, column=1, columnspan =4)

dollarCoinsLabel = tkinter.Label(root, text = "Dollar Coins")
dollarCoinsLabel.grid(row=4, column=1, pady= 5)

dollarCoinsEntry = tkinter.Entry(root, textvariable = dollarCoins)
dollarCoinsEntry.grid(row=4, column=2, pady= 5, padx = 10)

halfDollarsLabel = tkinter.Label(root, text = "Half Dollars")
halfDollarsLabel.grid(row=5, column=1, pady= 5, padx = 10)

halfDollarsEntry = tkinter.Entry(root, textvariable = halfDollars)
halfDollarsEntry.grid(row=5, column=2, pady= 5)

quartersLabel = tkinter.Label(root, text = "Quarters")
quartersLabel.grid(row=6, column=1, pady= 5, padx = 10)

quartersEntry = tkinter.Entry(root, textvariable = quarters)
quartersEntry.grid(row=6, column=2, pady= 5)

dimesLabel = tkinter.Label(root, text = "Dimes")
dimesLabel.grid(row=7, column=1, pady= 5, padx = 10)

dimesEntry = tkinter.Entry(root, textvariable = dimes)
dimesEntry.grid(row=7, column=2, pady= 5)

nickelsLabel = tkinter.Label(root, text = "Nickels")
nickelsLabel.grid(row=8, column=1, pady= 5)

nickelsEntry = tkinter.Entry(root, textvariable = nickels)
nickelsEntry.grid(row=8, column=2, pady= 5, padx = 10)

penniesLabel = tkinter.Label(root, text = "Pennies")
penniesLabel.grid(row=9, column=1, pady= 5, padx = 10)

penniesEntry = tkinter.Entry(root, textvariable = pennies)
penniesEntry.grid(row=9, column=2, pady= 5)

dollarCoinsLabelText = tkinter.Label(root, text = "Dollar Coins Value: $")
dollarCoinsLabelText.grid(row=4, column=3, pady= 50, padx = 10)

dollarCoinsLabelValue = tkinter.Label(root, textvariable = dollarCoinsTotal)
dollarCoinsLabelValue.grid(row=4, column=4, pady= 5)

halfDollarLabelText = tkinter.Label(root, text = "Half Dollar Value: $")
halfDollarLabelText.grid(row=5, column=3, pady= 5, padx = 10)

halfDollarLabelValue = tkinter.Label(root, textvariable = halfDollarTotal)
halfDollarLabelValue.grid(row=5, column=4, pady= 5)

quartersLabelText = tkinter.Label(root, text = "Quarters Value: $")
quartersLabelText.grid(row=6, column=3, pady= 5, padx = 10)

quartersLabelValue = tkinter.Label(root, textvariable = quartersTotal)
quartersLabelValue.grid(row=6, column=4, pady= 5)

dimesLabelText = tkinter.Label(root, text = "Dimes Value: $")
dimesLabelText.grid(row=7, column=3, pady= 5, padx = 10)

dimesLabelValue = tkinter.Label(root, textvariable = dimesTotal)
dimesLabelValue.grid(row=7, column=4, pady= 5)

nickelsLabelText = tkinter.Label(root, text = "Nickels Value: $")
nickelsLabelText.grid(row=8, column=3, pady= 5, padx = 10)

nickelsLabelValue = tkinter.Label(root, textvariable = nickelsTotal)
nickelsLabelValue.grid(row=8, column=4, pady= 5)

penniesLabelText = tkinter.Label(root, text = "Pennies Value: $")
penniesLabelText.grid(row=9, column=3, pady= 5, padx = 10)

penniesLabelValue = tkinter.Label(root, textvariable = penniesTotal)
penniesLabelValue.grid(row=9, column=4, pady= 5)

calculateButton = tkinter.Button(root, text = "Compute", command = Totals)
calculateButton.grid(row=10, column=1)


root.mainloop()