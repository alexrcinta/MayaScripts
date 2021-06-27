#!/usr/bin/env python
# -*- coding: utf-8 -*-

import maya.cmds as mc

ClipmapResMap = {"0.0625m": 0.0625,
                 "0.125m": 0.125,
                 "0.25m": 0.25,
                 "0.50m": 0.50,
                 "1.0m": 1.00,
                 "1.50m": 1.50,
                 "2.00m": 2.00}


def AnchorPoint(self):
    AnchorPoint = mc.spaceLocator
    mc.spaceLocator(name="AnchorPoint")


def CreateLMPlane(self):
    global AnchorPoint_tx, AnchorPoint_ty, ClipmapRes
    AnchorPoint_tx = mc.getAttr('AnchorPoint.translateX')
    AnchorPoint_ty = mc.getAttr('AnchorPoint.translateY')
    RenderRes = mc.intField("RenderRes", query=True, value=True)
    ClipmapRes = mc.optionMenu("ClipmapResMenu", query=True, value=True)

    if ClipmapRes == '':
        ClipmapRes = 1.00
    else:
        ClipmapRes = ClipmapResMap[ClipmapRes]

    h_grid = mc.intField("h_grid", query=True, value=True)
    v_grid = mc.intField("v_grid", query=True, value=True)

    if RenderRes % 2 != 0:
        mc.warning("La resolución debe ser un número par.")
        return -1

    for y in range(0, v_grid):
        for x in range(0, h_grid):
            name = "LMplane_" + str(y + 1) + "_" + str(x + 1)
            mc.polyPlane(n=name, sx=1, sy=1, w=RenderRes, h=RenderRes)
            mc.rotate(90, 0, 0, name)
            mc.move(-(RenderRes / 2), (RenderRes / 2), 0, name + ".scalePivot", name + ".rotatePivot",
                    absolute=True)
            mc.move((RenderRes / 2), -(RenderRes / 2), 0, name)
            mc.makeIdentity(apply=True)
            mc.delete(all=True, constructionHistory=True)
            mc.setAttr(name + ".translateX", AnchorPoint_tx + (x * RenderRes * ClipmapRes))
            mc.setAttr(name + ".translateY", AnchorPoint_ty - (y * RenderRes * ClipmapRes))
            mc.setAttr(name + ".scaleX", ClipmapRes)
            mc.setAttr(name + ".scaleY", ClipmapRes)
            mc.setAttr(name + ".scaleZ", ClipmapRes)

    mc.button(TfwButton, e=True, enable=True)


def CreateTFWs(self):
    global AnchorPoint_tx, AnchorPoint_ty, ClipmapRes

    utmX = mc.floatField("utmX", query=True, value=True)
    utmY = mc.floatField("utmY", query=True, value=True)

    print ("Getting *.tfw files...")
    """Check if window already exists"""
    if mc.window("TFWs Window", exists=True):
        mc.deleteUI("TFWs Window")
    """Create print window"""
    mc.window("TFWs Window", sizeable=True, title="TFWs Window", widthHeight=(100, 200))
    mc.formLayout("TFWs Window")
    calc_1 = str(ClipmapRes)
    calc_2 = str(0.0)
    calc_3 = str(0.0)
    calc_4 = str(-ClipmapRes)
    calc_5 = str(utmX + AnchorPoint_tx + ClipmapRes/2)
    calc_6 = str(utmY + AnchorPoint_ty - ClipmapRes/2)
    mc.scrollField(width=300, height=100, insertText=calc_1 + '\n' + calc_2 + '\n' + calc_3 + '\n' + calc_4 + '\n' + calc_5 + '\n' + calc_6)
    mc.showWindow()


def showUI():
    global TfwButton
    WIDTH = 300
    HEIGHT = 300

    myWin = mc.window(title="Lightmap Manager", w=WIDTH, h=HEIGHT,
                      menuBar=True, minimizeButton=False, maximizeButton=False)
    mainLayout = mc.columnLayout('mainLayout', w=WIDTH)
    mc.separator(height=5, style="in")

    mc.frameLayout(label='Set Noshad Coordinates', width=WIDTH, collapsable=False)
    wrow = WIDTH / 2
    mc.rowLayout('rowLayout', numberOfColumns=2, columnWidth=[(1, wrow), (2, wrow)])

    # Las variables utmx y utmy son para luego coger los datos de estos campos para el boton "Create TFWs"
    utmX_tb = mc.floatField("utmX", minValue=0, precision=3, w=wrow - 5)
    utmY_tb = mc.floatField("utmY", minValue=0, precision=3, w=wrow - 5)

    mc.setParent(mainLayout)
    mc.separator(height=25, style="in")
    mc.button(label="Create Anchor", w=WIDTH, command=AnchorPoint, backgroundColor=(0.275, 1.0, 0.411))
    mc.separator(height=5, style="in")

    mc.text(label='Render Resolution: ')
    RenderRes_tb = mc.intField("RenderRes", minValue=0)
    mc.separator(height=5, style="in")

    mc.text(label='Clipmap Resolution: ')
    mc.separator(height=5, style="in")
    # ClipmapRes_tb = mc.floatField("ClipmapRes", minValue=0, precision=3)

    mc.optionMenu("ClipmapResMenu", width=92)
    mc.menuItem(label='')
    mc.menuItem(label='0.0625m', parent='ClipmapResMenu')
    mc.menuItem(label='0.125m', parent='ClipmapResMenu')
    mc.menuItem(label='0.25m', parent='ClipmapResMenu')
    mc.menuItem(label='0.50m', parent='ClipmapResMenu')
    mc.menuItem(label='1.0m', parent='ClipmapResMenu')
    mc.menuItem(label='1.50m', parent='ClipmapResMenu')
    mc.menuItem(label='2.00m', parent='ClipmapResMenu')
    mc.separator(height=5, style="in")

    mc.text(label='H. Grid: ')
    h_grid_tb = mc.intField("h_grid", minValue=0)
    mc.separator(height=5, style="in")
    mc.text(label='V. Grid:')
    v_grid_tb = mc.intField("v_grid", minValue=0)
    mc.separator(height=5, style="in")

    mc.button(label="Create LM Planes", w=WIDTH, command=CreateLMPlane, backgroundColor=(1.0, 0.706, 0.263))

    mc.separator(height=25, style="in")
    TfwButton = mc.button("Create TFWs", w=WIDTH, command=CreateTFWs, enable=False)
    mc.showWindow(myWin)
