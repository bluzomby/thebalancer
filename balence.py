#!/usr/bin/env python
import wx
import os

class MainWindow(wx.Frame): # Setting up the window that the game will run in 
	def __init__(self, parent, title):
		wx.Frame.__init__(self, parent, title=title, size=(200,100)) # Set the size of the window
		self.control = wx.TextCtrl(self, style=wx.TE_MULTILINE)
		self.CreateStatusBar()

		# Set up the menu
		filemenu = wx.Menu()

		# using the about and exit on the dropdown 
		menuAbout = filemenu.Append(wx.ID_ABOUT,"&About"," Information about this program")
        menuExit = filemenu.Append(wx.ID_EXIT,"E&xit"," Terminate the program")

        # Creating the menubar.
        menuBar = wx.MenuBar()
        menuBar.Append (filemenu, "&File") # Adding the "filemenu" to the MenuBar
        self.SetMenuBar(menuBar)  # Adding the MenuBar to the Frame content.

        # Set events.
        self.Bind(wx.EVT_MENU, self.OnAbout, menuAbout)
        self.Bind(wx.EVT_MENU, self.OnExit, menuExit)

        self.Show(True)

def OnAbout(self,e):
	dlg = wx.MessageDialog( self, "a small text editor", "written by Jake Massoth", wx.OK)
	dlg.ShowModal()
	dlg.Destroy
def OnExit(self,e):
	self.close(True)
		
app = wx.App(False)
frame = MainWindow(None, 'The Balancer') # Name that the window will have
app.MainLoop()