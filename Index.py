import wx
import os

class SNP(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Modeling Hybrid Feature Selection Method for Discovering Prognostic Gene Biomarkers of Breast and Thyroid Cancer from Complex High Dimensional SNP Profiles", size=(1650,1000))
        panel = wx.Panel(self)
        wx.StaticText(panel, -1, "Workflow of the System", (750, 50))
        proc_1 = wx.Button(panel, label='Data Encoding and Redundancy Elimination', pos=(200, 100), size=(300, 60))
        proc_2 = wx.Button(panel, label='Missing Value Treatment and Data Balancing', pos=(400, 200), size=(300, 60))
        proc_3 = wx.Button(panel, label='Removal of Redundant Features', pos=(600, 300), size=(300, 60))
        proc_4 = wx.Button(panel, label='CFS-L2-Regularization', pos=(800, 400), size=(300, 60))
        proc_5 = wx.Button(panel, label='Classification and AUROC visualization', pos=(1000, 500), size=(300, 60))
        exit = wx.Button(panel, label='Exit', pos=(1200, 600), size=(200, 60))

        self.Bind(wx.EVT_BUTTON, self.DERE, proc_1)
        self.Bind(wx.EVT_BUTTON, self.MVTDB, proc_2)
        self.Bind(wx.EVT_BUTTON, self.RRF, proc_3)
        self.Bind(wx.EVT_BUTTON, self.CFSL2, proc_4)
        self.Bind(wx.EVT_BUTTON, self.CAUROC, proc_5)
        self.Bind(wx.EVT_BUTTON, self.exit, exit)


    def DERE(self, event):
     os.system(r" python C:\Users\Karthik-Sekaran\Desktop\Breast-Github\1.Data-Encoding-and-Redundancy-Elimination.py")

    def MVTDB(self, event):
     os.system(r" python C:\Users\Karthik-Sekaran\Desktop\Breast-Github\2.Missing-Value-Treatment-and-Data-Balancing.py")

    def RRF(self, event):
     os.system(r" python C:\Users\Karthik-Sekaran\Desktop\Breast-Github\3.Removal-of-Redundant-Features.py")

    def CFSL2(self, event):
     os.system(r" python C:\Users\Karthik-Sekaran\Desktop\Breast-Github\4.CFS-L2-Regularization.py")

    def CAUROC(self, event):
        os.system(r" python C:\Users\Karthik-Sekaran\Desktop\Breast-Github\5.Classification-and-AUROC-visualization.py")

    def exit(self, event):
     self.Destroy()

    def closewindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    App = wx.App()
    frame = SNP(parent=None, id=-1)
    frame.Show()
    App.MainLoop()

