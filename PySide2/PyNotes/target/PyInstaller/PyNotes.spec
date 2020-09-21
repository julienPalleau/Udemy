# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Udemy\\PySide2\\PyNotes\\src\\main\\python\\main.py'],
             pathex=['C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Udemy\\PySide2\\PyNotes\\target\\PyInstaller'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=['C:\\Users\\MOTTIER LUCIE\\venv\\lib\\site-packages\\fbs\\freeze\\hooks'],
             runtime_hooks=['C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Udemy\\PySide2\\PyNotes\\target\\PyInstaller\\fbs_pyinstaller_hook.py'],
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
          name='PyNotes',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=False,
          console=False , icon='C:\\Users\\MOTTIER LUCIE\\Documents\\GitHub\\Udemy\\PySide2\\PyNotes\\src\\main\\icons\\Icon.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=False,
               upx_exclude=[],
               name='PyNotes')
