import os
import shutil
import whisper
from moviepy.editor import VideoFileClip

# Charger le modèle Whisper une seule fois
model = whisper.load_model("base")  # ou "small" selon ton CPU/GPU

def ffmpeg_available() -> bool:
    """Vérifie si FFmpeg est accessible"""
    return shutil.which("ffmpeg") is not None

def video_to_text(video_path: str, language: str = "fr") -> str:
    """
    Transforme une vidéo en texte (transcription audio).
    Ne plante pas si FFmpeg est absent.
    """
    if not os.path.exists(video_path):
        return f"[Erreur] Vidéo non trouvée : {video_path}"

    if not ffmpeg_available():
        return "[Erreur] FFmpeg non trouvé. Installez-le et ajoutez-le au PATH."

    temp_audio = "temp_audio.wav"
    text = ""

    try:
        clip = VideoFileClip(video_path)
        if clip.audio is None:
            return "[Erreur] La vidéo n'a pas de piste audio."
        clip.audio.write_audiofile(temp_audio, verbose=False, logger=None)
        result = model.transcribe(temp_audio, language=language)
        text = result["text"]

    except Exception as e:
        text = f"[Erreur] Impossible de traiter la vidéo : {str(e)}"

    finally:
        clip.close()
        if os.path.exists(temp_audio):
            os.remove(temp_audio)

    return text

def load_videos_from_folder(folder_path: str, language: str = "fr") -> list:
    """
    Transforme toutes les vidéos d’un dossier en texte.
    Retourne une liste de textes.
    """
    texts = []
    if not os.path.exists(folder_path):
        return [f"[Erreur] Dossier non trouvé : {folder_path}"]

    for file in os.listdir(folder_path):
        if file.lower().endswith(".mp4"):
            video_path = os.path.join(folder_path, file)
            text = video_to_text(video_path, language)
            texts.append(text)
    return texts
