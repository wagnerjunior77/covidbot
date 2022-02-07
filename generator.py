import json
import requests
from PIL import Image, ImageDraw, ImageFont
import matplotlib.pyplot as plt
import numpy as np
from datetime import date
import os

Path = os.path.abspath(os.curdir)

def generator ():
    # source -- Brazil
    response = requests.get("https://disease.sh/v2/countries/brazil")
    stats = json.loads(response.content)
    # source -- World
    response2 = requests.get("https://disease.sh/v2/all")
    stats2 = json.loads(response2.content)
    # source -- South America
    response3 = requests.get("https://disease.sh/v2/continents/South%20America?yesterday=false")
    statsSA = json.loads(response3.content)

    # SouthAmerica (getting)
    activeSA = statsSA['active']
    recoveredSA = statsSA['recovered']
    deathsSA = statsSA['deaths']


    # BrazilCases (getting)
    cases = stats['cases']
    active = stats['active']
    recovered = stats['recovered']
    deaths = stats['deaths']

    # WorldCases (getting)
    casesW = stats2['cases']
    recoveredW = stats2['recovered']
    deathsW = stats2['deaths']

    # Getting Date
    today = date.today()
    d1 = today.strftime("%d/%m/%Y")

    #Gráfico 1
    plt.figure(num=None, figsize=(5, 5), dpi=100, facecolor='w', edgecolor='k')


    mes_x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

    casos_y = [50, 500, 1000, 3000, 5000, 8000, 20000, 60000, 60050, 65000, 70000, 80000]

    plt.plot(mes_x, casos_y)

    casos_total_y = [5, 55, 155, 455, 955, 1755, 3755, 9755, 15760, 22260, 29260, 37260]

    plt.plot(mes_x, casos_total_y)

    plt.xlabel('Mês')
    plt.ylabel('Total de casos')
    plt.title('Media de casos de COVID-19')

    plt.legend(['Casos no Brasil', 'Casos no Mundo'])
    plt.savefig(Path + "/BotUploads/grafico.jpg")

    #plt.show()

    #Gráfico de Barras
    labels = ['América do Sul (Sem o Brasil)', 'Brasil']
    ativos = [activeSA - active, active]
    recuperados = [recoveredSA - recovered, recovered]
    mortos = [deathsSA - deaths, deaths]

    x = np.arange(len(labels))  # the label locations
    width = 0.35  # the width of the bars

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width / 2, ativos, width, label='Casos Ativos')
    rects2 = ax.bar(x + width / 2, recuperados, width, label='Recuperados')
    rects3 = ax.bar(x + width / 2, mortos, width, label='Mortos')

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Casos/Recuperados')
    ax.set_title(f'COVID 19 - Situação no Continente - {d1}')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rects1)
    autolabel(rects2)
    autolabel(rects3)

    fig.tight_layout()
    plt.savefig(Path + "/BotUploads/graficobarras.jpg")
    #plt.show()


    ## Pillow (criando imagem) -- Dados do Brasil
    image = Image.open(Path + "/Images/brazildata-template.png")
    font_type = ImageFont.truetype('arial.ttf', 50)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(140,227), text=str(f"{cases}"), fill=(0, 0, 0), font=font_type)
    draw.text(xy=(140,461), text=str(recovered), fill=(0, 0, 0), font=font_type)
    draw.text(xy=(140,693), text=str(f"{deaths}"), fill=(0, 0, 0), font=font_type)
    #image.show()

    #Salvando a Imagem e convertendo
    rgb_im = image.convert('RGB')
    rgb_im.save(Path + "/BotUploads/1-brazildata.jpg")

    ## Pillow (criando imagem) -- Dados do Mundo
    image = Image.open(Path + "/Images/worlddata-template.png")
    font_type = ImageFont.truetype('arial.ttf', 50)
    draw = ImageDraw.Draw(image)
    draw.text(xy=(140,227), text=str(f"{casesW}"), fill=(0, 0, 0), font=font_type)
    draw.text(xy=(140,461), text=str(recoveredW), fill=(0, 0, 0), font=font_type)
    draw.text(xy=(140,693), text=str(f"{deathsW}"), fill=(0, 0, 0), font=font_type)
    #image.show()


    # Salvando a Imagem e convertendo
    rgb_im = image.convert('RGB')
    rgb_im.save(Path + "/BotUploads/2-worlddata.jpg")

generator()