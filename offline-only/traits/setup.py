import os
from cx_Freeze import setup, Executable
import cx_Freeze.hooks
def hack(finder, module):
    return
cx_Freeze.hooks.load_matplotlib = hack
import scipy
import matplotlib
import PyQt5.Qt

os.environ['ETS_TOOLKIT'] = 'qt4'
os.environ['QT_API'] = 'pyqt5'
scipy_path = os.path.dirname(scipy.__file__) 
pyqt5_path = os.path.dirname(PyQt5.Qt.__file__)

build_exe_options = {"packages": ["sys", "os", "glob",'subprocess',"pyface.ui.qt4", "tvtk.vtk_module", "tvtk.pyface.ui.wx", "matplotlib.backends.backend_qt4",'pygments.lexers',
                                  'tvtk.pyface.ui.qt4','pyface.qt','pyface.qt.QtGui','pyface.qt.QtCore',
                                  'openpyxl','scipy','matplotlib','numpy','math','matplotlib','mayavi',"statistics","sympy","mplcursors","traitsui","pyface"],
                     "include_files": [(str(scipy_path), "scipy"), (str(pyqt5_path), "PyQt5.Qt"), (matplotlib.get_data_path(), "mpl-data")],
                     "includes":['pyface','Traitsui ','PyQt5'],
                     'excludes':'Tkinter',
                    "namespace_packages": ['mayavi']
                    }

executables = [
    Executable('T1.py', targetName="Test.exe",base = 'Win32GUI',)
]

setup(name='Test',
      version='1.0',
      description='',
      options = {"build_exe": build_exe_options},
      executables=executables,
      )