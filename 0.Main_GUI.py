import wx
import os

class SNP(wx.Frame):
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, "Modeling Hybrid Feature Selection Method for Discovering Prognostic Gene Biomarkers of Breast and Thyroid Cancer from Complex High Dimensional SNP Profiles", size=(1650,1000))
        panel = wx.Panel(self)
        wx.StaticText(panel, -1, "", (750, 50))
        pic = wx.StaticBitmap(panel,size=(200,300),pos=(100,100))
        pic.SetBitmap(wx.Bitmap("bioinformatics.jpg"))
        self.ShowFullScreen(False)
        ran = wx.Button(panel, label='Proceed', pos=(1000, 400), size=(200, 60))
        cls = wx.Button(panel, label='Exit', pos=(1300, 400), size=(200, 60))

        self.Bind(wx.EVT_BUTTON, self.ran, ran)
        self.Bind(wx.EVT_BUTTON, self.cls, cls)

    def ran(self, event):
     os.system(r" python C:\Users\Karthik-Sekaran\Desktop\Thyroid-Github\Index.py")

    def cls(self, event):
        self.Destroy()

    def closewindow(self, event):
        self.Destroy()


if __name__ == '__main__':
    App = wx.App()
    frame = SNP(parent=None, id=-1)
    frame.Show()
    App.MainLoop()

