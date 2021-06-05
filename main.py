from tkinter import *
import random

# Variables
background_color = "gray13"
foreground_color = "floralwhite"
btn_color = "mediumseagreen"
names_list = [] 
asked = [] 

def randomiser(): 
  global qnum 

  qnum = random.randint(1,15)

  if qnum not in asked: 
    asked.append(qnum)
  elif qnum in asked: 
    randomiser()

randomiser()

# Questions and Answers 
# Physics 
phy_qanda = {
  1: ['What is Mechanics?', 'The mechanical components of a car', 'an area of physics concerned with the motion of objects','the interactions between particles','A school of physics which concerns itself with waves',2,'Mechanics'],
  2: ['Who theorised the existence of electrons?','JJ Thompson','John Dalton','Ernest Rutherford','Issac Newton',1,'Nuclear Physics'],
  3: ['What are the two different optics in physics?','Light and Sound','Ray and Wave','Dynamic and Mono','Rays and Orbits',2,'Waves'],
  4: ['What is Newtons first law?','For every action there is an equal and opposire reaction','The amount of acceleration of a body is proportional to the acting force','Gravity acts towards the centre','An object at rest will remain at rest',4,'Mechanics'],
  5: ['What is the mass of an electron?','1','2','1/1836','1.1836',3,'Nuclear Physics'],
  6: ['An image is virtual when..','..The rays cross each other','..The rays seem to cross each other','..The image is above the mirror','..The image is in the mirror',2,'Waves'],
  7: ['How do you calculate centripetal force?','a = V^2/r','F = ma','A = V/t','F = mv^2/r',4,'Mechanics'],
  8: ['An alpha particle is..','High velocity, but light electrons','Energy from the electromagnetic spectrum','A heavy, slow and positively charged helium nucleus','An ionised particle',3,'Nuclear Physics'],
  9: ['What is the equation for magnification?','i/O = M','1/i + 1/0 = 1/f = 2/r[f=R/2]','A = V/t','C = 2r',1,'Waves'],
  10: ['‘For every action there is an equal and opposite reaction’ describes...','Newton’s first law of motion','The Square Cube law','Newton’s fourth law of motion','Newton’s third law of motion',4,'Mechanics'],
  11: ['What charge is a Beta particle?','Neutral','Positive','All','Negative',4,'Nuclear Physics'],
  12: ['Wave optics believes that..','..Light is made out of rays','..Light can be split up from rays into waves','..Light is made up of waves','..Light is formed by waves and rays',3,'Waves'],
  13: ['What forces effected the projectile in it’s motion?','Only Gravity','Gravity and Horozontial force','Gravity and Light','Nothing, it is only directed by the force exerted',1,'Mechanics'],
  14: ['What is half-life in physics?','Half life is a popular video game franchise','The time it takes for the number of undecayed nuclei to fall to half its original number','The time it takes for decayed nuclei to regenerate','The half point for an organisim',2,'Nuclear Physics'],
  15: ['What is refraction?','The angle when a ray hits a reflective surface','When a light ray goes from one medium to another','The act of light travelling through space in waves','Light creating an image off of a reflective surface',2,'Waves']
}
# Computer Science
# Question number: Question, Answer 1, Answer 2, Answer 3, Answer 4, Correct Answer placement, Category 
cs_qanda = {
  1: ['What is python in computer science?','Python is a programming language','Python is a search engine','Python is a type of snake','Python is a famous car brand',1,'Python'],
  2: ['What does the heuristic, ‘Match with the real world’ deal with?','Make the user able to edit and change their answers','Use familiar icons and concepts found in the real world','Conventions in programming','Able to show the user the status of the system',2,'Heuristics'],
  3: ['What is an algorithm?','A version of the windows operating system','A type of programming technique that is similar to a class','A finite ordered sequence of steps to solve a problem','The observation of sequences within a computer program',3,'Algorithms'],
  4: ['What is the data type for this?: 1.4','Float','Integer','String','Boolean',1,'Python'],
  5: ['Who made the design heuristics?','Jakob Nielsen','Jacob Nielsen','John Nelson','Rolf Molich',1,'Heuristics'],
  6: ['When can Algorithms be used?','Only in Python','Any time to design a solution to a problem','When finding an error','Only when repairing computers',2,'Algorithms'],
  7: ['What does this sign mean in python?: !=','Approximately','If this happens do this','Equal to','Not equal to',4,'Python'],
  8: ['What is the 9th heuristic?','Aesthetic and Minimalist Design','Recognition Rather than recall','Algorithms and Databases','Diagnose and Recover from errors',4,'Heuristics'],
  9: ['How do you measure algorithm efficiency in terms of run time and space?','F equations','Small R cubits','Big O Notation','Y5 Rankings',3,'Algorithms'],
  10: ['What does an If statement do?','Checks if something is true then executes it','Compares 2 values and returns a true or false','While a statement is true, it will loop a indefinitely until it is not','A block of code that only runs if called.',1,'Python'],
  11: ['What does the Heuristic ‘Diagnose Recover and Errors’ deal with?','Allows access for more efficient processes','Gives the user the freedom to personalise their experience','After making an error, the user will be able to recover easily','Follow already existing conventions',3,'Heuristics'],
  12: ['What is the worst case for a search and sort algorithm?','O(n)','O(n/2)','F - (QT)','Y5 - 6',1,'Algorithms'],
  13: ['‘Address = []’ is an example of what in python?','Variable','Integer','Dictionary','List',4,'Python'],
  14: ['‘Clean, Uncluttered, Visible’ is an example of what heuristic?','Help and Documentation','Flexibility and Efficiency of use','Aesthetic and minimalist design','Consistency and standards',3,'Heuristics'],
  15: ['What is the best case for a quick sort?','Y4^4','F + (n^6)','n*log(n)','O(f^log(6)',3,'Algorithms']
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

    self.question_label = Label(self.quiz_frame, text=chosen_quiz[qnum][0], font=("Tw Cen MT", "17", "bold"), bg=background_color, fg=foreground_color)
    self.question_label.grid(row=1,padx=10,pady=30)

    self.var1 = IntVar()

    self.rb1 = Radiobutton(self.quiz_frame, text=chosen_quiz[qnum][1],font=("Tw Cen MT", "11", "bold"),bg=foreground_color, fg=background_color,value=1,padx=10,pady=10,variable=self.var1)
    self.rb1.grid(row=2,sticky=W)

    self.rb2 = Radiobutton(self.quiz_frame, text=chosen_quiz[qnum][2],font=("Tw Cen MT", "11", "bold"),bg=foreground_color, fg=background_color,value=2,padx=10,pady=10,variable=self.var1)
    self.rb2.grid(row=3,sticky=W)

    self.rb3 = Radiobutton(self.quiz_frame, text=chosen_quiz[qnum][3],font=("Tw Cen MT", "11", "bold"),bg=foreground_color, fg=background_color,value=3,padx=10,pady=10,variable=self.var1)
    self.rb3.grid(row=4,sticky=W)

    self.rb4 = Radiobutton(self.quiz_frame, text=chosen_quiz[qnum][4],font=("Tw Cen MT", "11", "bold"),bg=foreground_color, fg=background_color,value=4,padx=10,pady=10,variable=self.var1)
    self.rb4.grid(row=5,sticky=W)

     
if __name__ == "__main__":
  root = Tk()
  root.title("NCEA Study buddy")
  quiz_instance = QuizStarter(root) #instantiation, making an instance of the class Quiz
  root.mainloop()#so the frame doesnt dissapear
