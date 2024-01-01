import requests
from pytube import YouTube
from tqdm import tqdm

def linha():
    print("-" * 30)

def verificar_link(link: str):
    return link.startswith("https://youtu") or link.startswith("https://www.youtu")

def pegar_link(url: str) -> None:
    if verificar_link(url):
        print("Começando o download...")
        yt = YouTube(url=url)
        video = yt.streams.get_highest_resolution()
        caminho = video.download()
        
        video_url = video.url
        
        resposta = requests.get(video_url, stream=True)
        tamanho_arquivo = int(resposta.headers.get('content-length'))
        
        with open(caminho, 'wb') as arquivo:
            progresso = tqdm(total=tamanho_arquivo, unit='bytes', unit_scale=True, desc=yt.title)
            for parte in resposta.iter_content(chunk_size=1024):
                if parte:
                    arquivo.write(parte)
                    progresso.update(len(parte))
            progresso.close()
        
        print(f"\nDownload completo! Vídeo salvo em: {caminho}")
            
    else:
        print("O link não é válido como um link do YouTube")

linha()
url = str(input("Insira um link válido do YouTube: "))
pegar_link(url)
linha()
