# ======= IMPORT REQUIREMENTS ====== #
import tkinter
from tkinter import *
import ctypes
import random
import tkinter as tk

# ========= COLOR VARIABLES ========= #
background_color = "#2B2D42"
button_color = "#8D99AE"
text_color = "#EDF2F4"
header_color = "#EF233C"
aux_color_2 = "#D90429"


# ========= CLASS DEFINITION ========= #
class Typing(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        # ========== WINDOW =========== #
        self.title("Typing Speed Test")
        self.geometry("700x700")
        self.config(background=background_color)
        ctypes.windll.shcore.SetProcessDpiAwareness(1)

        # ========= VARIABLES ========= #
        self.easy_sentences = [
            "In a small village nestled between rolling hills and lush forests, there lived a kind-hearted baker named Eliza who was known for her delicious pastries and warm smile. Every morning, the scent of freshly baked bread wafted through the air, drawing villagers from far and wide to her cozy little shop. Eliza loved to experiment with new recipes, often incorporating seasonal fruits and locally sourced ingredients to create unique and mouthwatering treats. Her bakery was not just a place to buy bread, but a gathering spot for friends and neighbors to share stories and laughter over a cup of tea.",
            "One day, while walking through the bustling marketplace, young Samuel stumbled upon a mysterious old book tucked away in a dusty corner of an antique shop. Intrigued by its worn leather cover and intricate gold lettering, he decided to buy it and take it home. As he flipped through the pages, he discovered it was filled with fascinating tales of adventure, magic, and ancient legends. Little did Samuel know that this book would soon become his gateway to a world beyond his wildest dreams, leading him on a journey that would change his life forever.",
            "At the edge of the city, where the river meets the sea, stood an old lighthouse that had guided ships safely to shore for generations. Its weathered stones and tall, imposing structure were a testament to its resilience against the harsh elements. The lighthouse keeper, a solitary figure named Mr. Thompson, had dedicated his life to ensuring the light never dimmed, tirelessly maintaining the beacon that shone bright each night. Despite his lonely existence, Mr. Thompson found solace in the rhythmic sound of the waves crashing against the rocks and the beauty of the endless horizon.",
            "In the heart of the bustling city, amidst the noise and chaos, there was a hidden oasis of tranquility known as the Garden of Serenity. This lush, green sanctuary was filled with vibrant flowers, towering trees, and winding pathways that offered a peaceful escape from the hustle and bustle. Visitors to the garden often found themselves lost in thought, wandering through its serene landscape and finding a moment of respite from their busy lives. The garden was not just a place of natural beauty, but a symbol of hope and renewal for all who sought its calming embrace."
        ]
        self.hard_sentences = [
            "In the labyrinthine corridors of academia, where the pursuit of knowledge is both a solitary and communal endeavor, Dr. Penelope Abernathy found herself increasingly preoccupied with the esoteric intricacies of quantum mechanics, a field that not only defied the conventional boundaries of classical physics but also challenged the very fabric of human comprehension. Her research, often conducted in the dead of night under the soft glow of computer screens and surrounded by towering stacks of reference materials, delved into the probabilistic nature of subatomic particles, the paradoxes of entanglement, and the theoretical frameworks that sought to unify these phenomena with the macroscopic world. As she navigated through this intellectual maze, her thoughts frequently wandered to the philosophical implications of her work, pondering the intersection of science and metaphysics, and the profound questions about existence and reality that lay at the heart of her scholarly pursuit.",
            "Amid the bustling metropolis, where the cacophony of urban life melded with the relentless hum of technological advancement, stood the architectural marvel known as the Pinnacle Tower, a testament to human ingenuity and ambition. This towering edifice, with its sleek glass façade and intricate lattice of steel beams, housed a multitude of enterprises ranging from cutting-edge biotech firms to avant-garde design studios. Within its confines, the convergence of diverse disciplines fostered a dynamic environment of innovation and creativity, where interdisciplinary collaborations were not merely encouraged but deemed essential for progress. The tower’s atrium, an expansive space adorned with contemporary art installations and verdant indoor gardens, served as a communal nexus for intellectual exchange, spontaneous brainstorming sessions, and serendipitous encounters that often sparked groundbreaking ideas.",
            "In the annals of history, few events have captured the collective imagination and scholarly scrutiny as the enigmatic disappearance of the ancient city of Atlantis, a tale that has been perpetuated through the ages by a confluence of myth, legend, and speculative inquiry. According to Platonic dialogues, this fabled civilization, endowed with unparalleled technological prowess and utopian societal structures, met its demise through a cataclysmic event that consigned it to the depths of the ocean. Modern archaeological expeditions, driven by the relentless quest to unearth tangible evidence of Atlantis' existence, have scoured the seabed and analyzed geological anomalies, yet the elusive nature of their findings has only fueled further debate and conjecture. As researchers continue to grapple with the veracity of this ancient narrative, the story of Atlantis endures as a symbol of human curiosity, the limits of empirical knowledge, and the enduring allure of the unknown.",
            "Navigating the intricate web of global economic dynamics requires a nuanced understanding of not only the fundamental principles of supply and demand but also the myriad externalities and geopolitical factors that influence market behavior. In the realm of international trade, the interplay between protectionist policies, currency fluctuations, and bilateral agreements creates a complex tapestry that policymakers must adeptly manage to foster economic stability and growth. Moreover, the advent of digital currencies and blockchain technology has introduced novel paradigms that challenge traditional financial systems, necessitating a reevaluation of regulatory frameworks and fiscal strategies. As economists and legislators endeavor to adapt to these transformative changes, the imperative for a holistic approach that encompasses both macroeconomic indicators and microeconomic realities becomes increasingly apparent, highlighting the intricate balance required to navigate the contemporary economic landscape."
        ]
        self.text = None
        self.split_point = 0
        self.write_able = False
        self.time_elapsed = 0
        self.result_label = None
        self.restart_button = None
        self.max_score = None

        # ======== INTRO PAGE =========== #
        self.header = tk.Frame(self, bg=header_color)
        self.header.place(relx=0, rely=0, relwidth=1, relheight=0.1)
        self.start_page()

    def start_page(self):
        self.intro_title = Label(self.header,
                                 text="TYPING SPEED TEST APPLICATION",
                                 font=("Arial", 20, "bold"),
                                 fg=text_color,
                                 bg=header_color)
        self.intro_title.place(relx=0.16, rely=0.3)

        self.choose_difficulty = Label(text="Choose Difficulty",
                                       font=("Arial", 20, "bold"),
                                       fg=text_color,
                                       bg=background_color)
        self.choose_difficulty.place(x=225, y=130)

        self.easy = Button(text="EASY",
                           bg=button_color,
                           fg="green",
                           activebackground=text_color,
                           width=10,
                           height=2,
                           font=("Arial", 20, "bold"),
                           command=lambda: self.start_game(difficulty="EASY"))
        self.easy.place(x=80, y=200)

        self.hard = Button(text="HARD",
                           bg=button_color,
                           fg="red",
                           activeforeground="red",
                           activebackground=text_color,
                           width=10,
                           height=2,
                           font=("Arial", 20, "bold"),
                           command=lambda: self.start_game(difficulty="HARD"))
        self.hard.place(x=420, y=200)

        self.instructions_title = Label(text="Instructions",
                                        font=("Arial", 20, "bold"),
                                        fg=text_color,
                                        bg=background_color)
        self.instructions_title.place(x=260, y=350)

        self.inst_label_1 = Label(text="1.- Choose a difficulty level. Word complexity is higher for HARD mode.",
                                  bg=background_color,
                                  fg=text_color,
                                  font=("Arial", 14))
        self.inst_label_1.place(x=30, y=420)
        self.inst_label_2 = Label(text="2.- The timer will start IMMEDIATELY. Start typing the indicated word.",
                                  bg=background_color,
                                  fg=text_color,
                                  font=("Arial", 14))
        self.inst_label_2.place(x=30, y=460)
        self.inst_label_3 = Label(text="3.- After 60 seconds, scores are automatically saved and displayed in WPM.",
                                  bg=background_color,
                                  fg=text_color,
                                  font=("Arial", 14))
        self.inst_label_3.place(x=30, y=500)

        self.shameless_plug = Label(text="Visit https://oscarbejas.com to check my projects!",
                                    font=("Arial", 20, "bold"),
                                    fg=aux_color_2,
                                    bg=background_color)
        self.shameless_plug.place(x=20, y=620)

        # ========= TEXT LABELS ========= #
        # self.text_area = Label()
        #
        self.mainloop()

    def start_game(self, difficulty):
        self.choose_difficulty.destroy()
        self.easy.destroy()
        self.hard.destroy()
        self.instructions_title.destroy()
        self.inst_label_1.destroy()
        self.inst_label_2.destroy()
        self.inst_label_3.destroy()

        self.time_elapsed = 0
        self.write_able = True

        if difficulty == "EASY":
            self.text = random.choice(self.easy_sentences)
        else:
            self.text = random.choice(self.hard_sentences)

        # ========= CALLBACKS AND BIND =========== #
        self.after(10000, self.stop_test)
        self.after(1000, self.add_second)
        self.bind("<Key>", self.keypress)

        self.left_label = Label(text=self.text[0:self.split_point], fg=text_color, bg=background_color,
                                font=("Arial", 30))
        self.left_label.place(relx=0.5, rely=0.5, anchor=E)

        self.right_label = Label(text=self.text[self.split_point:], fg=text_color, bg=background_color,
                                 font=("Arial", 30))
        self.right_label.place(relx=0.5, rely=0.5, anchor=W)

        self.current_letter = Label(text=self.text[self.split_point], fg=aux_color_2, bg=background_color,
                                    font=("Arial", 35))
        self.current_letter.place(relx=0.5, rely=0.6, anchor=N)

        self.time_left = Label(text=f"0 Seconds", fg=text_color, bg=background_color, font=("Arial", 40))
        self.time_left.place(relx=0.5, rely=0.4, anchor=S)

    def stop_test(self):
        self.write_able = False

        # Calculating the amount of words
        word_count = len(self.left_label.cget('text').split(' '))

        # Destroy all unwanted widgets.
        self.time_left.destroy()
        self.current_letter.destroy()
        self.right_label.destroy()
        self.left_label.destroy()

        with open("max_score.txt", mode="r") as file:
            contents = file.read()
            if word_count < int(contents):
                self.max_score = int(contents)
            else:
                self.max_score = word_count
                with open("max_score.txt", mode="w") as file2:
                    file2.write(f"{word_count}")

        # Display the test results with a formatted string
        self.result_label = Label(text=f'Words per Minute: {word_count}', fg=text_color, bg=background_color,
                                  font=("Arial", 40))
        self.result_label.place(relx=0.5, rely=0.3, anchor=CENTER)

        self.max_score = Label(text=f"Current Record: {self.max_score}", fg=text_color, bg=background_color,
                               font=("Arial", 40))
        self.max_score.place(relx=0.5, rely=0.5, anchor=CENTER)

        # Display a button to restart the game
        self.restart_button = Button(text=f'Retry', fg=text_color, bg=background_color, command=self.restart,
                                     font=("Arial", 20))
        self.restart_button.place(relx=0.5, rely=0.7, anchor=CENTER)

    def restart(self):
        self.restart_button.destroy()
        self.result_label.destroy()
        self.max_score.destroy()

        # re-setup writing labels.
        self.start_page()

    def add_second(self):
        self.time_elapsed += 1
        self.time_left.configure(text=f'{self.time_elapsed} Seconds')

        # call this function again after one second if the time is not over.
        if self.write_able:
            self.after(1000, self.add_second)

    def keypress(self, event=None):
        try:
            if event.char.lower() == self.right_label.cget("text")[0].lower():
                self.right_label.configure(text=self.right_label.cget("text")[1:])
                self.left_label.configure(text=self.left_label.cget("text") + event.char.lower())
                self.current_letter.configure(text=self.right_label.cget("text")[0])
        except tkinter.TclError:
            pass
