#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/7/28 21:36
# @Author  : Desong Tang
# @E-Mail  : Desong_Tang@qq.com
# @File    : main.py

import wx


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, parent=None, id=-1, title='Dashboard View', size=(683, 384), pos=(500, 200))

        # self.font = wx.Font(22, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False)

        self.panel = wx.Panel(self, -1)
        self.sizer = wx.GridBagSizer(vgap=1, hgap=1)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        self.sizer.Add(self.btn_tt_breakdown, pos=(0, 0), span=(1, 1), flag=wx.EXPAND, userData=None)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        self.sizer.Add(self.btn_tt_breakdown, pos=(0, 1), span=(1, 1), flag=wx.EXPAND, userData=None)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        self.sizer.Add(self.btn_tt_breakdown, pos=(0, 2), span=(1, 1), flag=wx.EXPAND, userData=None)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        self.sizer.Add(self.btn_tt_breakdown, pos=(0, 3), span=(1, 1), flag=wx.EXPAND, userData=None)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        self.sizer.Add(self.btn_tt_breakdown, pos=(1, 0), span=(1, 1), flag=wx.EXPAND, userData=None)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        self.sizer.Add(self.btn_tt_breakdown, pos=(1, 1), span=(1, 2), flag=wx.EXPAND, userData=None)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        self.sizer.Add(self.btn_tt_breakdown, pos=(1, 3), span=(1, 1), flag=wx.EXPAND, userData=None)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        self.sizer.Add(self.btn_tt_breakdown, pos=(2, 0), span=(1, 1), flag=wx.EXPAND, userData=None)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        self.sizer.Add(self.btn_tt_breakdown, pos=(2, 1), span=(1, 2), flag=wx.EXPAND, userData=None)
        self.btn_tt_breakdown = wx.Button(self, -1, u'Test Time Breakdown')
        # self.sizer.Add(self.btn_tt_breakdown, pos=(2, 3), span=(1, 1), proportion=1, flag=wx.EXPAND, userData=None)

        self.panel.SetSizer(self.sizer)
        self.Fit()

        # logo_sys = wx.Image(load_image('logo_sys.png'), wx.BITMAP_TYPE_ANY).ConvertToBitmap()
        # wx.StaticBitmap(panel, -1, logo_sys, pos=(40, 90), size=(85, 85))


def main():
    app = wx.App()
    frame = MainFrame()
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
