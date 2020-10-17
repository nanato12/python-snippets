""" zoneinfo module """

from datetime import datetime
from zoneinfo import ZoneInfo

tokyo = ZoneInfo("Asia/Tokyo")

now = datetime(2020, 10, 1, 0, 0, 0, tzinfo=tokyo)
print("now = datetime(2020, 10, 1, 0, 0, 0, tzinfo=tokyo)")
print("now.isoformat() => {}".format(now.isoformat()))
