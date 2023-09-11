import PyPDF2
from gtts import gTTS
import os

def reader(file1,start=1,end=None):
    if not os.path.exists(file1):
        print("File not found")
        return
    
    pdfreader=PyPDF2.PdfReader(open(file1,'rb'))
    if end==None:
        end=len(pdfreader.pages)
    text=''

    for i in range(start-1,end):
        page=pdfreader.pages[i]
        text+=page.extract_text()
    
    tts=gTTS(text,lang='en')
    if os.path.exists('output.mp3'):
        os.remove('output.mp3')
    tts.save('output.mp3')
    

if __name__=='__main__':
    ipfile=input("Enter the path to the pdf file: ")
    choice=input("Do you want to customize the start page and/or the end page? (y/n)")
    if choice=='y':
        start=int(input("Enter starting page number of choice: "))
        end=int(input("Enter ending page number of choice: (enter 'null' to skip customizing last page)"))
        if end=='null':
            end=None
        reader(ipfile,start,end)
    else:
        reader(ipfile,1,None)
    print("Audio file stored as output.")