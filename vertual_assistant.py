

#   ----------THIS INTENDATION HAS ALL THE NECESSARY MODULES WHICH ARE BEING USED. ALL THE------------------------------
#        ------MODULES USED ARE OPEN-SOURCE, SO THAT THERE ARE NOT ANY COPY WRITE CLAMES.-------------------------------


from tkinter import *
from tkinter import messagebox as mb
import pyttsx3
import random
from datetime import datetime
import wikipedia
import webbrowser
import os
import requests
#  ------------------------WIDGET CLASS--------------------------------------------------------------------------------
#          THIS IS THE MAIN AND ONLY CLASS OF THE APPLICATION AND ALSO THE MOST IMPORTANT ONE.
#          IT HAS ALL THE NECESSARY FUCTIONS, LISTS, CONDITION AND INIT FUCTION.
#  ---------------------------------------------------------------------------------------------------------------------


class Widget:
    # ------------------------------------------------------KEY WORD LISTS----------------------------------------------
    #     THESE ARE ALL THE LIST WHICH CONTAINS IMPORTANT KEYWORDS WHICH THE pravi CAN USE.
    # ------------------------------------------------------------------------------------------------------------------

    greet = ['Hey Whats up! How are you doing', 'hi ', 'namaste ! I am your Assistant', ' How may I help You']
    how = ['I am Fine Sir, What about You', 'I am fine as always', 'what you think', 'just fine!!']
    name = ['You Can call me your assistant like jarvis', 'My Name Is pravi', 'you named me pravi as your assistant ',
            'You Should Know this, My name is pravi']
    creator = ['prajjval pramod amd ujjval made me', 'I was Made by 3 members',
               'One And only,prajjval pramod amd ujjval', 'Best in the World, prajjval and team']
    can = ['I Can Do Everything .', 'Just Give Me A Try And Figure This Out.',
           'What you Coded Within Me ;) ', 'Your Choice']
    c_un = ["I did'nt get that", 'What You Said?', 'I was Unable To Understand', 'I have some Bugs Because of you']
    here = ['To Help You Out', 'To Help You To Do Tasks', 'To Be Your Assistant', 'You Called me, Thatwise']
    frd = ['I will Feel Lucky To Be Your Friend', 'Yaa Of cource']
    me = ['You Told Me Your Name, prajjval', 'I Think That\'s ujjval', 'Your Name That I Know Is prajjval']
    thanks = ['My Pleasure', 'Welcome', 'Ohh Don\'t amberis me by saying thanks ', 'So Sweet!!']

    # ------------------------------------------------------------------------------------------------------------------
    # -------------------------------------------------ABOUT US FUNCTION------------------------------------------------

    def more(self):

        more = Tk()
        more.configure(bg='powder blue')
        more.geometry('600x600')
        more.title('my assistant')
        Label(more, text='ask me - The Virtual Assistant', bg='powder blue', font=('Arial Black', 10, 'bold')).pack()
        Label(more, text='By: prajjval', bg='powder blue', font=('Arial Black', 10, 'bold')).pack()
        out = 'My Name Is pravi. I Was Created By prajjval ujjwal and pramod. \n they Made Me Using Python Language. ' \
              'I Was Made\n As A Project For them. But Later I Turned Really Well.\n ' \
              'So they Started Working Really Hard On Me.' \
              ' their\n Progress In Me Was Just Great. So, Now I Am their One\n ' \
              'Of The Dream Project Which they are Planning\n ' \
              'To Build For Cross-Platform.'
        Label(more, text=out, bg='powder blue', font=('Arial Black', 10, 'bold')).pack()
        Label(more, text='Contact us at:\n750932214', bg='powder blue', font=('Arial Black', 10, ' bold'))\
            .pack(side=LEFT)

        Button(more, text='Narrate', font=('Arial Black', 10, 'bold'), command=lambda: self.speak(out)).pack(side=RIGHT,
                                                                                                             padx=10)
        more.mainloop()

# ----------------------------------------------------------------------------------------------------------------------
# --------------------------------ENGINE FOR SPEAKING-------------------------------------------------------------------
#         THESE VARIABLES ARE  BUILDING AN ENGINE WHICH THE SPEAK FUNCTION IS USING.
# ----------------------------------------------------------------------------------------------------------------------
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)

# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------PRINTING FUNC------------------------------------------------------------------
#                THIS FUCTION PRINTS THE pravi'S RESPONCE TO SCREEN.
# ----------------------------------------------------------------------------------------------------------------------

    def printing_func(self, out):
        self.text_box2.delete(1.0, END)
        self.text_box2.insert(INSERT, out)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------SPEAK FUNCTION----------------------------------------------------------------------------------
#           THIS FUNCTION SPEAKS THE pravi'S RESPONCE
# ----------------------------------------------------------------------------------------------------------------------
    def speak(self, s):
        self.engine.say(s)
        self.engine.runAndWait()

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------SEND FUNC-------------------------------------------------------------------------------------
#        THIS FUCTION IS BEING USED TO SEND USER_INPUT TO pravi
# ----------------------------------------------------------------------------------------------------------------------
    def send_func(self):
        user_input = self.search_var.get().lower()
        self.search_var.set('')
        self.text_box1.delete(1.0, END)
        self.text_box1.insert(INSERT, user_input)

# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------CONDITIONS-----------------------------------------------------------------------
# THESE ARE CONDITIONS WHICH THE pravi CHECKS. HE RESPOND TO THE MOST RELEVENT CONDITION.
# ----------------------------------------------------------------------------------------------------------------------

        # ----------------ABOUT CONDITION---------------------
        if 'about' in user_input and ('you' or 'us') in user_input:
            out = 'Ok Let Me Introduce Myself.'
            self.printing_func(out)  # |
            self.speak(out)
            self.more()

# ----------------------------------------------------------------------------------------------------------------------
# --------------------------YOU CONDITIONS -----------------------------------------------------------------------------
        elif 'you' in user_input:  # |

            if 'who' in user_input and 'are' in user_input:
                r = random.randint(0, len(self.name) - 1)  # |
                out = self.name[r]  # |
                self.printing_func(out)  # |
                self.speak(out)

            elif 'how are' in user_input:  # |
                r = random.randint(0, len(self.how) - 1)  # |
                out = self.how[r]  # |
                self.printing_func(out)  # |
                self.speak(out)  # |

            elif 'who made' in user_input:  # |
                r = random.randint(0, len(self.creator) - 1)  # |
                out = self.creator[r]  # |
                self.printing_func(out)  # |
                self.speak(out)  # |

            elif 'do' in user_input:  # |
                r = random.randint(0, len(self.can) - 1)  # |
                out = self.can[r]  # |
                self.printing_func(out)  # |
                self.speak(out)  # |

            elif 'name' in user_input:  # |
                r = random.randint(0, len(self.name) - 1)  # |
                out = self.name[r]  # |
                self.printing_func(out)  # |
                self.speak(out)  # |

            elif 'open' in user_input:  # |
                out = 'Opening Youtube'  # |
                self.printing_func(out)  # |
                self.speak(out)  # |
                webbrowser.open('youtube.com')  # |

            elif 'here' in user_input:
                r = random.randint(0, len(self.here) - 1)  # |
                out = self.here[r]  # |
                self.printing_func(out)  # |
                self.speak(out)

            elif 'love' in user_input:
                out = 'i love only to help you'  # |
                self.printing_func(out)  # |
                self.speak(out)

            else:  # |
                r = random.randint(0, len(self.c_un) - 1)  # |
                out = self.c_un[r]  # |
                self.printing_func(out)  # |
                self.speak(out)  # |
# ----------------------------------------------------------------------------------------------------------------------
# -----------------------------my CONDITION-----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
        elif 'pravi' in user_input:
            out = 'pravi Is A Good Friend Of prajjval pramod and ujjwal.'  # |
            self.printing_func(out)  # |
            self.speak(out)
# ----------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------MY NAME CONDITION----------------------------------------------------
        elif 'who' in user_input and 'i' in user_input or 'my' in user_input and 'name' in user_input:
            r = random.randint(0, len(self.me) - 1)  # |
            out = self.me[r]  # |
            self.printing_func(out)  # |
            self.speak(out)
# ----------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------THANKS CONDITION-------------------------------------------------------
        elif 'thank' in user_input:
            r = random.randint(0, len(self.thanks) - 1)  # |
            out = self.thanks[r]  # |
            self.printing_func(out)  # |
            self.speak(out)
# ----------------------------------------------------------------------------------------------------------------------
# ----------------GOOD MORNING CONDITION--------------------------------------------------------------------------------
        elif 'good morning' in user_input:
            t = datetime.now().strftime('%H  hours and %M minutes')  # |
            o = t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt) + ':' + str(o[3] + ' PM')
            else:
                time = str(o[0]) + ':' + str(o[3] + ' AM')

            try:
                url = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=Ludhiana'
                json_data = requests.get(url).json()
                format_add = json_data['weather'][0]['main']
                format_temp = json_data['coord']['lat']
                outa = f'Temperture In Your City is {format_temp} Deegre   Celcius, And  Climate is  {format_add}'
            except '':
                outa = ' Weather Forcast Is Currently Unavailable'

            out = f'Good Morning sir, The Current Time is {time},  And {outa},    Have A Good Day Sir.'
            self.printing_func(out)
            self.speak(out)
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------USES------------------------------------------------------------------------------------------
        elif 'can' in user_input and 'friend' in user_input:
            r = random.randint(0, len(self.frd) - 1)  # |
            out = self.frd[r]  # |
            self.printing_func(out)  # |
            self.speak(out)
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------BORED-----------------------------------------------------------------------------------------
        elif 'bored' in user_input:
            out = 'Shall I Play Some Music Or A Game, What You Think?'
            self.printing_func(out)  # |
            self.speak(out)
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------WEATHER FORCAST---------------------------------------------------------------------------------
        elif 'weather' in user_input:
            try:
                if 'in' in user_input:
                    u = user_input.split()
                    for i in range(0, len(u)):
                        if u[i] == 'in':
                            city = u[i + 1]

                    api = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
                    url = api + city
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = json_data['coord']['lat']
                    out = f'Temperture In {city} is {format_temp} Deegre Celcius, And Climate is {format_add}'
                    self.printing_func(out)
                    self.speak(out)

                else:
                    url = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q' \
                          '=Ludhiana'
                    json_data = requests.get(url).json()
                    format_add = json_data['weather'][0]['main']
                    format_temp = json_data['coord']['lat']
                    out = f'Temperture In Your city is {format_temp} Deegre Celcius, And Climate is {format_add}'
                    self.printing_func(out)
                    self.speak(out)
            except '':
                out = 'I Was Unable To Connect To Internet.'
                self.printing_func(out)
                self.speak(out)
# ----------------------------------------------------------------------------------------------------------------------
# ---------------------------------------LOCATION-----------------------------------------------------------------------
        elif 'where' in user_input and 'i' in user_input or 'location' in user_input:
            try:
                r = requests.get('https://ipinfo.io/')
                d = r.text.split()[4]
                out = 'You Location Is Near To ' + d
                self.printing_func(out)
                self.speak(out)
            except '':
                out = 'I Was Unable To Track Your Location'
                self.printing_func(out)
                self.speak(out)
# ----------------------------------------------------------------------------------------------------------------------
# -------------------HELLO CONDITION------------------------------------------------------------------------------------
        elif 'hello' in user_input or 'hi' in user_input:  # |
            r = random.randint(0, len(self.greet) - 1)  # |
            out = self.greet[r]  # |
            self.printing_func(out)  # |
            self.speak(out)  # |
# ----------------------------------------------------------------------------------------------------------------------
# --------------------EXIT CONDITION------------------------------------------------------------------------------------
        elif 'exit' in user_input or 'quit' in user_input:   # |
            out = 'Okk I am going, Have a good Day sir'     # |
            self.printing_func(out)  # |
            self.speak(out)  # |
            self.win.destroy()
            # |
# ----------------------------------------------------------------------------------------------------------------------
# -------------------OPEN CONDITIONS -----------------------------------------------------------------------------------
        elif 'open' in user_input:
            if 'google' in user_input:
                out = 'Opening Google'
                self.printing_func(out)
                self.speak(out)
                webbrowser.open('google.com')

            elif 'youtube' in user_input:
                out = 'Opening Youtube'
                self.printing_func(out)
                self.speak(out)
                webbrowser.open('youtube.com')

            elif 'current' in user_input:
                out = 'Opening Current Working Directory'
                self.printing_func(out)
                self.speak(out)
                path = ''
                os.startfile(path)

            elif 'python' in user_input:
                out = 'Opening Python'
                self.printing_func(out)
                self.speak(out)
                path = r"C:\Users\Home\PycharmProjects"
                os.startfile(path)

            elif 'paint' in user_input:
                out = 'Opening Paint'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Windows\System32\mspaint.exe'
                os.startfile(path)

            elif 'wordpad' in user_input:
                out = 'Opening WordPad'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office'
                os.startfile(path)

            elif 'notepad' in user_input:
                out = 'Opening Note Pad'
                self.printing_func(out)
                os.chdir(r'E:\EXE_FILES\Text_editor')
                self.speak(out)
                path = r'E:\EXE_FILES\Text_editor\Text_editor.exe'
                os.startfile(path)

            elif 'game' in user_input:
                out = 'sorry you dont have any Games'
                self.printing_func(out)
                self.speak(out)
                # path = r'E:\snake2.py'
                # os.startfile(path)

            elif 'vlc' in user_input:
                out = 'Opening VLC'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\VideoLAN\VLC\vlc.exe'
                os.startfile(path)

            elif 'calculator' in user_input:
                out = 'sorry you dont have Calculator'
                self.printing_func(out)
                # os.chdir(r'E:\EXE_FILES\calculator')
                self.speak(out)
                # path = r'E:\EXE_FILES\CALCULATOR\CALCULATOR v2.0.exe'
                # os.startfile(path)

            elif 'browser' in user_input or 'chrome' in user_input:
                out = 'Opening Crome Browser'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Program Files\Google\Chrome\Application\chrome.exe'
                os.startfile(path)

            elif 'vsc' in user_input:
                out = 'Opening Visual Studio Code'
                self.printing_func(out)
                self.speak(out)
                path = r"C:\Users\Home\visual stdio code"
                os.startfile(path)

            elif 'picture' in user_input or 'images' in user_input or 'photo' in user_input:
                out = 'Opening  Images'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Users\Home\pictures'
                os.startfile(path)

            elif 'movie' in user_input:
                out = 'Opening  movie'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Users\Home\Desktop\MOV'
                os.startfile(path)

            elif 'presentation' in user_input:
                out = 'Opening presentation'
                self.printing_func(out)
                os.chdir(r'C:\Users\Home\Documents\python_project')
                self.speak(out)
                path = r'C:\Users\Home\Documents\python_project'
                os.startfile(path)

            elif 'cmd' or 'command prompt' in user_input:
                out = 'Opening Command Prompt'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Windows\System32\cmd.exe'
                os.startfile(path)

            elif 'screenshot' in user_input:
                out = 'Take ScreenShot'
                self.printing_func(out)
                self.speak(out)
                path = r'C:\Windows\system32\SnippingTool.exe'
                os.startfile(path)

            else:  # |
                r = random.randint(0, len(self.c_un) - 1)  # |
                out = self.c_un[r]  # |
                self.printing_func(out)  # |
                self.speak(out)  # |


# ----------------------------------------------------------------------------------------------------------------------
# -------------------GET LOST CONDITION---------------------------------------------------------------------------------
        elif 'get' in user_input and 'lost' in user_input:
            out = 'You Can\'t Talk To Me Like This \n I Am Going.'
            self.printing_func(out)
            self.speak(out)
            self.win.destroy()
#  ---------------------------------------------------------------------------------------------------------------------
#  -----------------------NONE CONDITION--------------------------------------------------------------------------------
        elif user_input == '':
            out = 'You Said Nothing'
            self.printing_func(out)
            self.speak(out)
# ----------------------------------------------------------------------------------------------------------------------
# ---------------------TIME CONDITION-----------------------------------------------------------------------------------
        elif 'time' in user_input:  # |
            t = datetime.now().strftime('%H  hours and %M minutes')  # |
            o = t.split()
            if int(o[0]) > 12:
                tt = int(o[0]) - 12
                time = str(tt) + ':' + str(o[3] + ' PM')
            else:
                time = str(o[0]) + ':' + str(o[3] + ' AM')
            out = 'Current time is : ' + time  # |
            self.printing_func(out)  # |
            self.speak(out)  # |
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------WIKIPEDIA CONDITION---------------------------------------------------------------------------
        elif 'wikipedia' in user_input:  # |
            i_l = list(user_input.split())  # |
            i_l.remove('wikipedia')  # |
            to2 = ''.join(i_l)  # |

            try:  # |
                out = 'According To Wikipedia ' + wikipedia.summary(to2, 2)  # |
                self.printing_func(out)  # |
                self.speak(out)  # |
            except '':  # |
                out = 'cannot find'  # |
                self.printing_func(out)  # |
                self.speak(out)  # |
# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------FINE COMMAND------------------------------------------------------------------------------
        elif 'fine' in user_input:
            out = 'oh Great'
            self.printing_func(out)  # |
            self.speak(out)

# ----------------------------------------------------------------------------------------------------------------------
# ----------------------------love you COMMAND--------------------------------------------------------------------------
#         elif 'love' in user_input:
#             out = 'oooooo i love you too'
#             self.printing_func(out)  # |
#             self.speak(out)


# ----------------------------------------------------------------------------------------------------------------------
# ---------------------SHUTDOWN COMMAND---------------------------------------------------------------------------------
        elif 'shutdown' in user_input:
            out = 'Shutting Down The System'  # |
            self.printing_func(out)  # |
            self.speak(out)
            os.system('shutdown -s')
# ----------------------------------------------------------------------------------------------------------------------
# ------------------------ELSE CONDITION--------------------------------------------------------------------------------
        else:  # |

            to_search = user_input
            out = 'I Can Search That On Google, May I SIR?'  # |
            self.printing_func(out)  # |
            self.speak(out)

            res = mb.askquestion('Google Search', 'May I Search That On Google.')

            if res == 'yes':
                out = 'Opening Google Search sir'
                self.printing_func(out)
                self.speak(out)
                webbrowser.open('https://www.google.co.in/search?q=' + to_search)
            else:
                out = 'Ok Sir!!'
                self.printing_func(out)
                self.speak(out)

# -------------------------------------CONSTRUCTER  FUNCTION------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self):
        self.win = Tk()
        self.win.geometry('380x340')
        self.win.resizable(0, 0)
        self.win.configure(bg='#000033')
        self.win.title('MY ASSISTANT - PRAVI')

        Label(self.win, text='A S S I S T A N T', font=('Oswald sans-serif', 20), fg='white', width=30, bg='black',
              bd=5).pack()

        Label(self.win, text='--YOU--', font=('arial black', 15), fg='green', bg='#000033').place(x=60, y=50)
        Label(self.win, text='--PRAVI--', font=('arial black', 15), fg='orange', bg='#000033').place(x=220, y=50)

        self.text_box1 = Text(self.win, font=('arial black', 13), width=16, height=5, fg='black', wrap=WORD)
        self.text_box1.place(x=10, y=100)

        self.text_box2 = Text(self.win, font=('arial black', 13), width=15, height=5, fg='black', wrap=WORD)
        self.text_box2.place(x=200, y=100)

        self.search_var = StringVar()

        Entry(self.win, font=('arial black', 14), width=18, textvariable=self.search_var, bd=5).place(x=10, y=250)

        send = Button(self.win, text='Send', font=('arial yellow', 10), bg='black', fg='white', bd=5, width=10,
                      command=self.send_func).place(x=270, y=250)

        def enter(*args):
            self.send_func()

        self.win.bind('<Return>', enter)

        self.win.mainloop()
# ----------------------------------------------------------------------------------------------------------------------


root = Widget()

# ----------------------------------------------------------------------------------------------------------------------
# ------------------------------CODE FINISH-----------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------
