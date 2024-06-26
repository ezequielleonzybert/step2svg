# -*- mode: python ; coding: utf-8 -*-

import os
import sys

block_cipher = None
icon_path = 'img/logo.ico'
ocp_path = []

if sys.platform == 'win32':
    ocp_path = [(os.path.join(HOMEPATH, 'OCP.cp312-win_amd64.pyd'), '.')]

a = Analysis(
    ['step2svg.py'],
    pathex=[],
    binaries=ocp_path,
    datas=[],
    hiddenimports=['vtkmodules', 'vtkmodules.all'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=['PySide6'],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='step2svg',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,
    onefile=True,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='step2svg',
)
