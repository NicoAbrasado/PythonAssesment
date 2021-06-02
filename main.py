from tkinter import *
import random

# Variables
background_color = "gray13"
foreground_color = "floralwhite"
btn_color = "mediumseagreen"
names_list = [] 


# Questions and Answers 
# Physics 
phy_qanda = {
  1: ['What is Mechanics?', 'The mechanical components of a car', 'an area of physics concerned with the motion of objects','the interactions between particles','A school of physics which concerns itself with waves',2,'Mechanics']
}
# Computer Science
# Question number: Question, Answer 1, Answer 2, Answer 3, Answer 4, Correct Answer placement, Category 
cs_qanda = {
  1: ['What is python in computer science?','Python is a programming language','Python is a search engine','Python is a type of snake','Python is a famous car brand',1,'Python']
}


class QuizStarter: # Class for the UI, the main menu and username 
    def __init__(self, parent):    
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
        self.continue_button = Button(self.quiz_frame, text="Continue", font=("Tw Cen MT", "13", "bold"), bg="mediumseagreen", command=self.continue_process)
        self.continue_button.grid(row=3,  padx=50, pady=30, sticky=E)  
        self.continue_button.config(width = 8) # button same size as the exit button

        #Exit button 
        self.exit_button = Button(self.quiz_frame, text="Exit", font=("Tw Cen MT", "13", "bold"), bg="indianred", command=self.end_screen)
        self.exit_button.grid(row=3, padx=50 ,pady=30, sticky=W)
        self.exit_button.config(width = 8) # make the button the same size as the continue button

        #Error correction
        self.error_label = Label(self.quiz_frame, text="", font=("Tw Cen MT", "10", "bold"), bg=background_color, fg="indianred")
        self.error_label.grid(row=4,padx=20,pady=10)
   
    def continue_process(self): 
      name = self.entry_box.get()
      if str.isalpha(name) == True and int(len(name)) <= 15: 
          names_list.append(name)
          self.quiz_frame.destroy()
          Selection(root)
          print(names_list)
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
     # Heading for the Quiz Selection
     self.heading_label = Label(self.quiz_frame, text="Which Quiz Would you like to do?", font=("Tw Cen MT", "17", "bold"), bg=background_color, fg=foreground_color)
     self.heading_label.grid(row=0, column = 0, columnspan = 2, pady=20, padx=50)

     self.var1 = IntVar()
     # Computer Science Radio Button
     self.CS_button = Radiobutton(self.quiz_frame, text="Computer Science", font=("Tw Cen MT", "13", "bold"), bg=foreground_color, fg=background_color,value=1, variable=self.var1)
     self.CS_button.grid(row=1, column = 0, padx=15, pady=30)
     self.CS_button.config(width = 17, height = 4)

     # Physics Button
     self.PHY_button = Radiobutton(self.quiz_frame, text="Physics", font=("Tw Cen MT", "13", "bold"),  bg=foreground_color, fg=background_color, value=2, variable=self.var1)
     self.PHY_button.grid(row=1, column = 1, padx=15, pady=30)
     self.PHY_button.config(width = 17, height = 4)

     # Go back to the main menu interface 
     self.back_button = Button(self.quiz_frame, text="Back", font=("Tw Cen MT", "13", "bold"),  bg="indianred", fg=background_color, command=self.return_func)
     self.back_button.grid(row=2, column = 0, pady=40)
     self.back_button.configure(width = 8)
     
     # Submit the answer 
     self.submit_button = Button(self.quiz_frame, text="Submit", font=("Tw Cen MT", "13", "bold"),  bg=btn_color, fg=background_color, command=self.test_setup)
     self.submit_button.grid(row=2, column = 1, pady=40)
     self.submit_button.configure(width = 8)
     
     # Error correction label 
     self.error_show = Label(self.quiz_frame, text="", font=("Tw Cen MT", "10", "bold"), bg=background_color, fg="indianred")
     self.error_show.grid(row=3,column=0,pady=10,columnspan=2)

  # Start the questions 
  def test_setup(self):
    global chosen_quiz 
    quiz_choice = self.var1.get()
    if quiz_choice == 2: 
       chosen_quiz = phy_qanda
       print(chosen_quiz[1][0])
       self.quiz_frame.destroy()
       Quiz(root)

    elif quiz_choice == 1: 
       chosen_quiz = cs_qanda
       print(chosen_quiz[1][0])
       self.quiz_frame.destroy()
       Quiz(root)
    else: 
       self.error_show.configure(text="")
       self.error_show.configure(text="Please select an option before continuing!")
  
  # Return to the first screen function 
  def return_func(self): 
    names_list.clear()
    self.quiz_frame.destroy()
    QuizStarter(root)
    print(names_list)

class Quiz: # Actual quiz 
  def __init__(self, parent):
    self.quiz_frame = Frame(parent, bg=background_color, padx=100, pady=100)
    # Geometry and placement of the UI
    self.quiz_frame.grid()

    self.question_label = Label(self.quiz_frame, text=chosen_quiz[1][0], font=("Tw Cen MT", "17", "bold"), bg=background_color, fg=foreground_color)
    self.question_label.grid(row=1,padx=10,pady=10)

     
if __name__ == "__main__":
  root = Tk()
  root.title("NCEA Study buddy")
  quiz_instance = QuizStarter(root) #instantiation, making an instance of the class Quiz
  root.mainloop()#so the frame doesnt dissapear