#
# Honeybee: A Plugin for Environmental Analysis (GPL) started by Mostapha Sadeghipour Roudsari
# 
# This file is part of Honeybee.
# 
# Copyright (c) 2013-2017, Mostapha Sadeghipour Roudsari <mostapha@ladybug.tools> 
# Honeybee is free software; you can redistribute it and/or modify 
# it under the terms of the GNU General Public License as published 
# by the Free Software Foundation; either version 3 of the License, 
# or (at your option) any later version. 
# 
# Honeybee is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of 
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.
# 
# @license GPL-3.0+ <http://spdx.org/licenses/GPL-3.0+>


"""
Daysim's electrical lighting use

-
Provided by Honeybee 0.0.61

    Args:
        _htmlReport: Address to a valid .htm file generated by daysim.
    Returns:
        electricLightingUse: Lists of annual occupancy profiles if any
"""
ghenv.Component.Name = "Honeybee_Daysim Electrical Lighting Use"
ghenv.Component.NickName = 'DSElectricalLightingUse'
ghenv.Component.Message = 'VER 0.0.61\nFEB_05_2017'
ghenv.Component.IconDisplayMode = ghenv.Component.IconDisplayMode.application
ghenv.Component.Category = "Honeybee"
ghenv.Component.SubCategory = "04 | Daylight | Daylight"
#compatibleHBVersion = VER 0.0.56\nFEB_01_2015
#compatibleLBVersion = VER 0.0.59\nFEB_01_2015
try: ghenv.Component.AdditionalHelpFromDocStrings = "5"
except: pass

def main(htmlReport):
    
    if htmlReport==None: return
    
    selectedLines = []
    with open(htmlReport, "r") as report:
        lines = report.readlines()
    
    for lineCount, line in enumerate(lines):
        if line.strip().startswith("<u>Electric Lighting Use:</u>"):
            break
            
    for line in lines[lineCount+1:]:
        if line.startswith("<li>"):
            report = line.strip("<li>")[:-6]
            selectedLines.append(report)
        elif line.startswith("</ul>"):
            break
    
    return selectedLines

electricLightingUse = main(_htmlReport)