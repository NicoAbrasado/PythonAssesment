from tkinter import *

background_color = "gray13"
foreground_color = "floralwhite"
names_list = [] 

class QuizStarter: # Class for the UI, the main menu and username 
    def __init__(self, parent):
        
        # background_color = "gray13" 
        # foreground_color = "floralwhite"
        # Frame of the UI
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        # Geometry and placement of the UI
        self.quiz_frame.grid()

        #Widgets
        # Main header
        self.heading_label = Label(self.quiz_frame, text="NCEA Study Buddy",font=("Tw Cen MT","20","bold"),bg=background_color,fg=foreground_color)
        self.heading_label.grid(row=0, padx=100)

        # Username Label
        self.user_label = Label(self.quiz_frame, text="Enter your name:", font=("Tw Cen MT","14"),bg=background_color, fg=foreground_color)
        self.user_label.grid(row=1,pady=20,padx=100)
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=100, pady=20)
        self.entry_box.configure(width=30)
      
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="mediumseagreen", command=self.continue_process)
        self.continue_button.grid(row=3,  padx=50, pady=30, sticky=E)  
        self.continue_button.config(width = 8) # button same size as the exit button

        #Exit button 
        self.exit_button = Button(self.quiz_frame, text="Exit", font=("Helvetica", "13", "bold"), bg="indianred", command=self.end_screen)
        self.exit_button.grid(row=3, padx=50 ,pady=30, sticky=W)
        self.exit_button.config(width = 8) # make the button the same size as the continue button

        #Error correction
        self.error_label = Label(self.quiz_frame, text="", font=("Helvetica", "9","bold"), bg=background_color, fg="indianred")
        self.error_label.grid(row=4,padx=20,pady=10)
   
    def continue_process(self): 
      name = self.entry_box.get()
      if str.isalpha(name) == True and int(len(name)) <= 15: 
        names_list.append(name)
        self.quiz_frame.destroy()
        Selection(root)
      else:
         self.error_label.configure(text = "")
         self.error_label.configure(text = "We only accept names in the alphabet and under 15 letters!")
    
    def end_screen(self): 
      root.withdraw()
    
class Selection: # Class for the quiz selection interface
  def __init__(self, parent): 
    self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
    # Geometry and placement of the UI
    self.quiz_frame.grid()

    self.heading_label = Label(self.quiz_frame, text="test", bg=background_color, fg=foreground_color)
    self.heading_label.grid(row=0, pady=20, padx=100)

    self.CS_button = Button(self.quiz_frame, text="Computer Science", bg=foreground_color, fg=background_color)
    self.CS_button.grid(row=1, padx=50, pady=30, sticky=W)

    self.PHY_button = Button(self.quiz_frame, text="Physics", bg=foreground_color, fg=background_color)
    self.PHY_button.grid(row=1, padx=50, pady=30, sticky=E)



if __name__ == "__main__":
  root = Tk()
  root.title("NCEA Study buddy")
  quiz_instance = QuizStarter(root) #instantiation, making an instance of the class Quiz
  root.mainloop()#so the frame doesnt dissapear
