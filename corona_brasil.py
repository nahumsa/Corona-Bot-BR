from selenium import webdriver
from datetime import datetime
import numpy as np
import time

class Coronavirus():
    """
    Code based on https://towardsdatascience.com/how-to-track-coronavirus-with-python-a5320b778c8e.
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def update(self):
        try:
            possible_Cases = self.data[0][0]
            confirmed_Cases = self.data[1][0]
            descarted_cases = self.data[2][0]
            deaths = self.data[3][0]
            now = datetime.now()         
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")    

            #print(f"País: Brasil")
            #print(f"Casos Possíveis: {possible_Cases}")
            #print(f"Casos Confirmados: {confirmed_Cases}")            
            #print(f"Casos Descartados: {descarted_cases}")
            #print(f"Mortes: {deaths}")
            
            return f"País: Brasil\nCasos Possíveis: {possible_Cases}\nCasos Confirmados: {confirmed_Cases}\nCasos Descartados: {descarted_cases}\nMortes: {deaths}\nData e Hora : {dt_string} \nDados de : http://plataforma.saude.gov.br/novocoronavirus/ \n#coronavirus"            
        
        except:
            now = datetime.now() 
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
            print("Something is wrong.")
            return f"Estamos com problemas de contatar o site./nData e Hora : {dt_string} \nDados de : http://plataforma.saude.gov.br/novocoronavirus/ \n"


    def get_data(self):
        """Getting data from http://plataforma.saude.gov.br/novocoronavirus/.
        """
        try:                    
            self.data = []
            self.driver.get('http://plataforma.saude.gov.br/novocoronavirus/')
            time.sleep(10)
            for i in np.arange(1,4+1,1):
                #order: Possible Cases, Confirmed Cases, descarted cases, deaths
                dat = self.driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div[1]/div[{i}]/div[2]/h4').text.split(" ")
                self.data.append(dat)                                        

            self.driver.close()            
            

        except:
            self.driver.quit()


if __name__ == "__main__":    
    bot = Coronavirus()
    bot.get_data()
    print(bot.update())
