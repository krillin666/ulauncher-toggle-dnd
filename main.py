from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
import subprocess



class ToggleDnD(Extension):

    def __init__(self):
        super(ToggleDnD, self).__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())


class KeywordQueryEventListener(EventListener):
    
    value_gnome = ''
    value_dunst = ''

    def on_event(self, event, extension):
        process_gnome = subprocess.Popen(
            ['gsettings', 'get', 'org.gnome.desktop.notifications', 'show-banners'], stdout=subprocess.PIPE)
        output_gnome = process_gnome.stdout.readline().decode('utf-8').strip()


        process_dunst = subprocess.Popen(
            ['dunstctl', 'is-paused'], stdout=subprocess.PIPE)
        output_dunst = process_dunst.stdout.readline().decode('utf-8').strip()

        print("output_gnome = " + output_gnome)
  
        print("output_dunst = " + output_dunst)      
        
        if output_gnome == 'true':
            value_gnome = 'false' 
            print("1")

        elif output_dunst == 'false': 

            value_dunst = "true" 
            print("2")

            
        elif output_gnome == 'false':
            value_gnome = "true" 
            print("3")

            
        elif output_dunst == 'true': 
            print("1")

            value_dunst = "false"

        subprocess.Popen(
            'gsettings set org.gnome.desktop.notifications show-banners ' + value_gnome + " &" " dunstctl set-paused " + value_dunst, shell=True)

        return HideWindowAction()


if __name__ == '__main__':
    ToggleDnD().run()
