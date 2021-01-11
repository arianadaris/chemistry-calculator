"""
Handles classes to generate GUI frames for calculator panels, and perform calculations.

Classes
----------
    `MainFrame` - Sets size and layout for GUI.

    `MainPanel` - Represents GUI components to access calculators.

    `SearchPanel` - Represents GUI components to search for elements on Periodic Table.

    `MWPanel` - Represents GUI components to calculate molecular weight of a compound.

    `MCPanel` - Represents GUI components to calculate molecular weight of a compound based on amount (grams).

    `HalfLifePanel` - Represents GUI components to perform half life equations.

    `NuclearDecayPanel` - Represents GUI components to perform nucelar decay equations.

    `NuclearFissionPanel` - Represents GUI components to calculate nuclear fission by mol.
"""
import wx
from element import element
import periodicTable as pt

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = (800, 600), style=wx.DEFAULT_FRAME_STYLE | wx.RESIZE_BORDER)

        self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
        bSizer1 = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(bSizer1)
        self.Layout()

        self.Center(wx.BOTH)

    def __del__(self):
        pass


class MainPanel(wx.Panel): # Main Menu
    def __init__(self,parent):
        wx.Panel.__init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(800, 600), style = wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # Add Labels, Buttons, Dialogs
        self.m_button2 = wx.Button(self, wx.ID_ANY, u"Periodic Table", pos = (200, 50)) # Periodic Table
        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Molecular Weight", pos = (200, 75)) # Molecular Weight
        self.m_button4 = wx.Button(self, wx.ID_ANY, u"Molecular Calculator", pos = (200, 100)) # Molecular Calculator
        self.m_button5 = wx.Button(self, wx.ID_ANY, u"Half-Life Equations", pos = (200, 125)) # Half-Life Equations
        self.m_button6 = wx.Button(self, wx.ID_ANY, u"Nuclear Decay Equations", pos = (200, 150)) # Nuclear Decay Equations
        self.m_button7 = wx.Button(self, wx.ID_ANY, u"Nuclear Fission by Mol", pos = (200, 175)) # Nuclear Fission by Mol

        # Set Sizer and Layout
        self.SetSizer(bSizer5)
        self.Layout()

        # Bind Button Events
        self.m_button2.Bind(wx.EVT_BUTTON, self.changeMainPanelPT)
        self.m_button3.Bind(wx.EVT_BUTTON, self.changeMainPanelMW)
        self.m_button4.Bind(wx.EVT_BUTTON, self.changeMainPanelMC)
        self.m_button5.Bind(wx.EVT_BUTTON, self.changeMainPanelHLE)
        self.m_button6.Bind(wx.EVT_BUTTON, self.changeMainPanelNDE)
        self.m_button7.Bind(wx.EVT_BUTTON, self.changeMainPanelNFM)
    
    def __del__(self):
        pass

    def changeMainPanelPT(self, event):
        event.Skip()
    
    def changeMainPanelMW(self, event):
        event.Skip()
    
    def changeMainPanelMC(self, event):
        event.Skip()

    def changeMainPanelHLE(self, event):
        event.Skip()

    def changeMainPanelNDE(self, event):
        event.Skip()

    def changeMainPanelNFM(self, event):
        event.Skip()


class SearchPanel(wx.Panel): # Search Periodic Table
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(800, 600), style = wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # Add Labels, Buttons, Dialogs
        self.menubutton = wx.Button(self, wx.ID_ANY, u"Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        self.enterbutton = wx.Button(self, wx.ID_ANY, u"Enter", pos = (50, 125))

        self.label_searchbox = wx.StaticText(self, wx.ID_ANY, u"Enter element name, symbol, atomic number, or atomic weight.", pos = (50, 50))
        self.label_result = wx.StaticText(self, id = wx.ID_ANY, pos = (200, 75))
        
        self.searchbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (50, 75))

        # Set Sizer and Layout
        bSizer5.Add(self.menubutton, 0, wx.ALL, 5)
        self.SetSizer(bSizer5)
        self.Layout()

        # Bind Button Events
        self.menubutton.Bind(wx.EVT_BUTTON, self.changeMainPanelPT)
        self.enterbutton.Bind(wx.EVT_BUTTON, self.on_press)
        self.searchbox.Bind(wx.EVT_TEXT_ENTER, self.on_press)

    def __del__(self):
        pass

    def changeMainPanelPT(self, event):
        event.Skip()
    
    def clear(self, event):
        self.searchbox.Clear()
        self.label_result.Hide()

    def on_press(self, event):
        var = self.searchbox.GetValue()

        if var and not pt.searchElement(var) == None:
            element = pt.searchElement(var)
            result = "Element: " + element.name +"\nSymbol: " + element.symbol + "\nGroup: " + element.group + "\nNumber: " + str(element.number) + "\nWeight: " + str(element.weight)
        elif var and pt.searchElement(var) == None:
            result = "Element not found."
        else:
            result = "Error: No input."

        self.label_result.SetLabelText(result)
        self.label_result.Show()


class MWPanel(wx.Panel): # Calculate Molecular Weight
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(800, 600), style = wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # Add Labels, Buttons, Dialogs
        self.menubutton = wx.Button(self, wx.ID_ANY, u"Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        self.enterbutton = wx.Button(self, wx.ID_ANY, u"Enter", pos = (50, 175))

        self.label_searchbox = wx.StaticText(self, wx.ID_ANY, u"Enter expanded compound.\nExample: H2O = HHO", pos = (50, 50))
        self.label_result = wx.StaticText(self, id = wx.ID_ANY, pos = (50, 140))

        self.searchbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (50, 100))

        # Set Sizer and Layout
        bSizer5.Add(self.menubutton, 0, wx.ALL, 5)
        self.SetSizer(bSizer5)
        self.Layout()

        # Bind Button Events
        self.menubutton.Bind(wx.EVT_BUTTON, self.changeMainPanelMW)
        self.enterbutton.Bind(wx.EVT_BUTTON, self.on_press)
        self.searchbox.Bind(wx.EVT_TEXT_ENTER, self.on_press)

    def __del__(self):
        pass

    def changeMainPanelMW(self, event):
        event.Skip()
    
    def clear(self, event):
        self.searchbox.Clear()
        self.label_result.Hide()

    def on_press(self, event):
        compound = self.searchbox.GetValue()

        if compound:
            mw = pt.getMolecularWeight(compound)
            result = "Molecular Weight of " + compound + ": " + str(mw)
        else:
            result = "Error: No input."

        self.label_result.SetLabelText(result)
        self.label_result.Show()


class MCPanel(wx.Panel): # Molecular Calculator
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(800, 600), style = wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # Add Labels, Buttons, Dialogs
        self.menubutton = wx.Button(self, wx.ID_ANY, u"Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        self.enterbutton = wx.Button(self, wx.ID_ANY, u"Enter", pos = (200, 150))

        self.label_compound = wx.StaticText(self, wx.ID_ANY, u"Enter compound.", pos = (87, 50))
        self.label_grams = wx.StaticText(self, wx.ID_ANY, u"Enter amount of grams.", pos = (50, 100))
        self.label_result = wx.StaticText(self, id = wx.ID_ANY, pos = (50, 250))

        self.compoundbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (200, 50))
        self.gramsbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (200, 100))
       
        # Set Sizer and Layout
        bSizer5.Add(self.menubutton, 0, wx.ALL, 5)
        self.SetSizer(bSizer5)
        self.Layout()

        # Bind Buttons Events
        self.menubutton.Bind(wx.EVT_BUTTON, self.changeMainPanelMC)
        self.enterbutton.Bind(wx.EVT_BUTTON, self.on_press)
        self.compoundbox.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        self.gramsbox.Bind(wx.EVT_TEXT_ENTER, self.on_press)

    def __del__(self):
        pass
    
    def changeMainPanelMC(self, event):
        event.Skip()

    def clear(self, event):
        self.compoundbox.Clear()
        self.gramsbox.Clear()
        self.label_result.Hide()

    def on_press(self, event):
        compound = self.compoundbox.GetValue()
        grams = float(self.gramsbox.GetValue())

        if compound and grams:
            mc = pt.getMol(compound, grams)
            result = "Molecular Weight of " + str(grams) + " units of " + compound + ": " + str(mc)
        elif compound and not grams or grams and not compound:
            result = "Error: Both inputs required."
        else:
            result = "Error: No input."

        self.label_result.SetLabelText(result)
        self.label_result.Show()


class HalfLifePanel(wx.Panel): # Half-Life Equations
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(800, 600), style = wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # Add Labels, Buttons, Dialogs
        self.menubutton = wx.Button(self, wx.ID_ANY, u"Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        self.enterbutton = wx.Button(self, wx.ID_ANY, u"Enter", pos = (310, 200))
        self.clearbutton = wx.Button(self, wx.ID_ANY, u"Clear", pos = (50, 275))

        self.label_instruction = wx.StaticText(self, wx.ID_ANY, u"Enter 0 for unknown variable. For unnecessary unknown variable, enter 1.", pos = (50, 50))
        self.label_massI = wx.StaticText(self, wx.ID_ANY, u"Enter initial mass.", pos = (50, 75))
        self.label_massF = wx.StaticText(self, wx.ID_ANY, u"Enter final mass.", pos = (50, 100))
        self.label_time = wx.StaticText(self, wx.ID_ANY, u"Enter time duration.", pos = (50, 125))
        self.label_halflife = wx.StaticText(self, wx.ID_ANY, u"Enter half-life of element.", pos = (50, 150))
        self.label_rate = wx.StaticText(self, wx.ID_ANY, u"Enter rate constant.", pos = (50, 175))
        self.label_result = wx.StaticText(self, wx.ID_ANY, pos = (50, 250))

        self.massIbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (300, 75))
        self.massFbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (300, 100))
        self.timebox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (300, 125))
        self.halflifebox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (300, 150))
        self.ratebox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (300, 175))

        # Set Sizer and Layout
        bSizer5.Add(self.menubutton, 0, wx.ALL, 5)
        self.SetSizer(bSizer5)
        self.Layout()

        # Bind Button Events
        self.menubutton.Bind(wx.EVT_BUTTON, self.changeMainPanelHLE)
        self.enterbutton.Bind(wx.EVT_BUTTON, self.on_press)
        self.clearbutton.Bind(wx.EVT_BUTTON, self.clear)

        self.massIbox.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        self.massFbox.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        self.timebox.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        self.halflifebox.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        self.ratebox.Bind(wx.EVT_TEXT_ENTER, self.on_press)

    def __del__(self):
        pass
    
    def changeMainPanelHLE(self, event):
        event.Skip()
    
    def clear(self, event):
        self.massIbox.Clear()
        self.massFbox.Clear()
        self.timebox.Clear()
        self.halflifebox.Clear()
        self.ratebox.Clear()
        self.label_result.Hide()
    
    def on_press(self, event):
        massI = float(self.massIbox.GetValue())
        massF = float(self.massFbox.GetValue())
        time = float(self.timebox.GetValue())
        halflife = float(self.halflifebox.GetValue())
        rate = float(self.ratebox.GetValue())

        result = pt.getHalfLife(massI, massF, time, halflife, rate)
        
        self.label_result.SetLabelText(result)
        self.label_result.Show()
        

class NuclearDecayPanel(wx.Panel): # Nuclear Decay Equations
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(800, 600), style = wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # Add Labels, Buttons, Dialogs
        self.menubutton = wx.Button(self, wx.ID_ANY, u"Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        self.enterbutton = wx.Button(self, wx.ID_ANY, u"Enter", pos = (207, 150))
        self.clearbutton = wx.Button(self, wx.ID_ANY, u"Clear", pos = (50, 250))

        self.label = wx.StaticText(self, wx.ID_ANY, u"Enter mass number, atomic number, and decay type.", pos = (50, 50))
        self.label_mass = wx.StaticText(self, wx.ID_ANY, u"Enter mass number.", pos = (50, 75))
        self.label_number = wx.StaticText(self, wx.ID_ANY, u"Enter atomic number.", pos = (50, 100))
        self.label_decay = wx.StaticText(self, wx.ID_ANY, u"Enter decay type.", pos = (50, 125))

        self.label_decays = wx.StaticText(self, wx.ID_ANY, u"DECAYS\nAlpha Emission: 4;2 He\nBeta Emission: 0;-1 e\nPositron Emission: 0;+1 e\nElectron Transfer: 0;-1 e\nGamma Decay: 0/0γ", pos = (450, 50)) 

        self.label_initial = wx.StaticText(self, wx.ID_ANY, pos = (50, 175))
        self.label_daughter = wx.StaticText(self, wx.ID_ANY, pos = (50, 200))

        self.massbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (200, 75))
        self.numberbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (200, 100))
        self.decaybox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (200, 125))

        # Set Sizer and Layout
        bSizer5.Add(self.menubutton, 0, wx.ALL, 5)
        self.SetSizer(bSizer5)
        self.Layout()

        # Bind Button Events
        self.menubutton.Bind(wx.EVT_BUTTON, self.changeMainPanelNDE)
        self.enterbutton.Bind(wx.EVT_BUTTON, self.on_press)
        self.massbox.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        self.numberbox.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        self.decaybox.Bind(wx.EVT_TEXT_ENTER, self.on_press)
        self.clearbutton.Bind(wx.EVT_BUTTON, self.clear)

    def __del__(self):
        pass
    
    def changeMainPanelNDE(self, event):
        event.Skip()

    def clear(self, event):
        self.massbox.Clear()
        self.numberbox.Clear()
        self.decaybox.Clear()
        self.label_result.Hide()

    def on_press(self, event):
        mass = int(self.massbox.GetValue())
        number = int(self.numberbox.GetValue())
        decay = self.decaybox.GetValue()

        initial = "Initial: " + str(mass) + ";" + str(number) + " " + pt.getSymbol(number)
        daughter = pt.getNuclearDecay(mass, number, decay)

        self.label_initial.SetLabelText(initial)
        self.label_daughter.SetLabelText(daughter)
        self.label_initial.Show()
        self.label_daughter.Show()


class NuclearFissionPanel(wx.Panel): # Nuclear Fission by Mol
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, id = wx.ID_ANY, pos = wx.DefaultPosition, size = wx.Size(800, 600), style = wx.TAB_TRAVERSAL)
        bSizer5 = wx.BoxSizer(wx.VERTICAL)

        # Add Labels, Buttons, Dialogs
        self.menubutton = wx.Button(self, wx.ID_ANY, u"Main Menu", wx.DefaultPosition, wx.DefaultSize, 0)
        self.enterbutton = wx.Button(self, wx.ID_ANY, u"Enter", pos = (132, 100))
        self.clearbutton = wx.Button(self, wx.ID_ANY, u"Clear", pos = (50, 150))

        self.label = wx.StaticText(self, wx.ID_ANY, u"Enter mol value to calculate nuclear fission.", pos = (50, 50))
        self.label_mol = wx.StaticText(self, wx.ID_ANY, u"Enter mol.", pos = (50, 75))
        self.label_result = wx.StaticText(self, wx.ID_ANY, pos = (50, 125))

        self.molbox = wx.TextCtrl(self, style = wx.TE_PROCESS_ENTER, pos = (125, 75))

        # Set Sizer and Layout
        bSizer5.Add(self.menubutton, 0, wx.ALL, 5)
        self.SetSizer(bSizer5)
        self.Layout()

        # Bind Button Events
        self.menubutton.Bind(wx.EVT_BUTTON, self.changeMainPanelNFM)
        self.enterbutton.Bind(wx.EVT_BUTTON, self.on_press)
        self.clearbutton.Bind(wx.EVT_BUTTON, self.clear)

    def __del__(self):
        pass

    def changeMainPanelNFM(self, event):
        event.Skip()

    def clear(self, event):
        self.molbox.Clear()
        self.label_result.Hide()

    def on_press(self, event):
        mol = float(self.molbox.GetValue())

        nuclearFission, power = pt.getNuclearFission(mol)
        result = str('{0:.8g}'.format(nuclearFission)) + " * 10^" + str(power) + " J/mol U-235"

        self.label_result.SetLabelText(result)
        self.label_result.Show()