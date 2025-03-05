# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['C:\\Users\\Chenyen.Guo\\Desktop\\python\\view\\processing_tools.py'],
    pathex=[],
    binaries=[],
    datas=[('C:\\Users\\Chenyen.Guo\\Desktop\\python\\view\\bowl_calculate.py', '.'), ('C:\\Users\\Chenyen.Guo\\Desktop\\python\\view\\bowl_gui.py', '.'), ('C:\\Users\\Chenyen.Guo\\Desktop\\python\\view\\calculate_inner_pich.py', '.'), ('C:\\Users\\Chenyen.Guo\\Desktop\\python\\view\\calculate_pich.py', '.'), ('C:\\Users\\Chenyen.Guo\\Desktop\\python\\view\\processing_tools.py', '.'), ('C:\\Users\\Chenyen.Guo\\Desktop\\python\\view\\xw_view.py', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='processing_tools',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\Chenyen.Guo\\Desktop\\python\\view\\icon_result.ico'],
)
