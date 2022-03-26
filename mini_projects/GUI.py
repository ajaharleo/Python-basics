import logging
import kivy
logging.basicConfig(filename = 'test5.log',level=logging.DEBUG,format ='%(asctime)s %(message)s')
logging.info('Importing all required kivy libraries')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #initialize infinite keywords
    logging.info('Creating Gridlayout class')
    def __init__(self,**kwargs):
        #call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        #set columns
        logging.info('Creating GUI buttons and widgets')
        self.cols = 1
        self.add_widget(Label(text="Put your Path here: ",font_size='25sp'))
        self.address = TextInput()
        self.add_widget(self.address)
        # add submit button
        self.submit = Button(text = 'SUBMIT',width=10,height=10,pos_hint={'center_x':0.8})
        self.submit.bind(on_press=self.PDF_merging)
        self.add_widget((self.submit))

    logging.info('Calling our Main PDF_merging() function after getting input')
    def PDF_merging(self,instance):
        import os
        try:
            path = self.address.text
            files = os.listdir(path)  # list down all the pdf file in the given path
            count = 0
            logging.info('Counting Number of PDF files at the location')
            for i in files:
                if i.endswith('.pdf'):
                    count += 1
            logging.error("Given path may be not correct")
            if count == 0:
                self.add_widget(Label(text=f'there are no pdf files in the location: {path}'))
            elif count == 1:
                self.add_widget(Label(text=f'there are only one pdf files in the location: {path}'))
            else:
                #get merged pdf name
                import datetime
                now = datetime.datetime.now()
                name = now.strftime("%B%d_%Y_%H_%M_%S%p")

                #merging pdfs to a one file
                try:
                    from PyPDF2 import PdfFileMerger
                    merger = PdfFileMerger()
                    st = name + '.pdf'
                    for i in files:
                        if i.endswith('.pdf'):
                            merger.append(os.path.join(path, i))
                    final = merger.write(path + st)
                    merger.close()

                    # move processed pdfs to newly created directory

                    self.add_widget(Label(text=f'we found {count} PDFs at the location :{path}.find Merged PDF and log file at current working directory'))
                    self.address.text = ''
                except Exception as e:
                    loggin.error(e)
        except Exception as e:
            logging.error(e)

class Myapp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    Myapp().run()