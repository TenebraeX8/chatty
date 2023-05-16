import aiml
import sys

def std():
    k = aiml.Kernel()
    k.learn("std-startup.xml")
    k.respond("load aiml b")

    while True: 
        print(k.respond(input("> ")))

def tests(kernel):
    inputs = ["Hi","Bye Chatty","Hello I am Bob","Hi","How is the weather today","Can you tell me the weather","I like you","bye"]
    for inp in inputs:    
        print(f"> {inp}")
        print(kernel.respond(inp))

if __name__ == "__main__":
    kernel = aiml.Kernel()
    kernel.learn("bot.xml")
    if len(sys.argv) > 1 and sys.argv[1] == "-t":
        tests(kernel)
    else: 
        print("Bot is up!")
        inp = ""
        while True:
            inp = input("> ")
            if inp != "exit":            
                print(kernel.respond(inp))
            else:
                break


