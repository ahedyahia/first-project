import pyttsx3
yahia=pyttsx3.init()


loop=int(1)
while loop ==1:
 yahia.say('enter your first number')
 yahia.runAndWait()

 number1= int (input ("enter first number"))
 yahia.say('enter the operation')
 yahia.runAndWait()

 op= input ("/,*,-,+ ==>")
 yahia.say('enter your second number')
 yahia.runAndWait()
 number2= int (input ("enter second number"))
 

 if op =="+":
    yahia.say('the result is')
    yahia.runAndWait()
    yahia.say(number1+number2)
    yahia.runAndWait()
    print(number1+number2)
    
 elif op =="/":
    yahia.say('the result is')
    yahia.runAndWait()
    yahia.say(number1/number2)
    yahia.runAndWait()
    print(number1/number2)
 elif op =="*":
    yahia.say('the result is')
    yahia.runAndWait()
    yahia.say(number1*number2)
    yahia.runAndWait()
    print(number1*number2)
 elif op =="-":
    yahia.say('the result is')
    yahia.runAndWait()
    yahia.say(number1-number2)
    yahia.runAndWait()
    print(number1-number2)

