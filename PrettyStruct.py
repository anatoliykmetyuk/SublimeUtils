import sublime, sublime_plugin

class PrettyStructCommand(sublime_plugin.TextCommand):
  def refine(self, to_refine):
    result = ''
    indentLevel = 0
    indentSize = sublime.load_settings("PrettyStruct.sublime-settings").get("indent_size")
    newLine = lambda: '\n' + ' ' * indentLevel * indentSize
    for c in to_refine:
      if c in ['(', '[']:
        indentLevel += 1
        result += c + newLine()
      elif c in [')', ']']:
        indentLevel -= 1
        result += newLine() + c
      elif c == ',':
        result += c + newLine()
      else:
        result += c
    return result

  def run(self, edit):
    selected_region = self.view.sel()[0]
    to_refine = self.view.substr(selected_region)
    refined = self.refine(to_refine)
    self.view.replace(edit, selected_region, refined)
