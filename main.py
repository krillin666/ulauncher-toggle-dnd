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

    def on_event(self, event, extension):
        process_gnome = subprocess.Popen(
            ['gsettings', 'get', 'org.gnome.desktop.notifications', 'show-banners'], stdout=subprocess.PIPE)
        output_gnome = process_gnome.stdout.readline().decode('utf-8').strip()

        process_dunst = subprocess.Popen(
            ['dunstctl', 'is-paused'], stdout=subprocess.PIPE)
        output_dunst = process_dunst.stdout.readline().decode('utf-8').strip()

        if output_gnome == 'true':
            value_gnome = 'false' 

        elif output_dunst == 'false: 

            value_dunst = "true" 

        else:

            value_gnome = "true" 
            value_dunst = "false"

        subprocess.Popen(
            'gsettings set org.gnome.desktop.notifications show-banners ' + value_gnome + "&" " dunstctl set-pause " + value_dunst, shell=True)

        return HideWindowAction()


if __name__ == '__main__':
    ToggleDnD().run()
