

import os
os.system('color 2f') 
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
print('-----WELCOME TO BOT------')
speak.speak('welcome to bot')
start = input()
speak.speak(start)
print('Hello!') 
speak.Speak('Hello!')
print('Whats your name?')
speak.Speak('Whats your name?')
Name = input() 
print('Im glad to meet you, ' + Name + '!!')
speak.Speak('Im glad to meet you, ' + Name + '!!')
talk = input()
print('How old are you?') 
speak.Speak('How old are you?')
Reply = input()
print('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.') 
speak.Speak('Okay, then you will be ' + str(int(Reply) + 1) + ' next year.')
print('Do You like me?')
speak.Speak('Do you like me?')
Reply = input() 
if Reply == 'yes' or Reply == 'yeah' or Reply == 'ofcourse' :
    print('yeah!!!!thank you') 
    speak.Speak('yeah!!!!thank you')
else:
    print("it's okay:)")
    speak.Speak("it's okay:)")

print('How was your day?') 
speak.Speak('How was your day?')
Reply = input() 
print('Ah ha! okay ' ) 
speak.Speak('Ah ha! okay ' )
print('By the way, are you enjoying this conversation?')
speak.Speak('By the way, are you enjoying this conversation?')
Reply = input() 
if Reply == 'yes' or Reply == 'yeah' or Reply == 'ofcourse' :
    print('yeah!!!!thank you'+ Name) 
    speak.Speak('yeah!!!!thank you'+ Name)
else:
    print('ohh i try to change myself')
    speak.Speak('ohh i try to change myself')

print('Do you want to continue our conversion?') 
speak.Speak('Do you want to continue our conversion?')
Reply = input() 
if Reply == 'yes' or Reply == 'yeah' or Reply == 'ofcourse' or Reply == 'i want to talk to you' :
    print('Nice!!!!!'+ Name + 'ask something')
    speak.Speak('Nice!!!!!'+ Name + 'ask something')
else:
    print('Okay see you' + Name) 
    speak.Speak('Okay see you'+ Name)
    

