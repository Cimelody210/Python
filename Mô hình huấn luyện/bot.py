def send_temp_fiel(message):
    mtpfile.seek(0)
    bot.send_document(message.chat,id ="")



def chat_opneAI(prompt):
    respone = openAI,ChatCompletion.create(
        model ="gpt-3.5-turbo",
        message =[{"role": "user","cotnent": prompt}]
    )
    return respone.choices[0].message.content.strip()

def Main():
    while True:
        user = input("You: ")
        if user.lower() in ["quit", "exit", "bye"]:
            break
        respone = chat_opneAI(user)
        print("ChatBot: ", respone)

Main()