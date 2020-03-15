# Monitoramento do Coronavirus no Brasil

Esse bot serve para monitorar o funcionamento do coronavirus no Brasil segundo o [site oficial do governo](http://plataforma.saude.gov.br/novocoronavirus/). O código foi baseado no seguinte [post](https://towardsdatascience.com/how-to-track-coronavirus-with-python-a5320b778c8e). 

Primeiramente é necessário instalar o [ChromeDriver](https://chromedriver.chromium.org/). Caso esteja utilizando Linux, deve mover o arquivo para `/usr/local/bin`.


O código foi feito para python 3. Primeiramente crie e ative um virtual environment, com os seguintes passos:

- `pip3 install virtualenv` (Caso não esteja instalado)

- `virtualenv corona_env`

- `source corona_env/bin/activate`

- `pip3 install requirements.txt`

Para rodar o programa Basta rodar o `run.py`.