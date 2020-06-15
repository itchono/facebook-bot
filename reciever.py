import fbchat

import os
import dotenv

def cipher(s):
    '''
    Simple bidirectional cipher which can decode or encode messages
    '''
    return " ".join([item[-1::-1] for item in s.split()])

class MingBot(fbchat.Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        '''self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)'''

        print(f"Deciphered: {cipher(message_object.text)}")

dotenv.load_dotenv()
receiver = MingBot(os.environ.get('EMAIL'), os.environ.get('PASSWORD'))
receiver.listen()