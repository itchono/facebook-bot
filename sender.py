import fbchat

import os
import dotenv

def cipher(s):
    '''
    Simple bidirectional cipher which can decode or encode messages
    '''
    return " ".join([item[-1::-1] for item in s.split()])


dotenv.load_dotenv()
sender = fbchat.Client(os.environ.get('EMAIL'), os.environ.get('PASSWORD')) # keep credentials private
sender.send(fbchat.Message(text=f"Logged in successfully with ID {sender.uid}"), thread_id=sender.uid, thread_type=fbchat.ThreadType.USER)


print("CIPHER SENDING SYSTEM")

tgt = input("Target:\n")

while True:
    try:
        text = cipher(input(">>> "))
        sender.send(fbchat.Message(text=text), thread_id=tgt, thread_type=fbchat.ThreadType.USER)
    
    except KeyboardInterrupt:
        # Log the user out
        sender.logout() 