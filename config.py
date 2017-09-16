import os

OVERWRITE_EXISTING = False
STUBS_NAME = 'stubs'
STUBS_NAME = raw_input('Stubs Name [{}]:'.format(STUBS_NAME)) or STUBS_NAME


PROJECT_DIR = os.getcwd()  # Must execute from project dir
BIN_DIR = os.path.join(PROJECT_DIR, 'bin')     # Repository Dlls
STUBS_DIR = os.path.join(PROJECT_DIR, STUBS_NAME) # Stubs Output
STUBS_JSON = os.path.join(PROJECT_DIR, '{}.json'.format(STUBS_NAME))

# List of all required Paths that need to be added in order to find
# the files needed
SYS_PATHS = [
    # Repo Binaries:
    BIN_DIR,
    # RevitAPI
    'C:\\Program Files\\Autodesk\\Revit 2017',
    # RevitAPIUI + Other  Revit Requirements
    'C:\\Program Files\\Autodesk\\Revit 2017\\en-US',
    # ProtoGeometry
    'C:\\Program Files\\Dynamo\\Dynamo Core\\1.2',
    # RevitServices
    'C:\\Program Files\\Dynamo\\Dynamo Revit\\1.2\\Revit_2017',
    # Rhino Common Dependencies
    'C:\\Program Files\\Rhinoceros 5 (64-bit)\\System'
    ]

BUILTIN_MODULES = ['clr', 'wpf']

LOADABLE_ASSEMBLIES = [
   'IronPython.Wpf',
   'System',
   'PresentationFramework',
   'PresentationCore',
   'WindowsBase',
   'System.Drawing',
   'System.Windows.Forms',

   'ProtoGeometry',
   'DSCoreNodes',
   'DSOffice',
   'Tessellation',

   'Rhino3dmIO',
   'RhinoCommon',

   # 'GH_IO',
   # 'Grasshopper',
   # 'GH_Util',
    ]

REVIT_ONLY_ASSEMBLIES = [
    'RevitAPI',
    'RevitAPIUI'
    'RevitServices',
    'RevitNodes',
    ]

# If running inside Revit, Process these only
try:
    __revit__
    LOADABLE_ASSEMBLIES = REVIT_ONLY_ASSEMBLIES
    # LOADABLE_ASSEMBLIES = [ 'RevitAPI', 'RevitAPIUI',] # ONLY REVIT
except NameError:
    pass