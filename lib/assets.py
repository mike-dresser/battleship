import curses
from curses import wrapper
import time
from window import Window

def logo_a():
        return ''' 
             (          (       ) (   (    (     
         (  )\ )  )   ))\ ) ( /( )\ ))\ ) )\ )  
         ( )\(()/(` )  /(()/( )\()|()/(()/((()/(  
         )((_)/(_))( )(_))(_)|(_)\ /(_))(_))/(_)) 
         ((_)_(_)) (_(_()|_))  _((_|_))(_)) (_))   
         | _ )_ _||_   _/ __|| || |_ _| _ \/ __|  
         | _ \| |   | | \__ \| __ || ||  _/\__ \  
         |___/___|  |_| |___/|_||_|___|_|  |___/
         ________________________________________'''
    

def take_aim_a():
        return '''


          _____ _   _  _____     _   ___ __  __ 
         |_   _/_\ | |/ | __|   /_\ |_ _|  \/  |
           | |/ _ \| ' <| _|   / _ \ | || |\/| |
           |_/_/ \_|_|\_|___| /_/ \_|___|_|  |_|
        _______________________________________
            '''
    
def hit_a():
        return '''


                   __ ______________
                  / // /  _/_  __/ /
                 / _  // /  / / /_/ 
                /_//_/___/ /_/ (_)
        ________________________________________
'''
    
def miss_a():
        return '''


                   __  _______________ __
                 /  |/  /  _/ __/ __/ / /
                / /|_/ // /_\ \_\ \/ /_/ 
               /_/  /_/___/___/___/ (_) 
        ________________________________________
                      '''    


def take_cover_a():
        return '''


        _________   __ ______  _________ _   _________  __
       /_  __/ _ | / //_/ __/ / ___/ __ \ | / / __/ _ \/ /
        / / / __ |/ ,< / _/  / /__/ /_/ / |/ / _// , _/_/ 
       /_/ /_/ |_/_/|_/___/  \___/\____/|___/___/_/|_(_)
            ________________________________________
                   '''


def safe_a():
        return '''


                   _______   ________   __
                  / __/ _ | / __/ __/  / /
                 _\ \/ __ |/ _// _/   /_/ 
                /___/_/ |_/_/ /___/  (_)
        ________________________________________
                      '''

def under_fire_a():
        return '''
                _  _ _  _ ___  ____ ____        
                |  | |\ | |  \ |___ |__/        
                |__| | \| |__/ |___ |  \                        
                   ____  _ ____ ____      
                   |___  | |__/ |___      
                   |     | |  \ |___       
        ________________________________________
                                
'''

def game_over_a():
        return '''

                      ___   _   __  __ ___ 
                     / __| /_\ |  \/  | __|
                    | (_ |/ _ \| |\/| | _| 
                     \___/_/ \_\_|_ |_|___|
                      / _ \ \ / / __| _ \   
                     | (_) \ V /| _|| | /   
                      \___/ \_/ |___|_|_\  
        ________________________________________        '''


def victory_a():
        return '''


          __  ___________ _____ _____ __ __ __  __
         | | / /  _/ ___/_  __/ __ \/ _ \ \/ / | |
         | |/ // // /__  / / / /_/ / , _/\  /  |_|
         |___/___/\___/ /_/  \____/_/|_| /_/   (_)
        ___________________________________________
                                      
'''

def bombs_away_a():
        return '''
                ___  ____  __  ______  ____
               / _ )/ __ \/  |/  / _ )/ __/
              / _  / /_/ / /|_/ / _  |\ \  
             /____/\____/_/__/_/____/___/__
              / _ | | /| / / _ \ \/ /  / /
             / __ | |/ |/ / __ |\  /  /_/ 
            /_/ |_|__/|__/_/ |_|/_/  (_)  
        ________________________________________
'''


# def main(stdscr):
#     curses.curs_set(0)  
#     stdscr.clear()
#     stdscr.addstr(0, 0, bombs_away_a() )
#     stdscr.refresh()

#     progress = 0.0
#     while progress <= 1.0:
#         incoming(stdscr, progress)
#         progress += 0.1
#         time.sleep(0.5)  
    
#     progress = 1.0
#     while progress >= 0.0:
#         outgoing(stdscr, progress)
#         time.sleep(0.5)
#         progress -= 0.1




def incoming(win):
    progress = 0.0
    
    while progress <= 1.0:
    
        bar_width = 40
        fill_width = int(bar_width * progress)
        bar = '      🛳️' + ' ' * (bar_width - fill_width - 1) + '💣' + '0' * fill_width + '🛳️'
        win.add(under_fire_a())
        win.update(bar,1)
        win.add(bar)
      
        progress += 0.1
        time.sleep(0.05)  

def outgoing(win):
    progress = 1.0
    
    while progress >= 0.0:
    
        bar_width = 40
        fill_width = int(bar_width * progress)
        empty_width = bar_width - fill_width - 1
        bar = '     🛳️' + '0' * empty_width + '💣' + ' ' * fill_width + '🛳️'
        win.add(bombs_away_a())
        win.update(bar,1)
        win.add(bar)
      
        progress -= 0.1
        time.sleep(0.05)  



# def outgoing(stdscr, progress):
#     stdscr.clear()
#     stdscr.addstr(0, 0, bombs_away_a())
#     bar_width = 40
#     fill_width = int(bar_width * progress)
#     empty_width = bar_width - fill_width - 1
#     bar = '🛳️' + '0' * empty_width + '💣' + ' ' * fill_width + '🛳️'
#     stdscr.addstr(10, 10, bar)
#     stdscr.addstr(0, 10, bar)
#     stdscr.refresh()

#     progress = 1.0
#     while progress >= 0.0:
#         outgoing(stdscr, progress)
#         time.sleep(0.5)
#         progress -= 0.1

