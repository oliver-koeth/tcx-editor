"""Some functions for reading a TCX file (specifically, a TCX file
downloaded from Strava, which was generated based on data recorded by a
Garmin vívoactive 3) and creating a Pandas DataFrame with the data.
"""

from datetime import datetime, timedelta
from typing import Dict, Optional, Any, Union, Tuple

import xml.etree.ElementTree as ET
import lxml.etree
import pandas as pd
import dateutil.parser as dp

NAMESPACES = {
    'ns': 'http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2',
    'ns2': 'http://www.garmin.com/xmlschemas/UserProfile/v2',
    'ns3': 'http://www.garmin.com/xmlschemas/ActivityExtension/v2',
    'ns4': 'http://www.garmin.com/xmlschemas/ProfileExtension/v1',
    'ns5': 'http://www.garmin.com/xmlschemas/ActivityGoals/v1'
}

def main():
    tcx_tree = ET.parse('data/treadmill_uphill.tcx')
    tcx_root = tcx_tree.getroot()
    tcx_root.get

if __name__== "__main__" :
    main()
