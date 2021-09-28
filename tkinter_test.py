import tkinter as tk

card = "H2"
def pass_card():
    pass

def trade_card():
    pass

def rules():
    pass

def test():
    pass

root = tk.Tk()
root.title("Screw Your Neighbor")
x, y = 512, 512
root.geometry(f"{x}x{y}")
root.tk.call('tk', 'scaling', '-displayof', '.', 4)


card = tk.Label(root, text=card).pack()
pass_button = tk.Button(root, text="Pass", command=pass_card).pack()
trade_button = tk.Button(root, text="Trade", command=trade_card).pack()
rule_button = tk.Button(root, text="Rules", command=rules).pack()
root.mainloop()
