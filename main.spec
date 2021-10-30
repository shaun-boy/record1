# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

pyfile = ['main.py', 'backaccount.py', 'backdatabase.py', 'backup.py',
 'uiLaunchWindow.py', 'uiMainWindow.py', 'UI\\Login.py','UI\\mainwindow.py']

resouce = [('record1.db','.')]

a = Analysis(pyfile,
             pathex=['D:\\Java\\Java program\\pyprogram\\accountbook'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=['xml','_tkinter'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='record',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          icon='D:\\Java\\Java program\\pyprogram\\accountbook\\ico\\g2.ico',
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
