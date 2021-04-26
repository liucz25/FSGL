# -*- mode: python ; coding: utf-8 -*-
import os
import importlib

block_cipher = None
packages_path = r'D:\code\python38\Lib\site-packages'

auto_imports = []
crawl_path = os.path.abspath(os.path.join(packages_path, 'pyface', 'ui', 'qt4'))
for file in os.listdir(crawl_path):
    file_path = os.path.join(crawl_path, file)
    if file not in {'__pycache__', '__init__.py'} and (
            os.path.isdir(file_path) or (os.path.isfile(file_path) and file_path.endswith('.py'))):
        auto_imports.append('pyface.ui.qt4.%s' % file.replace('.py', ''))


a = Analysis(['t1.py'],
             pathex=['D:\\code\\fsgl\\offline-only\\traits'],
             binaries=[],
             datas=[('%s/pyface-7.3.0-py3.8.egg-info' % packages_path, 'pyface-7.3.0-py3.8.egg-info'),
        ('%s/traitsui-7.1.1-py3.8.egg-info' % packages_path, 'traitsui-7.1.1-py3.8.egg-info'),],
             hiddenimports=[
        'importlib_metadata',
        'importlib_resources',
        'numpy',
        'pyface',
        'pyface.toolkit',
        'pyface.ui.qt',
        'pyface.ui.qt4',
        'pyface.ui.qt4.action',
        'pyface.ui.qt4.clipboard',
        'pyface.ui.qt4.code_editor',
        'pyface.ui.qt4.console',
        'pyface.ui.qt4.data_view',
        'pyface.ui.qt4.fields',
        'pyface.ui.qt4.images',
        'pyface.ui.qt4.init',
        'pyface.ui.qt4.tasks',
        'pyface.ui.qt4.tests',
        'pyface.ui.qt4.timer',
        'pyface.ui.qt4.util',
        'pyface.ui.qt4.wizard',
        'pyface.ui.qt4.workbench',
        'pywin32_system32',
        'pywintypes',
        'scipy',
        'traitsui',
        'traitsui.qt4',
        'traitsui.qt4.extra',
        'traitsui.qt4.toolkit',
        'traitsui.toolkit',
        'traitsui.ui_traits',
    ],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='t1',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='t1')
