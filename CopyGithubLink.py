import sublime, sublime_plugin
import os, re, subprocess

def line_and_link(view):
  dotty_dir = os.path.join(view.window().folders()[0], 'dotty')
  line_start = view.rowcol(view.sel()[0].begin())[0]
  line_end = view.rowcol(view.sel()[0].end())[0]
  file = os.path.relpath(view.file_name(), dotty_dir)
  dotty_repo_url = 'https://github.com/lampepfl/dotty/blob/master/'
  return dotty_repo_url + file, line_start+1, line_end+1

class CopyGithubLinkCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sublime.set_clipboard(line_and_link(self.view)[0])

class CopyGithubLineCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    link, line_start, line_end = line_and_link(self.view)
    if line_start == line_end:
      suffix = '#L{0}'.format(line_start)
    else:
      suffix = '#L{0}-L{1}'.format(line_start, line_end)
    sublime.set_clipboard(link + suffix)