"""
Handles classes and methods to initiate the chemistry calculator GUI.

Classes
----------
    `MainApp` - Initializes calculator GUI and panels.

    `MainPanel` - Represents the main menu panel.

    `SearchPanel` - Represents the Periodic Table search panel.

    `MWMPanel` - Represents the molecular weight calculator panel.

    `MCPanel` - Represents the molecular calculator panel.

    `HalfLifePanel` - Represents the half life calculator panel.

    `NuclearDecayPanel` - Represents the nuclear decay calculator panel.

    `NuclearFissionPanel` - Represents the nuclear fission calculator panel.
"""
import wx
import gui

mainTitle = "Chemistry Calculator"

class MainApp(gui.MainFrame):
    def __init__(self, parent):
        gui.MainFrame.__init__(self, parent)
        self.SetTitle(mainTitle)

        self.mainPanel = MainPanel(self) # Main Menu
        self.searchPanel = SearchPanel(self) # Periodic Table
        self.mwPanel = MWPanel(self) # Molecular Weight
        self.mcPanel = MCPanel(self) # Moleuclar Calculator
        self.halfLifePanel = HalfLifePanel(self) # Half Life Equations
        self.nuclearDecayPanel = NuclearDecayPanel(self) # Nuclear Decay Equations
        self.nuclearFissionPanel = NuclearFissionPanel(self) # Nuclear Fission by Mol

        self.searchPanel.Hide()
        self.mwPanel.Hide()
        self.mcPanel.Hide()
        self.halfLifePanel.Hide()
        self.nuclearDecayPanel.Hide()
        self.nuclearFissionPanel.Hide()

class MainPanel(gui.MainPanel): # Main Menu
    def __init__(self, parent):
        gui.MainPanel.__init__(self, parent)
        self.parent = parent
    
    def changeMainPanelPT(self, event):
        if self.IsShown():
            self.parent.SetTitle("Periodic Table")
            self.Hide()
            self.parent.searchPanel.Show()
    
    def changeMainPanelMW(self, event):
        if self.IsShown():
            self.parent.SetTitle("Molecular Weight")
            self.Hide()
            self.parent.mwPanel.Show()
    
    def changeMainPanelMC(self, event):
        if self.IsShown():
            self.parent.SetTitle("Molecular Calculator")
            self.Hide()
            self.parent.mcPanel.Show()
    
    def changeMainPanelHLE(self, event):
        if self.IsShown():
            self.parent.SetTitle("Half-Life Equations")
            self.Hide()
            self.parent.halfLifePanel.Show()

    def changeMainPanelNDE(self, event):
        if self.IsShown():
            self.parent.SetTitle("Nuclear Decay Equations")
            self.Hide()
            self.parent.nuclearDecayPanel.Show()

    def changeMainPanelNFM(self, event):
        if self.IsShown():
            self.parent.SetTitle("Nuclear Fission by Mol")
            self.Hide()
            self.parent.nuclearFissionPanel.Show()


class SearchPanel(gui.SearchPanel): # Search Periodic Table
    def __init__(self, parent):
        gui.SearchPanel.__init__(self, parent)
        self.parent = parent
    
    def changeMainPanelPT(self, event):
        if self.IsShown():
            self.clear(event)
            self.parent.SetTitle(mainTitle)
            self.Hide()
            self.parent.mainPanel.Show()


class MWPanel(gui.MWPanel): # Calculate Molecular Weight
    def __init__(self, parent):
        gui.MWPanel.__init__(self, parent)
        self.parent = parent

    def changeMainPanelMW(self, event):
        if self.IsShown():
            self.clear(event)
            self.parent.SetTitle(mainTitle)
            self.Hide()
            self.parent.mainPanel.Show()


class MCPanel(gui.MCPanel): # Molecular Calculator
    def __init__(self, parent):
        gui.MCPanel.__init__(self, parent)
        self.parent = parent

    def changeMainPanelMC(self, event):
        if self.IsShown():
            self.clear(event)
            self.parent.SetTitle(mainTitle)
            self.Hide()
            self.parent.mainPanel.Show()


class HalfLifePanel(gui.HalfLifePanel): # Half-Life Equations
    def __init__(self, parent):
        gui.HalfLifePanel.__init__(self, parent)
        self.parent = parent

    def changeMainPanelHLE(self, event):
        if self.IsShown():
            self.clear(event)
            self.parent.SetTitle(mainTitle)
            self.Hide()
            self.parent.mainPanel.Show()


class NuclearDecayPanel(gui.NuclearDecayPanel): # Nuclear Decay Equations
    def __init__(self, parent):
        gui.NuclearDecayPanel.__init__(self, parent)
        self.parent = parent
    
    def changeMainPanelNDE(self, event):
        if self.IsShown():
            self.clear(event)
            self.parent.SetTitle(mainTitle)
            self.Hide()
            self.parent.mainPanel.Show()


class NuclearFissionPanel(gui.NuclearFissionPanel): # Nuclear Fission by Mol
    def __init__(self, parent):
        gui.NuclearFissionPanel.__init__(self, parent)
        self.parent = parent
    
    def changeMainPanelNFM(self, event):
        if self.IsShown():
            self.clear(event)
            self.parent.SetTitle(mainTitle)
            self.Hide()
            self.parent.mainPanel.Show()


def main():
    app = wx.App()
    window = MainApp(None)
    window.Show(True)
    app.MainLoop()

if __name__ == '__main__':
    main()