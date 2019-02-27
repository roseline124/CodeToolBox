"""
 python 프로그램을 실행파일로 변환
"""

# -*- coding: utf-8 -*-
# """
from distutils.core import setup
# from setuptools import setup
# import py2exe

# name, description, version등의 정보는 일반적인 setup.py와 같습니다.
setup(name="test_py2xxx",
      description="py2exe test application",
      version="0.0.1",
      windows=[{
            #   "pyside_run.py"
          "script": "pyside_run.py",
            #  "icon_resources": [(1, "resources/window_icon.ico")], #아이콘 이미지 
            #   "dest_base": "myfirstapp"
                }], # 실행파일명 
      options={
          "py2exe": {
              #실행 파일을 하나로 묶어준다. 
              "bundle_files": 1, 
              "packages" : ["encodings"],
              # PySide 구동에 필요한 모듈들은 포함시켜줍니다.
              "includes": ["PySide2.QtWidgets",
                        #     "PySide.QtCore",
                        #    "PySide.QtGui",
                        #    "PySide.QtWebKit",
                        #    "PySide.QtNetwork",
                        #    "PySide.QtXml",
                           ],
              # 존재하지 않거나 불필요한 파일은 제거합니다.
            #   "dll_excludes": ["msvcr71.dll",
                            #    "MSVCP90.dll"],
          }
      }, 
      zipfile=None
      )
# """

# 패키징은 CMD에 다음과 같이 입력한다.
#python setup.py py2exe
"""
cx_Freeze 사용 
"""
"""
import sys, os
from cx_Freeze import setup, Executable

__version__ = "1.1.0"

include_files = [
                 'config.py', 
                 ]
# excludes = ["tkinter"]
packages = ["sys",
            # "PySide2.QtWidgets",
            "os", 
            "urllib.request", 
            "datetime",
            "json",
            "time",
            # "pyodbc",
            ]

setup(
    name = "searchBlog",
    description='Search Blog',
    # version=__version__,
    options = {"build_exe": {
    'packages': packages,
    'include_files': include_files,
    # 'excludes': excludes,
    'include_msvcr': True,
}},
executables = [Executable("naverAPI_search.py",base="Win32GUI")]
)
"""