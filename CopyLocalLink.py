import sublime, sublime_plugin
import os, re, subprocess

# To open those links, use https://github.com/inopinatus/sublime_url
class CopyLocalLinkCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    file = self.view.file_name()
    line, col = self.view.rowcol(self.view.sel()[0].begin())
    link = "subl://open?url=file://{0}&line={1}&column={2}".format(file, line, col)
    sublime.set_clipboard(link)
