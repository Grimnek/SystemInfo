import platform, sys, cpuinfo

pc_info = f"""О компьютере:\n
Network Name:                  {platform.node()}
Processor:                            {cpuinfo.get_cpu_info()['brand_raw']}
System Name:                    {platform.system()}
Release:                               {platform.release()}
Version:                               {platform.version()}
Architecture (bits):            {platform.architecture()[0]}"""


python_info = f"""О Python:\n
Build Date:                                    {platform.python_build()[1]}
Python Implementation:            {platform.python_implementation()}
Python Version:                           {platform.python_version()}
Python Path:                                {sys.executable}"""