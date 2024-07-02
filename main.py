from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, PositiveInt


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]


m = Delivery(timestamp='2020-01-02T03:04:05Z', dimensions=['10', '20'])

"""
repr() fonksiyonu, nesnenin insan tarafından okunabilir ve geçerli 
Python ifadesi olarak yeniden oluşturulabilir bir temsiline dönüştürür.
"""
print(repr(m.timestamp))
#> datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
print(m.dimensions)
#> (10, 20)
