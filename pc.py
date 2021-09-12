import platform, sys, cpuinfo

pc_info = f"""О компьютере:\n
Сетевое имя ПК:              {platform.node()}
Процессор:                       {cpuinfo.get_cpu_info()['brand_raw']}
Имя:                                    {platform.system()}
Выпуск:                              {platform.release()}
Версия:                               {platform.version()}
Архитектура битов:          {platform.architecture()[0]}"""


python_info = f"""О Python:\n
Дата сборки:                               {platform.python_build()[1]}
Имплементация Python:          {platform.python_implementation()}
Версия Python:                           {platform.python_version()}
Путь к Python:                            {sys.executable}"""