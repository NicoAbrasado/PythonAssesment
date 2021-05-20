from tkinter import *

class QuizStarter: # Class for the UI, the main menu and username 
    def __init__(self, parent):
        background_color = "gray13" 
        foreground_color = "floralwhite"
        # Frame of the UI
        self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
        # Geometry and placement of the UI
        self.quiz_frame.grid()

        #Widgets
        # Main header
        self.heading_label = Label(self.quiz_frame, text="NCEA Study Buddy",font=("Tw Cen MT","20","bold"),bg=background_color,fg=foreground_color)
        self.heading_label.grid(row=0, padx=100)

        # Username Label
        self.user_label = Label(self.quiz_frame, text="Enter your username", font=("Tw Cen MT","14"),bg=background_color, fg=foreground_color)
        self.user_label.grid(row=1,pady=20,padx=100)
        
        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=100, pady=20)
      
        #continue button
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Helvetica", "13", "bold"), bg="mediumseagreen")
        self.continue_button.grid(row=3,  padx=50, pady=20, sticky=W)  

        #Exit button 
        self.exit_button = Button(self.quiz_frame, text="Exit", font=("Helvetica", "13", "bold"), bg="mediumseagreen")
        self.exit_button.grid(row=3, padx=50,pady=20, sticky=E)
                  
if __name__ == "__main__":
  root = Tk()
  root.title("NCEA Study buddy")
  quiz_instance = QuizStarter(root) #instantiation, making an instance of the class Quiz
  root.mainloop()#so the frame doesnt dissapear
