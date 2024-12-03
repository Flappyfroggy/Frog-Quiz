from appJar import gui
app = gui("FROG","800x800")
app.setBg("PaleGreen")
app.setFont(size=25, family="times", underline=False, slant="roman")
app.addFlashLabel("titlepage","FROG FUN FACTS")
app.addLabel("background","MediumSpringGreen")
app.setLabelBg("background","MediumSpringGreen")
app.setLabelFg("background","MediumSpringGreen")
app.addLabel("undertitle","froggy!!!")
app.setLabelBg("titlepage","Cornsilk")
app.setLabelBg("undertitle","Cornsilk")
app.addLabel("background3","MediumSpringGreen")
app.setLabelBg("background3","MediumSpringGreen")
app.setLabelFg("background3","MediumSpringGreen")
app.startLabelFrame("frogge")
app.addImage("frogge", "frog-frog-love.gif")
app.stopLabelFrame()
def open_sub_window1(button):
      app.showSubWindow("sub_window")
app.addButton("Next", open_sub_window1)
app.setButtonImage("Next", "arrow_image.png")
app.startSubWindow("sub_window","Fact 1-3",)
app.setSize("1000x400")
app.setBg("PaleGreen")
app.addLabel("fact1","There is evidence that frogs have roamed the Earth\n for more than 200 million years, atleast as long as the dinosaurs")
app.setLabelBg("fact1","cornsilk")
app.addLabel("background5","MediumSpringGreen")
app.setLabelBg("background5","MediumSpringGreen")
app.setLabelFg("background5","MediumSpringGreen")
app.addLabel("fact2","The world's largest frog is the goliath frog of West Africa\n—it can grow to 15 inches and weigh up to 7 pounds")
app.setLabelBg("fact2","cornsilk")
app.addLabel("background6","MediumSpringGreen")
app.setLabelBg("background6","MediumSpringGreen")
app.setLabelFg("background6","MediumSpringGreen")
app.addLabel("fact3"," Glass frogs make their skin transparent\n by hiding red blood cells in their livers")
app.setLabelBg("fact3","cornsilk")
def open_sub_window2(button):
      app.showSubWindow("factpage")
app.addButton("next",open_sub_window2)
app.setButtonImage("next","arrow_image.png")
app.startSubWindow("factpage","Fact 4-6")
app.setBg("PaleGreen")
app.setSize("1000x400")
app.addLabel("fact4","One gram of the toxin produced by the skin of the golden\n poison dart frog could kill 100,000 people.")
app.setLabelBg("fact4","cornsilk")
app.addLabel("background7","MediumSpringGreen")
app.setLabelBg("background7","MediumSpringGreen")
app.setLabelFg("background7","MediumSpringGreen")
app.addLabel("fact5"," When a frog swallows its prey, it blinks, which pushes its eyeballs \ndown on top of the mouth to help push the food down its throat.")
app.setLabelBg("fact5","cornsilk")
app.addLabel("background8","MediumSpringGreen")
app.setLabelBg("background8","MediumSpringGreen")
app.setLabelFg("background8","MediumSpringGreen")
app.addLabel("fact6","A group of frogs is called an army")
app.setLabelBg("fact6","cornsilk")
def open_sub_window3(button):
      app.showSubWindow("NextFactpage")
app.addButton("next2",open_sub_window3)
app.setButtonImage("next2","arrow_image.png")
app.startSubWindow("NextFactpage","Fact 7-9")
app.setBg("PaleGreen")
app.setSize("1000x400")
app.addLabel("fact7"," There are over 7,500 species of frogs on \n(almost) every continent on Earth")
app.setLabelBg("fact7","cornsilk")
app.addLabel("background9","MediumSpringGreen")
app.setLabelBg("background9","MediumSpringGreen")
app.setLabelFg("background9","MediumSpringGreen")
app.addLabel("fact8","Some frog species can spend weeks,\n if not months, underwater")
app.setLabelBg("fact8","cornsilk")
app.addLabel("background10","MediumSpringGreen")
app.setLabelBg("background10","MediumSpringGreen")
app.setLabelFg("background10","MediumSpringGreen")
app.addLabel("fact9","frogs absorb water rather than drink it")
app.setLabelBg("fact9","cornsilk")
def open_sub_window4(button):
      app.showSubWindow("startquizpage")
app.addButton("toquizpage",open_sub_window4)
app.setButtonImage("toquizpage","arrow_image.png")
app.startSubWindow("startquizpage","start da quiz now or else")
app.setBg("PaleGreen")
app.setSize("1000x400")
app.addLabel("quiz","take this quiz now or else")
app.setLabelBg("quiz","cornsilk")
app.addLabel("background11","MediumSpringGreen")
app.setLabelBg("background11","MediumSpringGreen")
app.setLabelFg("background11","MediumSpringGreen")
app.addLabel("press the button","click the button already")
app.setLabelBg("press the button","cornsilk")
def open_sub_window5(button):
      app.showSubWindow("quizquestion")
app.addButton("tothequizquestion",open_sub_window5)
app.setButtonImage("tothequizquestion","arrow_image.png")
app.startSubWindow("quizquestion","first few questions")
app.setBg("PaleGreen")
app.setSize("1000x2000")
#possible corrects
def show_correct(button):
      app.addLabel("correct","that's correct!!!!!!!") #used
def correctee(button):
      app.addLabel("correctee","finaaaaaaaaallllllyyyyy you got it correct") #used
def correct2(button): 
      app.addLabel("yas") #used
def correct3(button): 
      app.addLabel("yeah that's correct") #used
def correct4(button):
      app.addLabel("wow u aren't stupid") #used
def correct5(button):
      app.addLabel("yes") #used
def correct6(button):
      app.addLabel("wow u so smart") #used
def correct7(button):
      app.addLabel("yaaaahh") #used
def correct8(button):
      app.addLabel("good job you have brain cells")
#possuble wrongs
def wrong(button): 
      app.addLabel("wrong","wrong...try again") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong1(button):
      app.addLabel("wrong1","maybe it's a different one?") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong2(button):
      app.addLabel("wrong2","no") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong3(button):
      app.addLabel("wrong3","not this one") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong4(button):
      app.addLabel("wrong4","consider trying") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong5(button):
      app.addLabel("wrong5","have you considered getting it correct") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong6(button):
      app.addLabel("why are you here")
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong7(button):
      app.addLabel("head not ok?") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong8(button):
      app.addLabel("nope") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong9(button):
      app.addLabel("nah") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong10(button):
      app.addLabel("noor")#used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong11(button):
      app.addLabel("That is wrong. Please try again") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong12(button):
      app.addLabel("WRONG") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong13(button):
      app.addLabel("do you live under a rock") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong14(button):
      app.addLabel("do you have braincells")
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong15(button):
      app.addLabel("are you an orange cat in disguise") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong16(button): 
      app.addLabel("are u ok in the head rn tho") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")
def wrong17(button):
      app.addLabel("nae") #used
      app.setFont(size=10, family="times", underline=False, slant="roman")


app.addLabel("question1","How long have frogs roamed earth?")
app.addButton("150 million years!",wrong)
app.addButton("200 million years!",show_correct)   
app.addButton("100 million years!",wrong1)
app.addLabel("question2","What is the world's largest frog?")
app.addButton("The Golath frog",wrong2)
app.addButton("The Golias frog",wrong3)
app.addButton("The Goliath frog",correctee)
app.addLabel("question3","How do Glass Frogs hide?")
app.addButton("They can turn to glass",wrong4)
app.addButton("They have a clear body and\n only need to hide their heads",wrong5)
app.addButton("They hide their red blood cells",correct2)
app.addLabel("question4","how many people can 1 gram of toxin from the golden poison dart frog kill?")
app.addButton("not a lot",wrong12)
app.addButton("10,000 sadistic people",wrong11)
app.addButton("100,000 people",correct7)
app.addLabel("question5","what does a frog do when it swallows it's prey?")
app.addButton("it's eyeballs roll",wrong10)
app.addButton("It blinks",correct6)
app.addButton("The frog's throat will bob",wrong7)
app.addLabel("question6","What is a group of frog's called?")
app.addButton("An army",correct3)
app.addButton("A nestling",wrong9)
app.addButton("An armada",wrong15)
app.addLabel("question7","approximately how many frog species are there in the world?")
app.addButton("5,000 species",wrong8)
app.addButton("7,500 species",correct4)
app.addButton("10,000 species",wrong13)
app.addLabel("question8","what is the longest time frogs can spend underwater?")
app.addButton("3 full days",wrong16)
app.addButton("months",correct5) 
app.addButton("a fortnight",wrong17)
app.addLabel("question9","how do frogs drink water?")
app.addButton("They drink it by putting their mouths to the water",wrong6)
app.addButton("They dunk their heads into the water",wrong14)
app.addButton("They absorb it",correct8)
app.go()