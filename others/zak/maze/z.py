import curses
from curses.textpad import Textbox

def main(stdscr):
    # 1. Configurer la fenêtre principale en non-bloquant
    stdscr.nodelay(True)
    curses.curs_set(1)

    # 2. Créer la zone de saisie
    win = curses.newwin(1, 20, 5, 20)
    box = Textbox(win)
    
    # Variable pour stocker ce qu'on tape
    saisie_complete = False
    compteur = 0

    stdscr.addstr(2, 2, "Tapez quelque chose (Entrée pour finir) :")

    while not saisie_complete:
        # --- PARTIE ANIMATION / LOGIQUE (Ne s'arrête jamais) ---
        compteur += 1
        stdscr.addstr(10, 2, f"Le programme tourne toujours : {compteur}")
        
        # --- PARTIE INPUT ---
        # On essaie de récupérer une touche sans attendre
        ch = stdscr.getch()

        if ch != -1: # -1 signifie "aucune touche pressée"
            if ch in (10, 13, 7): # Entrée ou Ctrl-G
                saisie_complete = True
            else:
                # On envoie la touche à la textbox manuellement
                box.do_command(ch)
        
        stdscr.refresh()
        win.refresh()
        curses.napms(10) # Petite pause pour pas saturer le CPU (10ms)

    # Récupérer le résultat final
    resultat = box.gather().strip()
    stdscr.nodelay(False) # Remettre en bloquant avant de quitter
    stdscr.clear()
    stdscr.addstr(5, 5, f"Terminé ! Tu as saisi : {resultat}")
    stdscr.getch()

curses.wrapper(main)
