import tkinter as tk
import random
import time

root = tk.Tk()

frame1 = tk.Frame(root)
frame2 = tk.Frame(root)
frame3 = tk.Frame(root)

buttond = tk.Button(master=(frame3), text="done", command = lambda: exit())
buttond.pack()
# scores[-1]["uscore"] = 0
# scores[-1]["cscore"] = 0
scores = [{"cscore":0, "uscore":0}]
label3 = tk.Label(master = frame3, text=f"""
Player | Computer
----------------
{scores[-1]["uscore"]} | {scores[-1]["cscore"]}
""")


root.title("Guessing Game")
hint_label = tk.Label(master = frame1, text="")
num=random.randint(0, 100)

def reset_game():
  global num
  label2.config(text = " ")
  scores.append({"cscore":0, "uscore":0})
  frame2.pack_forget()
  frame3.pack_forget()
  frame1.pack()
  hint_label.config(text="")
  num=random.randint(0, 100)
  
buttonr = tk.Button(master = frame3, text="restart" ,command = reset_game)

def comg():
  res= tarea2.get("1.0", tk.END).strip("\n")
  min = 0
  max =(101)
  while True:
    num = ((min+max)//2)
    scores[-1]["cscore"] += 1
    res=int(res)
    if num<res:
      min = num
    elif num>res:
      max=num
    else:
      label2.config(text = "It guessed your number in " + str(scores[-1]["cscore"]) + " guesses.")
      break

  result = ""
  for game in scores:
    result+=f"{game['uscore']} | {game['cscore']}\n"
  
  frame3.pack()
  label3.config(text= f"""
Player | Computer
----------------
{result}
""")
  tarea2.delete("1.0",tk.END)
  # create resart button and done button
  
  buttonr.pack()
def swapscreen():
  frame1.pack_forget()
  frame2.pack()

def sub_g():
  res= tarea.get("1.0", tk.END).strip("\n")
  tarea.delete("1.0",tk.END)
  try:
    res = int(res)
    scores[-1]["uscore"] +=1
    if num > res:
      hint_label.config(text = "Too low")
    elif res > num:
      hint_label.config(text = "Too high")
    else:
      hint_label.config(text = "Correct in " + str(scores[-1]["uscore"]) + " guesses.")
      time.sleep(3.1419)
      swapscreen()
  except Exception as err:
    hint_label.config(text = "Error")
    print (err)

frame1.pack()
label = tk.Label(master = frame1, text="Enter a number between 1 and 100")
label.pack()
tarea = tk.Text(master = frame1, width = 30, height= 1)
tarea.pack()
button = tk.Button(master = frame1, text="submit" ,command = sub_g)
button.pack()
hint_label.pack()

tarea2 = tk.Text(master = frame2, width = 30, height= 1)
tarea2.pack()
button2 = tk.Button(master = frame2, text="submit" ,command = comg)
button2.pack()
label2 = tk.Label(master = frame2, text="Enter a number for the computer to guess.")
label2.pack()

label3.pack()

root.mainloop()
