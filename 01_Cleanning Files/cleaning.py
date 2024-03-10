import os
import shutil
import schedule
import time
os.chdir(r'C:\Users\Omar\Downloads')

def Cleaning():
    folder = ['Images','Documents','Applications','Zip Files','Movies']
    for f in folder:
        if not os.path.exists(f):
            os.makedirs(f)
    for file in os.listdir('.'):
        if file.endswith(('png','jpg','jpeg','gif')):
            shutil.move(file,'Images')
        elif file.endswith(('pdf','ppt','sql','doc','webp','docx','txt')):
            shutil.move(file,'Documents')   
        elif file.endswith(('exe','msi')):
            shutil.move(file,'Applications')
        elif file.endswith(('zip','rar')):
            shutil.move(file,'Zip Files')
        elif file.endswith(('mp4',)):
            shutil.move(file,'Movies')


    print('DOne')

schedule.every(10).seconds.do(Cleaning)
while True:
    schedule.run_pending()
    time.sleep(1)
