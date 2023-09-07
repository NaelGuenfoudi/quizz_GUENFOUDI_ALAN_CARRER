import time
import sys

def update_progress_bar(duration):
    start_time = time.time()  # Temps de départ
    end_time = start_time + duration  # Temps de fin

    while time.time() < end_time:
        elapsed_time = time.time() - start_time
        progress = int((elapsed_time / duration) * 100)

        bar_length = 20
        filled_length = int(bar_length * progress // 100)
        bar = '█' * filled_length + '-' * (bar_length - filled_length)

        sys.stdout.write('\r')
        sys.stdout.write(f'Progress: [{bar}] {progress}%')
        sys.stdout.flush()
        time.sleep(.005)  # Attente de 1 seconde avant la prochaine mise à jour de la barre

    sys.stdout.write('\r')
    sys.stdout.write('Progress: [████████████████████] 100%\n')  # Affiche la progression complète à la fin

# Utilisation
# Appel de la fonction update_progress_bar avec la durée maximale en secondes (par exemple : 180 pour 3 minutes)
update_progress_bar(1)
