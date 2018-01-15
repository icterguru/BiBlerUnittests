"""
__BiBler_Statechart_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Eugene Syriani
Modified: Wed Jan 22 13:27:36 2014
_______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Composite import *
from Basic import *
from contains import *
from Hyperedge import *
from graph_Basic import *
from graph_contains import *
from graph_Hyperedge import *
from graph_Composite import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def BiBler_Statechart_MDL(self, rootNode, DChartsRootNode=None):

    # --- Generating attributes code for ASG DCharts ---
    if( DChartsRootNode ): 
        # variables
        DChartsRootNode.variables.setValue('\n')
        DChartsRootNode.variables.setHeight(15)

        # misc
        DChartsRootNode.misc.setValue('\n')
        DChartsRootNode.misc.setHeight(15)

        # event_clauses
        DChartsRootNode.event_clauses.setValue('\n')
        DChartsRootNode.event_clauses.setHeight(15)
    # --- ASG attributes over ---


    self.obj154=Composite(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    # auto_adjust
    self.obj154.auto_adjust.setValue((None, 1))
    self.obj154.auto_adjust.config = 0

    # name
    self.obj154.name.setValue('Run')

    # is_default
    self.obj154.is_default.setValue((None, 0))
    self.obj154.is_default.config = 0

    # visible
    self.obj154.visible.setValue((None, 1))
    self.obj154.visible.config = 0

    # exit_action
    self.obj154.exit_action.setValue('\n')
    self.obj154.exit_action.setHeight(15)

    # enter_action
    self.obj154.enter_action.setValue('\n')
    self.obj154.enter_action.setHeight(15)

    self.obj154.graphClass_= graph_Composite
    if self.genGraphics:
       new_obj = graph_Composite(220.0,120.0,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Composite", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf2.handler,823.0,177.0,926.0,264.0)
       self.UMLmodel.itemconfig(new_obj.gf2.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf2.handler, fill='')
       self.UMLmodel.coords(new_obj.gf1.handler,823.0,170.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Run')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='Helvetica -12')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj155=Basic(self)
    self.obj155.isGraphObjectVisual = True

    if(hasattr(self.obj155, '_setHierarchicalLink')):
      self.obj155._setHierarchicalLink(False)

    # is_default
    self.obj155.is_default.setValue((None, 1))
    self.obj155.is_default.config = 0

    # name
    self.obj155.name.setValue('Start')

    # exit_action
    self.obj155.exit_action.setValue('\n')
    self.obj155.exit_action.setHeight(15)

    # enter_action
    self.obj155.enter_action.setValue('\n')
    self.obj155.enter_action.setHeight(15)

    self.obj155.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(760.0,100.0,self.obj155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,772.0,103.0,790.099722992,121.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,783.186634349,130.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Start')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font106010984')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.005540166204986, 1]
    else: new_obj = None
    self.obj155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj155)
    self.globalAndLocalPostcondition(self.obj155, rootNode)
    self.obj155.postAction( rootNode.CREATE )

    self.obj156=Basic(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    # is_default
    self.obj156.is_default.setValue((None, 0))
    self.obj156.is_default.config = 0

    # name
    self.obj156.name.setValue('Exit')

    # exit_action
    self.obj156.exit_action.setValue('\n')
    self.obj156.exit_action.setHeight(15)

    # enter_action
    self.obj156.enter_action.setValue('controller.exit()\n')
    self.obj156.enter_action.setHeight(15)

    self.obj156.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(960.0,100.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,972.0,103.0,990.0,121.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKBLUE')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,983.125,130.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Exit')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font100223856')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=Basic(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    # is_default
    self.obj157.is_default.setValue((None, 1))
    self.obj157.is_default.config = 0

    # name
    self.obj157.name.setValue('Idle')

    # exit_action
    self.obj157.exit_action.setValue('\n')
    self.obj157.exit_action.setHeight(15)

    # enter_action
    self.obj157.enter_action.setValue('[DUMP(\'Statechart is idle\')]\n')
    self.obj157.enter_action.setHeight(15)

    self.obj157.graphClass_= graph_Basic
    if self.genGraphics:
       new_obj = graph_Basic(860.0,220.0,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Basic", new_obj.tag)
       self.UMLmodel.coords(new_obj.gf3.handler,872.0,223.0,890.0,241.0)
       self.UMLmodel.itemconfig(new_obj.gf3.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, width='2.0')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, outline='DARKGREEN')
       self.UMLmodel.itemconfig(new_obj.gf3.handler, fill='lightgray')
       self.UMLmodel.coords(new_obj.gf1.handler,883.125,250.0)
       self.UMLmodel.itemconfig(new_obj.gf1.handler, stipple='')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, fill='black')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, text='Idle')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, width='0')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, font='font120082840')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, anchor='center')
       self.UMLmodel.itemconfig(new_obj.gf1.handler, justify='left')
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj158=contains(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    self.obj158.graphClass_= graph_contains
    if self.genGraphics:
       new_obj = graph_contains(279.138290478,366.443472332,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("contains", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj159=Hyperedge(self)
    self.obj159.isGraphObjectVisual = True

    if(hasattr(self.obj159, '_setHierarchicalLink')):
      self.obj159._setHierarchicalLink(False)

    # name
    self.obj159.name.setValue('')
    self.obj159.name.setNone()

    # broadcast
    self.obj159.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj159.broadcast.setHeight(15)

    # guard
    self.obj159.guard.setValue('1')

    # trigger
    self.obj159.trigger.setValue('start')

    # action
    self.obj159.action.setValue('controller=[PARAMS]\n')
    self.obj159.action.setHeight(15)

    # broadcast_to
    self.obj159.broadcast_to.setValue('')
    self.obj159.broadcast_to.setNone()

    # display
    self.obj159.display.setValue('start')

    self.obj159.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(832.942430902,139.98103148,self.obj159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [0.8928571428571429, 0.1]
       new_obj.layConstraints['Label Offset'] = [-12.0, -13.0]
    else: new_obj = None
    self.obj159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj159)
    self.globalAndLocalPostcondition(self.obj159, rootNode)
    self.obj159.postAction( rootNode.CREATE )

    self.obj160=Hyperedge(self)
    self.obj160.isGraphObjectVisual = True

    if(hasattr(self.obj160, '_setHierarchicalLink')):
      self.obj160._setHierarchicalLink(False)

    # name
    self.obj160.name.setValue('')
    self.obj160.name.setNone()

    # broadcast
    self.obj160.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj160.broadcast.setHeight(15)

    # guard
    self.obj160.guard.setValue('1')

    # trigger
    self.obj160.trigger.setValue('exitClicked')

    # action
    self.obj160.action.setValue('\n')
    self.obj160.action.setHeight(15)

    # broadcast_to
    self.obj160.broadcast_to.setValue('')
    self.obj160.broadcast_to.setNone()

    # display
    self.obj160.display.setValue('exitClicked')

    self.obj160.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(933.78301645,137.943472332,self.obj160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
       new_obj.layConstraints['Label Offset'] = [-13.0, 7.0]
    else: new_obj = None
    self.obj160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj160)
    self.globalAndLocalPostcondition(self.obj160, rootNode)
    self.obj160.postAction( rootNode.CREATE )

    self.obj161=Hyperedge(self)
    self.obj161.isGraphObjectVisual = True

    if(hasattr(self.obj161, '_setHierarchicalLink')):
      self.obj161._setHierarchicalLink(False)

    # name
    self.obj161.name.setValue('')
    self.obj161.name.setNone()

    # broadcast
    self.obj161.broadcast.setValue('# return an instance of DEVSevent or None\nreturn None\n')
    self.obj161.broadcast.setHeight(15)

    # guard
    self.obj161.guard.setValue('1')

    # trigger
    self.obj161.trigger.setValue('AFTER(3)')

    # action
    self.obj161.action.setValue('\n')
    self.obj161.action.setHeight(15)

    # broadcast_to
    self.obj161.broadcast_to.setValue('')
    self.obj161.broadcast_to.setNone()

    # display
    self.obj161.display.setValue('after 3')

    self.obj161.graphClass_= graph_Hyperedge
    if self.genGraphics:
       new_obj = graph_Hyperedge(877.0,185.0,self.obj161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Hyperedge", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Label Offset'] = [-59.0, -2.0]
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj161)
    self.globalAndLocalPostcondition(self.obj161, rootNode)
    self.obj161.postAction( rootNode.CREATE )

    # Connections for obj154 (graphObject_: Obj121) named Run
    self.drawConnections(
(self.obj154,self.obj160,[874.0, 177.0, 933.7830164499995, 137.94347233199994],"true", 2),
(self.obj154,self.obj158,[817.9999999999995, 216.0, 279.1382904780131, 366.44347233175597],"true", 2) )
    # Connections for obj155 (graphObject_: Obj122) named Start
    self.drawConnections(
(self.obj155,self.obj159,[788.8994554756022, 116.43524907991583, 832.9424309019997, 139.98103147999984],"true", 2) )
    # Connections for obj156 (graphObject_: Obj123) named Exit
    self.drawConnections(
 )
    # Connections for obj157 (graphObject_: Obj124) named Idle
    self.drawConnections(
(self.obj157,self.obj161,[873.3432000143135, 227.61979166666657, 841.9999999999994, 205.99999999999943, 876.9999999999995, 184.99999999999986],"true", 3) )
    # Connections for obj158 (graphObject_: Obj125) of type contains
    self.drawConnections(
(self.obj158,self.obj157,[279.1382904780131, 366.44347233175597, 872.9793366410263, 236.43524907991582],"true", 2) )
    # Connections for obj159 (graphObject_: Obj126) named 
    self.drawConnections(
(self.obj159,self.obj154,[832.9424309019997, 139.98103147999984, 874.0, 177.0],"true", 2) )
    # Connections for obj160 (graphObject_: Obj128) named 
    self.drawConnections(
(self.obj160,self.obj156,[933.7830164499995, 137.94347233199994, 972.9793366410265, 116.43524907991583],"true", 2) )
    # Connections for obj161 (graphObject_: Obj130) named 
    self.drawConnections(
(self.obj161,self.obj157,[876.9999999999995, 184.99999999999986, 917.9999999999993, 197.9999999999994, 888.920208901211, 227.4947916666666],"true", 3) )

newfunction = BiBler_Statechart_MDL

loadedMMName = 'DCharts'

atom3version = '0.3'
