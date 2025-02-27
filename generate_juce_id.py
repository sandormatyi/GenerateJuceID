import sublime
import sublime_plugin
import string
import random

def new_random_JUCE_id():
    id = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    return id

class GenerateJuceIdCommand(sublime_plugin.TextCommand):
    """
    Generate a Juce ID (6 characters - lowercase, uppercase and digits)
    Plugin logic for the 'generate_juce_id' command.
    """

    def run(self, edit):
        for r, value in zip(self.view.sel(), self.generate_juce_id()):
            self.view.replace(edit, r, value)

    def generate_juce_id(self):
        juce_id = new_random_JUCE_id()
        while True:
            yield juce_id

class GenerateJuceIdListenerCommand(sublime_plugin.EventListener):
    def on_query_completions(self, view, prefix, locations):
        if prefix == 'juce':
            val = re.sub('-', '', str(new_random_JUCE_id()))
        else:
            return []
        
        return [(prefix, prefix, val)] if val else []
