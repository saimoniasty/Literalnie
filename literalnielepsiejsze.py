import random
import tkinter as tk
from tkinter import messagebox
from tkinter import font as tkfont
chosen_word_atleastOnce=list()
column_number=0
row_number=0
column_numberDel=0
chosen_word=""
enter=0
good_word=0
#Zrobiłem w klasie bo w sumie nw chciałem zobaczyć czy umiem w klasach czy coś
class Literalnie:
    def __init__(self):
        self.words=["POLKI","KOTKI","KOTEK","CHATA","JUTRO","DAWAJ","RATUJ","MATKA","STARY",
               "POTEM","AWANS","LOTKI","KATAR","KANAR","BLUZA","KAJAK","PILOT","POTOP","KARTY"]
        self.drawnWord=random.choice(self.words)
        print(self.drawnWord)
        self.root=tk.Tk()
        self.root.geometry("600x650")
        self.root.title("Literaki")
        self.root.configure(bg="#36454F")

        self.fontHighlighter=tkfont.Font(family="Arial",size=25,weight="bold")
        self.welcome=tk.Label(self.root,text="LITERAKI",font=self.fontHighlighter,bg="#36454F",fg="white")
        self.welcome.pack(padx=10,pady=10)
        #frames for letters
        self.letterFrames=tk.Frame(self.root,bg="#36454F")
        for i in range(5):
            self.letterFrames.columnconfigure(i,weight=0)
        

        #row1
        for i in range(5):
            self.frame1_Border=tk.Frame(self.letterFrames,height=60,width=45,bg="gray")
            self.frame1_Border.grid(row=0,column=i,padx=15,pady=8)
        for i in range(5):
            self.frame1=tk.Frame(self.letterFrames,height=40,width=27,bg="lightgray")
            self.frame1.grid(row=0,column=i)
        
        #row2
        for i in range(5):
            self.frame2_Border=tk.Frame(self.letterFrames,height=60,width=45,bg="gray")
            self.frame2_Border.grid(row=1,column=i,padx=15,pady=8)
        for i in range(5):
            self.frame2=tk.Frame(self.letterFrames,height=40,width=27,bg="lightgray")
            self.frame2.grid(row=1,column=i)
        
        #row3
        for i in range(5):
            self.frame3_Border=tk.Frame(self.letterFrames,height=60,width=45,bg="gray")
            self.frame3_Border.grid(row=2,column=i,padx=15,pady=8)
        for i in range(5):
            self.frame3=tk.Frame(self.letterFrames,height=40,width=27,bg="lightgray")
            self.frame3.grid(row=2,column=i)
        
        #row4
        for i in range(5):
            self.frame4_Border=tk.Frame(self.letterFrames,height=60,width=45,bg="gray")
            self.frame4_Border.grid(row=3,column=i,padx=15,pady=8)
        for i in range(5):
            self.frame4=tk.Frame(self.letterFrames,height=40,width=27,bg="lightgray")
            self.frame4.grid(row=3,column=i)
        
        #row5
        for i in range(5):
            self.frame5_Border=tk.Frame(self.letterFrames,height=60,width=45,bg="gray")
            self.frame5_Border.grid(row=4,column=i,padx=15,pady=8)
        for i in range(5):
            self.frame5=tk.Frame(self.letterFrames,height=40,width=27,bg="lightgray")
            self.frame5.grid(row=4,column=i)

        #row6
        for i in range(5):
            self.frame6_Border=tk.Frame(self.letterFrames,height=60,width=45,bg="gray")
            self.frame6_Border.grid(row=5,column=i,padx=15,pady=8)
        for i in range(5):
            self.frame6=tk.Frame(self.letterFrames,height=40,width=27,bg="lightgray")
            self.frame6.grid(row=5,column=i)

        self.letterFrames.pack()

        #letter buttons
        self.letterButtons_1row=tk.Frame(self.root,bg="#36454F")
        for i in range(9):
            self.letterButtons_1row.columnconfigure(i,weight=1)

        self.letterButtons_2row=tk.Frame(self.root,bg="#36454F")
        for i in range(10):
            self.letterButtons_2row.columnconfigure(i,weight=1)

        self.letterButtons_34row=tk.Frame(self.root,bg="#36454F")
        for i in range(9):
            self.letterButtons_34row.columnconfigure(i,weight=1)

        #row1 buttons
        self.buttonLetter_Ą=tk.Button(self.letterButtons_1row,text="Ą",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Ą"))
        self.buttonLetter_Ą.grid(row=6,column=0,sticky=tk.W+tk.E)
        self.buttonLetter_Ć=tk.Button(self.letterButtons_1row,text="Ć",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Ć"))
        self.buttonLetter_Ć.grid(row=6,column=1,sticky=tk.W+tk.E)
        self.buttonLetter_Ę=tk.Button(self.letterButtons_1row,text="Ę",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Ę"))
        self.buttonLetter_Ę.grid(row=6,column=2,sticky=tk.W+tk.E)
        self.buttonLetter_Ł=tk.Button(self.letterButtons_1row,text="Ł",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Ł"))
        self.buttonLetter_Ł.grid(row=6,column=3,sticky=tk.W+tk.E)
        self.buttonLetter_Ó=tk.Button(self.letterButtons_1row,text="Ó",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Ó"))
        self.buttonLetter_Ó.grid(row=6,column=4,sticky=tk.W+tk.E)
        self.buttonLetter_Ś=tk.Button(self.letterButtons_1row,text="Ś",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Ś"))
        self.buttonLetter_Ś.grid(row=6,column=5,sticky=tk.W+tk.E)
        self.buttonLetter_Ń=tk.Button(self.letterButtons_1row,text="Ń",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Ń"))
        self.buttonLetter_Ń.grid(row=6,column=6,sticky=tk.W+tk.E)
        self.buttonLetter_Ż=tk.Button(self.letterButtons_1row,text="Ż",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Ż"))
        self.buttonLetter_Ż.grid(row=6,column=7,sticky=tk.W+tk.E)
        self.buttonLetter_Ź=tk.Button(self.letterButtons_1row,text="Ź",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Ź"))
        self.buttonLetter_Ź.grid(row=6,column=8,sticky=tk.W+tk.E)

        self.letterButtons_1row.pack(fill="x")

        #row2 buttons
        self.buttonLetter_Q=tk.Button(self.letterButtons_2row,text="Q",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Q"))
        self.buttonLetter_Q.grid(row=7,column=0,sticky=tk.W+tk.E)
        self.buttonLetter_W=tk.Button(self.letterButtons_2row,text="W",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("W"))
        self.buttonLetter_W.grid(row=7,column=1,sticky=tk.W+tk.E)
        self.buttonLetter_E=tk.Button(self.letterButtons_2row,text="E",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("E"))
        self.buttonLetter_E.grid(row=7,column=2,sticky=tk.W+tk.E)
        self.buttonLetter_R=tk.Button(self.letterButtons_2row,text="R",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("R"))
        self.buttonLetter_R.grid(row=7,column=3,sticky=tk.W+tk.E)
        self.buttonLetter_T=tk.Button(self.letterButtons_2row,text="T",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("T"))
        self.buttonLetter_T.grid(row=7,column=4,sticky=tk.W+tk.E)
        self.buttonLetter_Y=tk.Button(self.letterButtons_2row,text="Y",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Y"))
        self.buttonLetter_Y.grid(row=7,column=5,sticky=tk.W+tk.E)
        self.buttonLetter_U=tk.Button(self.letterButtons_2row,text="U",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("U"))
        self.buttonLetter_U.grid(row=7,column=6,sticky=tk.W+tk.E)
        self.buttonLetter_I=tk.Button(self.letterButtons_2row,text="I",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("I"))
        self.buttonLetter_I.grid(row=7,column=7,sticky=tk.W+tk.E)
        self.buttonLetter_O=tk.Button(self.letterButtons_2row,text="O",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("O"))
        self.buttonLetter_O.grid(row=7,column=8,sticky=tk.W+tk.E)
        self.buttonLetter_P=tk.Button(self.letterButtons_2row,text="P",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("P"))
        self.buttonLetter_P.grid(row=7,column=9,sticky=tk.W+tk.E)

        self.letterButtons_2row.pack(fill="x")

        #row3 buttons
        self.buttonLetter_A=tk.Button(self.letterButtons_34row,text="A",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("A"))
        self.buttonLetter_A.grid(row=8,column=0,sticky=tk.W+tk.E)
        self.buttonLetter_S=tk.Button(self.letterButtons_34row,text="S",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("S"))
        self.buttonLetter_S.grid(row=8,column=1,sticky=tk.W+tk.E)
        self.buttonLetter_D=tk.Button(self.letterButtons_34row,text="D",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("D"))
        self.buttonLetter_D.grid(row=8,column=2,sticky=tk.W+tk.E)
        self.buttonLetter_F=tk.Button(self.letterButtons_34row,text="F",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("F"))
        self.buttonLetter_F.grid(row=8,column=3,sticky=tk.W+tk.E)
        self.buttonLetter_G=tk.Button(self.letterButtons_34row,text="G",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("G"))
        self.buttonLetter_G.grid(row=8,column=4,sticky=tk.W+tk.E)
        self.buttonLetter_H=tk.Button(self.letterButtons_34row,text="H",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("H"))
        self.buttonLetter_H.grid(row=8,column=5,sticky=tk.W+tk.E)
        self.buttonLetter_J=tk.Button(self.letterButtons_34row,text="J",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("J"))
        self.buttonLetter_J.grid(row=8,column=6,sticky=tk.W+tk.E)
        self.buttonLetter_K=tk.Button(self.letterButtons_34row,text="K",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("K"))
        self.buttonLetter_K.grid(row=8,column=7,sticky=tk.W+tk.E)
        self.buttonLetter_L=tk.Button(self.letterButtons_34row,text="L",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("L"))
        self.buttonLetter_L.grid(row=8,column=8,sticky=tk.W+tk.E)

        #row4 buttons
        self.buttonLetter_Enter=tk.Button(self.letterButtons_34row,text="ENTER",width=4,font=("Arial",12),bg="gray",command=lambda: self.enterWord())
        self.buttonLetter_Enter.grid(row=9,column=0,sticky=tk.W+tk.E)
        self.buttonLetter_Z=tk.Button(self.letterButtons_34row,text="Z",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("Z"))
        self.buttonLetter_Z.grid(row=9,column=1,sticky=tk.W+tk.E)
        self.buttonLetter_X=tk.Button(self.letterButtons_34row,text="X",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("X"))
        self.buttonLetter_X.grid(row=9,column=2,sticky=tk.W+tk.E)
        self.buttonLetter_C=tk.Button(self.letterButtons_34row,text="C",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("C"))
        self.buttonLetter_C.grid(row=9,column=3,sticky=tk.W+tk.E)
        self.buttonLetter_V=tk.Button(self.letterButtons_34row,text="V",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("V"))
        self.buttonLetter_V.grid(row=9,column=4,sticky=tk.W+tk.E)
        self.buttonLetter_B=tk.Button(self.letterButtons_34row,text="B",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("B"))
        self.buttonLetter_B.grid(row=9,column=5,sticky=tk.W+tk.E)
        self.buttonLetter_N=tk.Button(self.letterButtons_34row,text="N",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("N"))
        self.buttonLetter_N.grid(row=9,column=6,sticky=tk.W+tk.E)
        self.buttonLetter_M=tk.Button(self.letterButtons_34row,text="M",font=("Arial",12),bg="gray",command=lambda: self.buttonClicking1("M"))
        self.buttonLetter_M.grid(row=9,column=7,sticky=tk.W+tk.E)
        self.buttonLetter_Del=tk.Button(self.letterButtons_34row,text="DEL",width=2,font=("Arial",12),bg="gray",command=lambda: self.delete())
        self.buttonLetter_Del.grid(row=9,column=8,sticky=tk.W+tk.E)

        self.letterButtons_34row.pack(fill="x")

        self.root.mainloop()
    def delete(self):
        global column_numberDel,column_number,row_number,chosen_word,enter
        self.deleteFrame=tk.Frame(self.letterFrames,height=40,width=27,bg="lightgray")

        delete_letter=lambda row_num,column_num: self.deleteFrame.grid(row=row_num,column=column_num)
        if column_number==1:
            delete_letter(row_number,column_numberDel)
            column_number=0
            chosen_word=chosen_word[:-1]
        elif column_number==2:
            column_numberDel=1
            delete_letter(row_number,column_numberDel)
            column_numberDel=0
            column_number=1
            chosen_word=chosen_word[:-1]
        elif column_number==3:
            column_numberDel=2
            delete_letter(row_number,column_numberDel)
            column_numberDel=1
            column_number=2
            chosen_word=chosen_word[:-1]
        elif column_number==4:
            column_numberDel=3
            delete_letter(row_number,column_numberDel)
            column_numberDel=2
            column_number=3
            chosen_word=chosen_word[:-1]
        elif column_number==5:
            column_numberDel=4
            delete_letter(row_number,column_numberDel)
            column_numberDel=3
            column_number=4
            enter=0
            chosen_word=chosen_word[:-1]

    def buttonClicking1(self,letter):
        global column_number,row_number,chosen_word,enter,good_word
        chosen_letter=tk.Label(self.letterFrames,text=f"{letter}",font=("Arial",16),bg="lightgray")
        letter_print=lambda row_num,column_num: chosen_letter.grid(row=row_num,column=column_num)
        if good_word<5:
            if row_number<6:
                if column_number==5:
                    enter=1
                if enter==0:
                    letter_print(row_number,column_number)
                    column_number+=1
                    chosen_word=f"{chosen_word}{letter}" 
    def enterWord(self):
        global enter,chosen_word,row_number,column_number,chosen_word_atleastOnce,good_word
        if good_word<5:
            if row_number==5:
                self.root.quit()
                messagebox.showinfo("Loser message", "YOU LOSE AT LITERAKI 2.0")
            if column_number==5:
                column_number=0
                enter=0
                for i in range(5):
                    chosen_word_atleastOnce=list(filter(lambda drawn_word:drawn_word==chosen_word[i],self.drawnWord))
                    if chosen_word[i]==self.drawnWord[i]:
                        good_letter=tk.Frame(self.letterFrames,height=40,width=27,bg="#80FF00")
                        good_letter.grid(row=row_number,column=i)
                        letter=tk.Label(self.letterFrames,text=f"{chosen_word[i]}",font=("Arial",16),bg="#80FF00")
                        letter.grid(row=row_number,column=i)
                        good_word+=1
                    if chosen_word[i]!=self.drawnWord[i]:
                        try:
                            if chosen_word_atleastOnce[0]==chosen_word_atleastOnce[0]:
                                good_letter_badPlace=tk.Frame(self.letterFrames,height=40,width=27,bg="yellow")
                                good_letter_badPlace.grid(row=row_number,column=i)
                                letter_goodbad=tk.Label(self.letterFrames,text=f"{chosen_word[i]}",font=("Arial",16),bg="yellow")
                                letter_goodbad.grid(row=row_number,column=i)
                        except IndexError:
                            bad_letter=tk.Frame(self.letterFrames,height=40,width=27,bg="gray")
                            bad_letter.grid(row=row_number,column=i)
                            letter_bad=tk.Label(self.letterFrames,text=f"{chosen_word[i]}",font=("Arial",16),bg="gray")
                            letter_bad.grid(row=row_number,column=i)
                row_number+=1
                chosen_word=""
        if good_word==5:
            self.root.quit()
            messagebox.showinfo("Winner message", "YOU WON LITERAKI 2.0")
Literalnie()