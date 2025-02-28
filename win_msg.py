# Win MSG plugin is made by LIGHT (imAnesYT)  

# GitHub https://github.com/imAnesYT  

# Source code https://github.com/imAnesYT/win-msg  

# Frequency QnA  

# Q: Can I change the author name and make myself the creator of this plugin?  
# A: No, unfortunately.  

# Q: Can I share this plugin with my friends on YouTube or other platforms?  
# A: Yes, you can.  

# ba_meta require api 9

import babase
import bauiv1 as bui
import bauiv1lib.party
import random
import bascenev1 as bs

# Default Win Messages (Users can edit in settings)
config = babase.app.config
if 'win_msgs' not in config:
    config['win_msgs'] = ["Ezz", "Easy", "Good Game", "GG", "TOO EZ"]

def save_config():
    """Save configuration to persist messages."""
    config.apply_and_commit()

class WinMSG(bauiv1lib.party.PartyWindow):
    def __init__(s, *args, **kwargs):
        super().__init__(*args, **kwargs)
        s._btn = bui.buttonwidget(
            parent=s._root_widget,
            size=(150, 60),
            scale=0.7,
            label='Win Message',
            button_type='square',
            position=(s._width - 170, s._height - 50),
            color=(0.5, 0.5, 0.5),  # Black button color
            textcolor=(1, 1, 1),  # White text for visibility
            on_activate_call=s._winmsg
        )

    def _winmsg(s):
        bs.chatmessage(random.choice(config['win_msgs']))

class WinMSGSettings:
    def __init__(self):
        """Create the settings UI."""
        self._root_widget = bui.containerwidget(
            size=(400, 300),
            transition='in_scale',
            scale=(1.5 if bui.app.ui_v1.uiscale is babase.UIScale.SMALL else 
                   1.2 if bui.app.ui_v1.uiscale is babase.UIScale.MEDIUM else 1.0)
        )

        bui.textwidget(
            parent=self._root_widget,
            position=(200, 250),
            scale=1.2,
            text="WinMSG Settings",
            h_align="center",
            v_align="center",
            maxwidth=300
        )

        # Input field for new messages
        self._input_field = bui.textwidget(
            parent=self._root_widget,
            position=(50, 180),
            size=(300, 40),
            text="",
            h_align="left",
            v_align="center",
            maxwidth=280,
            editable=True
        )

        # Button to add message
        bui.buttonwidget(
            parent=self._root_widget,
            position=(50, 130),
            size=(140, 40),
            label="Add Message",
            button_type="square",
            on_activate_call=self._add_message
        )

        # Button to clear messages
        bui.buttonwidget(
            parent=self._root_widget,
            position=(210, 130),
            size=(140, 40),
            label="Clear Messages",
            button_type="square",
            on_activate_call=self._clear_messages
        )

        # Close Button
        bui.buttonwidget(
            parent=self._root_widget,
            position=(150, 50),
            size=(100, 40),
            label="Close",
            button_type="square",
            on_activate_call=lambda: bui.containerwidget(edit=self._root_widget, transition='out_scale')
        )

    def _add_message(self):
        """Add a new win message."""
        new_msg = bui.textwidget(query=self._input_field).strip()
        if new_msg:
            config['win_msgs'].append(new_msg)
            save_config()
            bui.screenmessage(f"Added: {new_msg}", color=(0, 1, 0))
        else:
            bui.screenmessage("Enter a valid message!", color=(1, 0, 0))

    def _clear_messages(self):
        """Clear all win messages."""
        config['win_msgs'] = []
        save_config()
        bui.screenmessage("Win messages cleared!", color=(1, 0, 0))

# ba_meta export plugin

class ByLIGHT(babase.Plugin):
    def __init__(self):
        bauiv1lib.party.PartyWindow = WinMSG

    @classmethod
    def has_settings_ui(cls) -> bool:
        """Enable settings UI."""
        return True

    @classmethod
    def show_settings_ui(cls, source_widget: bui.Widget | None = None):
        """Show the settings window."""
        WinMSGSettings()
