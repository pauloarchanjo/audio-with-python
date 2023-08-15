from gtts import gTTS
import os

def text_to_audio(text, output_audio_path):
    tts = gTTS(text)
    tts.save(output_audio_path)
    
def main():
    input_text_path = 'caminho/para/seu/arquivo.txt'  # Substitua pelo caminho do seu arquivo de texto
    output_audio_path = 'output_audio.mp3'  # Caminho para salvar o arquivo de áudio gerado
    
    with open(input_text_path, 'r', encoding='utf-8') as file:
        text = file.read()
    
    text_to_audio(text, output_audio_path)
    print(f'Áudio gerado e salvo em {output_audio_path}')

if __name__ == "__main__":
    main()
