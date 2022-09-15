import platform, sys, cpuinfo

pc_info = f"""Про комп'ютер:\n
Мережеве ім'я ПК:              {platform.node()}
Процесор:                       {cpuinfo.get_cpu_info()['brand_raw']}
Ім'я:                                    {platform.system()}
Випуск:                              {platform.release()}
Версія:                               {platform.version()}
Архітектура бітів:          {platform.architecture()[0]}"""


python_info = f"""О Python:\n
Дата складання:                               {platform.python_build()[1]}
Імплементація Python:          {platform.python_implementation()}
Версія Python:                           {platform.python_version()}
Шлях до Python:                            {sys.executable}"""
