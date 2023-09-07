import time
import sys

# Liste d'emojis d'horloge
clock_emojis = ["🕛", "🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]

def update_progress_bar(duration):
    start_time = time.time()  # Temps de départ
    end_time = start_time + duration  # Temps de fin

    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        progress = int((elapsed_time / duration) * 100)

        bar_length = 60
        filled_length = int(bar_length * progress // 100)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        # Obtenez l'indice actuel de l'emoji d'horloge en fonction du temps écoulé et du nombre d'emojis
        emoji_index = int(elapsed_time / (duration / len(clock_emojis)))

        sys.stdout.write('\r')
        sys.stdout.write(f'{clock_emojis[emoji_index]} Progress: [{bar}] {progress}% {clock_emojis[emoji_index]}\r')
        sys.stdout.flush()
        time.sleep(1)  # Attente de 1 seconde avant la prochaine mise à jour de la barre

    sys.stdout.write('\r')
    sys.stdout.write('\r🕛 Progress: [████████████████████████████████████████████████████████████] 100% 🕛\r')  # Affiche la progression complète à la fin

# Utilisation
# Appel de la fonction update_progress_bar avec la durée maximale en secondes (par exemple : 180 pour 3 minutes)
update_progress_bar(15)
