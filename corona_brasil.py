from selenium import webdriver
from datetime import datetime
import numpy as np
import time

class Coronavirus_min_saude():
    """
    Code based on https://towardsdatascience.com/how-to-track-coronavirus-with-python-a5320b778c8e.
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    # DEPRACATED
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
            return f" Estamos com problemas de contatar o site. \n Data e Hora : {dt_string} \n Dados de : http://plataforma.saude.gov.br/novocoronavirus/ \n"


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

class Coronavirus_WorldOmeter():
    """
    Code based on https://towardsdatascience.com/how-to-track-coronavirus-with-python-a5320b778c8e.
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    # DEPRACATED
    def update(self):                
        """Update the bot.
        
        Returns:
            String -- Return statistics.
        """
        try:
            country = self.data[0]
            total_cases = self.data[1]
            new_cases = self.data[2]
            total_deaths = self.data[3]
            new_deaths = self.data[4]
            total_recovered = self.data[5]
            active_cases = self.data[6]
            serious_cases = self.data[7]
            tot_cases_p_1m = self.data[8]

            now = datetime.now()         
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")    

           #print(f"País: {country}")
           #print(f"Casos Totais: {total_cases}")
           #print(f"Casos Novos: {new_cases}")
           #print(f"Mortes: {total_deaths}")
           #print(f"Novas Mortes: {new_deaths}")
           #print(f"Pacientes Recuperados: {total_recovered}")
           #print(f"Casos Ativos: {active_cases}")
           #print(f"Casos Sérios: {serious_cases}")
           #print(f"Total de casos por 1 milhão de habitantes: {tot_cases_p_1m}")
           #print(f"Data e Hora : {dt_string}")
            
            return f"País: {country}\nCasos Totais: {total_cases}\nCasos Novos: {new_cases}\nMortes: {total_deaths}\nNovas Mortes: {new_deaths}\nData e Hora : {dt_string}\nDados de : https://www.worldometers.info/coronavirus/ \n#coronavirus"                                                
        
        except:
            now = datetime.now() 
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
            print("Something is wrong.")
            return f" Estamos com problemas de contatar o site. \n Data e Hora : {dt_string} \n Dados de : https://www.worldometers.info/coronavirus/ \n"

    
    def get_data(self):
        """Getting data from https://www.worldometers.info/coronavirus/.
        """
        try:        
            self.driver.get('https://www.worldometers.info/coronavirus/')
            time.sleep(10)
            table = self.driver.find_element_by_xpath('/html/body/div[3]/div[3]/div/div[3]/div[1]/div/table')
            country_element = table.find_element_by_xpath("//td[contains(., 'Brazil')]")
            row = country_element.find_element_by_xpath('./..')
            self.data = row.text.split(" ")                        

            self.driver.close()            
            

        except:
            self.driver.quit()
        

if __name__ == "__main__":    
    bot = Coronavirus_WorldOmeter()
    bot.get_data()
    print(bot.update())
